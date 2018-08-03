
# import tensorflow as tf
#
# a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
# b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
# c = tf.matmul(a, b)
# # Creates a session with log_device_placement set to True.
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# # Runs the op.
# print(sess.run(c))


# import os
# os.system("{}  {}  {}".format('我', 'B-oiu', '6'))

# dict1 = {'me':1,'is':2,'working':3}
# arr = []
# if 'me' in dict1.keys():
#     print('hahaha')
#     arr.append('me')

# tag_seq = ['B-ORG', 'O', 'O','B-ORG','I-ORG']
# char_seq = ['工','作','的','地','方']
#
# def get_ORG_entity(tag_seq, char_seq):
#     length = len(char_seq)
#     ORG = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'B-ORG':
#             if 'org' in locals().keys():
#                 ORG.append(org)
#                 del org
#             org = char
#             if i+1 == length:
#                 ORG.append(org)
#         if tag == 'I-ORG':
#             org += char
#             if i+1 == length:
#                 ORG.append(org)
#         if tag not in ['I-ORG', 'B-ORG']:
#             if 'org' in locals().keys():
#                 ORG.append(org)
#                 del org
#             continue
#     return ORG
#
# get_ORG_entity(tag_seq,char_seq)

# b = []
# a = [1,2,5,4,3,7,0]
# for i,val in enumerate(a):
#     if (8-val) in a:
#         b.append([i,a.index(8-val)])
#

#-------------------------------------------------------------------------------------------
## str.lower() 转换成小写 .upper()转换陈大写 .title()每个单词第一个字母大写，其余小写
## .capitalize() 把第一个字母转化为大写字母，其余小写----区别于上面的每个单词

# def normalize(name):
#     name = name.capitalize()
#     return name
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#------------------------
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
# def prod(L):
#     return reduce(lambda x,y:x*y ,L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

#------------------------
# 编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# from functools import reduce
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             return f + n / (point * 10)
#     return reduce(to_float, nums, 0.0)
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

#------------------------

#-*- coding:utf-8 -*-
def outer():
    num =10
    def inner():
        nonlocal num # nonlocal关键字声明
        print('inner-nonlocal-num',num)
        num = 100
        print('inner-local-num',num)
    print('outer-local-num',num)
    inner()
    print('outer-inner-local-num',num)
outer()


