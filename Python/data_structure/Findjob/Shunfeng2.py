# '''
# 排排坐吃果果
#
# 3
# 1
# 0
# 2
#
# '''
# import sys
# n = int(input())
# data = []
# for i in range(n):
#     line = sys.stdin.readline().split()
#     line = list(map(int,line))
#     data.append(line[0])
#
#
# def func(data,num,a):
#     if a == n-1:
#         return num
#     minn = data.index(min(data))
#     if a-1 == minn:
#         num = num+2
#     elif a+1 == minn:
#         num=num+2
#     else:
#         num = num + 1
#     m = func(data[:minn],num,minn)
#     func(data[minn+1:],m,minn)
#
# num =0
# minn = data.index(min(data))
# print(func(data,num,minn))
#


'''
edit distance (leetcode)

'''

def minDistance(word1, word2):
    m = len(word1) + 1
    n = len(word2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i] = i
    for i in range(m):
        dp[i][0] = i
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
    return dp[m - 1][n - 1]

a = str(input())


print('slep','slap','step')