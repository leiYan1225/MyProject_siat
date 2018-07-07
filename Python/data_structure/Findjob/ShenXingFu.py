'''
The damn rabbit!!!

https://www.zybuluo.com/Zwill/note/1099285
解题思路：动态规划

输入：
3 2
2 2

输出：
Yes

'''
## 感觉可以，但未经线上测试
import sys
# import numpy as np
# if __name__ == '__main__':
    ## split()根据默认分隔字符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
#     # line = sys.stdin.readline().split()  # line[0]、line[1] 分别表示洞的个数和查看天数
#     # day = sys.stdin.readline().split()
#     # line = list(map(int, line))
#     # day = list(map(int, day))
#     line = [5,6]
#     day = [2,2,3,4,4,3]
#     day.reverse()
#
#     k = line[0]
#     s = line[1]
#
#     # arr1 = [[0]*(k+2) for i in range(s)] #初始化一个二维数组 s行k+2列
#     arr1 = np.zeros((s,k+2)) #初始化一个二维数组 s行k+2列
#     for i in range(s): #将每一行的头和尾设置为1
#         arr1[i][0] = 1
#         arr1[i][-1] =1
#     print(arr1)
#     a = s
#     for i in day:
#         arr1[a-1][i] = 1
#         a-=1
#     print('-----------')
#     print(arr1)
#
#     for i in range(s-1,-1,-1):
#         for j in range(k+1):
#             if arr1[i][j-1]==1 and arr1[i][j+1] ==1:
#                 arr1[i-1][j] = 1
#     print('-----------')
#     print(arr1)
#     b = [1] * (k + 2)
#     flag = True
#     for i in range(k+2):
#         if arr1[0][i] ==0:
#             flag =False
#     if flag:
#         print("Yes")
#     else:
#         print("No")
#


'''
派发礼品

输入：
5
1
2
1
3
3

输出：
3
1
2
3

解决思路：
其实就是一个list 去重同时不改变顺序的问题
'''

import sys
a = sys.stdin.readline()# split()根据默认分隔字符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
arr1 = []
for i in range(int(a)):
    m = sys.stdin.readline()
    arr1.append(m.strip())
# for i in sys.stdin: # ctrl+d 结束多行输入
#     if i == '\n':
#         pass
#     else:
#         arr1.append(i.strip())

# a = 5
# # arr1 = [1,2,1,3,3,4,5,11,6,7,8,12,11,15,16,18,17,21]
arr2 = []
[arr2.append(i) for i in arr1 if i not in arr2]
if len(arr2)>10: # 只给前10名发
    arr2 = arr2[0:10]

print(len(arr2))
for i in arr2:
    print(i)


import sys

num = int(sys.stdin.readline().strip('\n'))
users = []
while num < 10:
    users.append(sys.stdin.readline().strip('\n'))
    if len(users) > num - 1:
        break

print('-----------')
new_users = []
for id in users:
    if id not in new_users:
        new_users.append(id)

print(len(new_users))
for id in new_users:
    print(id)