# import sys
#
#
# def isRabbit(list1):
#     flag = 'Yes'
#     for i in range(len(list1) - 1):
#         if list1[i] == 0 and list1[i + 1] == 0:
#             flag = 'No'
#     return flag
#
# if __name__ == '__main__':
#     line = sys.stdin.readline().split()  # line[0]、line[1] 分别表示洞的个数和天数
#     day = sys.stdin.readline().split()
#
#     line = list(map(int, line))
#     day = list(map(int, day))
#
#     k = line[0]
#     list1 = [0] * k
#     for i in day:
#         list1[i - 1] = 1
#
#     print(isRabbit(list1))

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
import sys
import numpy as np
if __name__ == '__main__':
    # line = sys.stdin.readline().split()  # line[0]、line[1] 分别表示洞的个数和查看天数
    # day = sys.stdin.readline().split()
    # line = list(map(int, line))
    # day = list(map(int, day))
    line = [3,2]
    day = [2,2]

    k = line[0]
    s = line[1]

    arr1 = np.zeros((s,k+2))
    arr1


    list1 = [[0]*(k+2) for i in range(s)] #初始化一个二维数组 s行k+2列
    list1[0][:] = [1,1,1,1]
    print(arr1)

