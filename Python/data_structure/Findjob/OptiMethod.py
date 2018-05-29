'''
Newton法

函数 f(x) = 6*x**5-5*x**4-4*x**3+3*x**2
梯度 g(x) = 30*x**4-20*x**3-12*x**2+6*x
'''

'''
from scipy.optimize import newton
from numpy.testing import assert_almost_equal

def newtons_method(f, df, x0, e):
    delta = abs(0-f(x0)) # 计算f(x0)=0的误差
    while delta > e:
        x0 = x0 - f(x0)/df(x0) #更新x0
        delta = abs(0-f(x0))  #更新误差
    return x0

def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2

def df(x):
    return 30*x**4-20*x**3-12*x**2+6*x

def test_with_scipy(f, df, x0s, e):
    for x0 in x0s:
        my_newton = newtons_method(f, df, x0, e)
        print(my_newton)
        scipy_newton = newton(f, x0, df, tol=e)
        print(scipy_newton)
        assert_almost_equal(my_newton, scipy_newton, decimal=5,err_msg="有x不满足大致相等啊！")
        print('Tests passed.')

if __name__ == '__main__':
    # run test
    x0s = [-10, -5, -0.1] ## x0初始值取-10, -5, -0.1三个值，然后计算delta
    test_with_scipy(f, df, x0s, 1e-10)
    # error 的选择也很重要，如果选择 1e-5 的话，
    # 就会出现my_newton得到的x值有不满足与sci_newton得到的x值 大致相等 这一条件
'''

'''
梯度下降法

函数 y=2 * (x1) + (x2) + 3
'''
import numpy as np
import matplotlib.pyplot as plt

#
rate = 0.001
x_train = np.array([[1, 2],    [2, 1],    [2, 3],    [3, 5],    [1, 3],    [4, 2],    [7, 3],    [4, 5],    [11, 3],    [8, 7]])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test  = np.array([[1, 4],    [2, 2],    [2, 5],    [5, 3],    [1, 5],    [4, 1]])

a = np.random.normal()
b = np.random.normal()
c = np.random.normal()

def h(x):
    return a*x[0]+b*x[1]+c

for i in range(10000):
    sum_a=0
    sum_b=0
    sum_c=0
    for x, y in zip(x_train, y_train): # zip() 打包为元组的列表
        sum_a = sum_a + rate * (y - h(x)) * x[0]
        sum_b = sum_b + rate * (y - h(x)) * x[1]
        sum_c = sum_c + rate * (y - h(x))

    a = a + sum_a #更新参数
    b = b + sum_b
    c = c + sum_c
    plt.plot([h(xi) for xi in x_test])

print(a)
print(b)
print(c)

result=[h(xi) for xi in x_train]
print(result)

result=[h(xi) for xi in x_test]
print(result)

plt.show() # 图像表示随着训练数据越多，迭代次数越多就越接近真值