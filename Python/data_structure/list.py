#
#
# #数组的初始化
# #直接初始化
# a = [1,2,3]
# b = [[1,2,3],[2,3,4]]
#
# #间接初始化
# c = range(1,4)
# d = [0 for i in range(4)] #一维数组
# e = [[0 for col in range(4)] for row in range(5)] #多维数组
#
# print(c)

# python 判断奇偶
n = 1
# if n%2 ==1:
#     print("奇数")
# else:
#     print("偶数")
#或者
# if n&1:
#     print("奇数")
# else:
#     print("偶数")


# #sigmoid 函数
import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    return 1.0/(1.0+np.exp(-1*(x-1)))

def tanh(x):
    y = (1.0-np.exp(-2*x))/(1.0+np.exp(-2*x))
    return y

x = np.arange(-20.,20.,0.2)
sig = sigmoid(x)
tah = tanh(x)
plt.plot(x,sig)
plt.show()















