import numpy as np

#simple example!

X = [1,2]
state = [0,0]
# 分开定义不同权重以方便操作
w_cell_state = np.asarray([[0.1,0.2],[0.3,0.4]])
w_cell_input = np.asarray([0.5,0.6])
b_cell = np.asarray([0.1,-0.1])

#定义用于输出的全连接层的参数
w_output = np.asarray([[1.0],[2.0]])  #列向量的定义方式，区别于[1，2]
b_output = 0.1

#按照时间顺序执行rnn的前向传播过程
for i in range(len(X)):
    before_activation = np.dot(state,w_cell_state)+X[i]*w_cell_input+b_cell
    state = np.tanh(before_activation)
    final_output = np.dot(state,w_output)+b_output

    print("before activation:",before_activation)
    print("state:",state)
    print("output:",final_output)
