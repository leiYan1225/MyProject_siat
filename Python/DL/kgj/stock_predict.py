# coding=utf-8
'''
Created on 2017楠烇拷2閺堬拷19閺冿拷

@author: Lu.yipiao
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('kgj_data',names=['date','flow'])
df1 = df.groupby(by='date')['flow'].sum()
df1 = pd.DataFrame(df1)
print(df1)
data=np.array(df1['flow'])
data=data[::-1]

plt.figure()
plt.plot(data)
plt.show()
normalize_data=(data-np.mean(data))/np.std(data)
normalize_data=normalize_data[:,np.newaxis]


time_step=20
rnn_unit=10
batch_size=60
input_size=1
output_size=1
lr=0.0006
train_x,train_y=[],[]
for i in range(len(normalize_data)-time_step-1):
    x=normalize_data[i:i+time_step]
    y=normalize_data[i+1:i+time_step+1]
    train_x.append(x.tolist())
    train_y.append(y.tolist()) 



X=tf.placeholder(tf.float32, [None,time_step,input_size])
Y=tf.placeholder(tf.float32, [None,time_step,output_size])

weights={
         'in':tf.Variable(tf.random_normal([input_size,rnn_unit])),
         'out':tf.Variable(tf.random_normal([rnn_unit,1]))
         }
biases={
        'in':tf.Variable(tf.constant(0.1,shape=[rnn_unit,])),
        'out':tf.Variable(tf.constant(0.1,shape=[1,]))
        }



def lstm(batch):
    w_in=weights['in']
    b_in=biases['in']
    input=tf.reshape(X,[-1,input_size])
    input_rnn=tf.matmul(input,w_in)+b_in
    input_rnn=tf.reshape(input_rnn,[-1,time_step,rnn_unit])
    cell=tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    init_state=cell.zero_state(batch,dtype=tf.float32)
    output_rnn,final_states=tf.nn.dynamic_rnn(cell, input_rnn,initial_state=init_state, dtype=tf.float32)
    output=tf.reshape(output_rnn,[-1,rnn_unit])
    w_out=weights['out']
    b_out=biases['out']
    pred=tf.matmul(output,w_out)+b_out
    return pred,final_states



# def train_lstm():
#     global batch_size
#     pred,_=lstm(batch_size)
#
#     loss=tf.reduce_mean(tf.square(tf.reshape(pred,[-1])-tf.reshape(Y, [-1])))
#     train_op=tf.train.AdamOptimizer(lr).minimize(loss)
#     saver=tf.train.Saver(tf.global_variables())
#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#         for i in range(10000):
#             step=0
#             start=0
#             end=start+batch_size
#             while(end<len(train_x)):
#                 _,loss_=sess.run([train_op,loss],feed_dict={X:train_x[start:end],Y:train_y[start:end]})
#                 start+=batch_size
#                 end=start+batch_size
#                 if step%100==0:
#                     print(i,step,loss_)
#                     print("保存模型：",saver.save(sess,'./savemodel/kgj.ckpt'))
#                 step+=1

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
        for i in range(10000):
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


# train_lstm()


def prediction():
    pred,_=lstm(1)
    saver=tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        module_file = './savemodel/kgj.ckpt'
        saver.restore(sess, module_file) 

        prev_seq=train_x[-1]
        predict=[]
        for i in range(7):
            next_seq=sess.run(pred,feed_dict={X:[prev_seq]})
            predict.append(next_seq[-1])
            prev_seq=np.vstack((prev_seq[1:],next_seq[-1]))
        plt.figure()
        plt.plot(list(range(len(normalize_data))), normalize_data, color='b')
        plt.plot(list(range(len(normalize_data), len(normalize_data) + len(predict))), predict, color='r')
        plt.show()

# prediction()
