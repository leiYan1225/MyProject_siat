# coding=utf-8

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# conn = psycopg2.connect(database="kgj", user="kgj", password="kgj123", host="172.16.100.3", port="5432")
# cur = conn.cursor()
# cur.execute("SELECT depart_date, volume from t_report_lxfx")
# rows = cur.fetchall()
#
# data = pd.DataFrame(list(rows))
# data.to_csv('kgj',header=0,index=0)
# conn.close()




time_step = 20
rnn_unit = 10  # 30  # hidden layer units
batch_size = 30  # 60   # 每一批次训练多少个样例
input_size = 1  # 输入层维度
output_size = 1  # 输出层维度
lr = 0.0006  # 学习率
FLAG = 'train'   # train or test

# ——————————————————导入数据——————————————————————
df = pd.read_csv('kgj_data',names=['date','flow'])
df1 = df.groupby(by='date')['flow'].sum()
df1 = pd.DataFrame(df1)
data=np.array(df1['flow'])   #获取进站数据
plt.plot(data)
plt.show()


normalize_data = (data - np.mean(data)) / np.std(data)  # 标准化
normalize_data = normalize_data[:, np.newaxis]  # 增加维度

data_x, data_y = [], []
for i in range(len(normalize_data) - time_step - 1):
    x = normalize_data[i:i + time_step]
    y = normalize_data[i + time_step]  # 用一天预测下一个5min
    data_x.append(x.tolist())
    data_y.append(y.tolist())
data_y = np.reshape(data_y, (-1, 1, 1))
# 分训练集和测试集
train_num = int(len(data_x)*0.8)
train_x = data_x[0:train_num]
train_y = data_y[0:train_num]
test_x = data_x[train_num:]
test_y = data_y[train_num:]




# —————————————————定义神经网络变量————————————————
X = tf.placeholder(tf.float32, [None, time_step, input_size])
Y = tf.placeholder(tf.float32, [None, 1, output_size])
# 输入层、输出层权重、偏置
weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(1.0, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(1.0, shape=[1, ]))
}


# —————————————————定义神经网络—————————————————
def lstm(batch):
    w_in = weights['in']
    b_in = biases['in']
    X_in = tf.reshape(X, [-1, input_size])  # 将X转换成2维,为了输入层'in'的输入
    input_rnn = tf.matmul(X_in, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])  # 将tensor转换回3维,作为lstm cell的输入
    cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    init_state = cell.zero_state(batch, dtype=tf.float32)
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state,
                                                 dtype=tf.float32)  # output_rnn是记录lstm每个输出节点的结果，final_states是最后一个cell的结果
    outputs = tf.unstack(tf.transpose(output_rnn, [1, 0, 2]))  # 作为输出层'out'的输入
    w_out = weights['out']
    b_out = biases['out']
    pred = tf.matmul(outputs[-1], w_out) + b_out  # time_step只取最后一项
    return pred, final_states, outputs,w_out,b_out


# ——————————————————训练模型——————————————————
def train_lstm():
    global batch_size
    pred, _ = lstm(batch_size)
    # print('train pred', pred.get_shape())
    # 损失函数
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1, 1]) - tf.reshape(Y, [-1, 1])))
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        start = 0
        end = start + batch_size
        for i in range(1000):
            _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[start:end], Y: train_y[start:end]})
            start += batch_size
            end = start + batch_size
            print(i, loss_)
            if i % 100 == 0:
                print("保存模型：", saver.save(sess, './savemodel/kgj.ckpt'))
            if end >= len(train_x):
                start = 0
                end = start + batch_size
    writer = tf.summary.FileWriter("./nn_log", sess.graph)
    writer.close()

                # ————————————————预测模型————————————————————

def prediction():
    global test_y
    pred, _ ,outputs,w_out,b_out = lstm(len(test_x))  # 预测时只输入[test_batch,time_step,input_size]的测试数据
    print('test pred', pred.get_shape())
    saver = tf.train.Saver()
    with tf.Session() as sess:
        # 参数恢复
        module_file = './savemodel/kgj.ckpt'
        saver.restore(sess, module_file)
        # 取测试样本,shape=[test_batch,time_step,input_size]

        test_pred = sess.run(pred, feed_dict={X: test_x})
        test_pred = np.reshape(test_pred, (-1))
        test_y = np.reshape(test_y, (-1))

        # --计算正确率
        test_pred = test_pred*np.std(data)+np.mean(data)
        test_y = test_y*np.std(data)+np.mean(data)

        print("平均绝对误差(MAE):")
        mae = np.mean(np.abs(test_pred - test_y))
        print(mae)
        # Root Mean Square Error
        print("均方根误差(RMSE):")
        rmse = np.sqrt(np.mean(np.square(test_pred-test_y)))
        print(rmse)
        # mean absolute percentage error
        print("相对百分误差(MAPE):")
        mape = np.mean(np.abs(test_pred - test_y)/test_y)
        print(mape)

        # 以折线图表示结果
        plt.figure()
        plt.plot(range(len(test_y)), test_y, 'r-', label='real')
        plt.plot(range(len(test_pred)), (test_pred), 'b-', label='pred')
        plt.legend(loc=0)
        plt.title('buji station prediction')
        plt.show()
        # plt.savefig('bj.jpg', dpi=1000, bbox_inches='tight')


if __name__ == '__main__':
    if FLAG == 'train':
        train_lstm()
    elif FLAG == 'test':
        prediction()