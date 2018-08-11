
import tensorflow as tf
import numpy as np

# tf.transpose()
# 函数作用：交换输入张量的不同维度
A = np.array([[1, 2, 3], [4, 5, 6]])
x = tf.transpose(A, [1, 0]) # 作用：行列转置， [1,0] 1表示列，0表示行

B = np.array([[[1, 2, 3], [4, 5, 6]]])
y = tf.transpose(B, [2, 1, 0])

with tf.Session() as sess:
    print(A)
    print(sess.run(x))
    print('-------------------')
    print(B)
    print(sess.run(y))

