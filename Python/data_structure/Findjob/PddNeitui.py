## 第二题

'''
3 4
.oxo
o..o
.xox

6 4
.oxo
o..o
.xox
.oxo
o..o
.xox

思路：
从最后一行开始遍历数组，找到 'o'的位置，判断
- 如果是在最后一行，则直接赋值为'.'
- 如果不在最后一行，记录一个k = i+1,滑落到最后一个'.'出现的位置，再将该位置赋值为'o',原位置赋值为'.'
'''
import sys

def floor(data,n,m):
    for i in range(n-1,-1,-1):
        for j in range(m):
            if 'o' == data[i][j]:
                k = i+1
                while (k<n and '.' in data[k][j]):
                    k += 1
                if k >= n:
                    data[i][j] = '.'
                elif k-1 >= 0 and k-1 != i:
                    data[i][j] = '.'
                    data[k-1][j] = 'o'
    return data

if __name__ == '__main__':
    line = sys.stdin.readline().split()
    line = list(map(int, line))

    data = []
    for i in range(line[0]):
        line1 = sys.stdin.readline().strip()
        data.append(list(line1))
    n = line[0]
    m = line[1]
    data1 = floor(data, n, m)
    for i in range(n):
        str1 = ''.join(data1[i])
        print(str1)





# def trans(m):
#     a = [[] for i in m[0]]
#     for i in m:
#         for j in range(len(i)):
#             a[j].append(i[j])
#     return a
#
# qp = trans(qipan)
#
#
# for i in range(line[1]):
#     if 'x' not in qp[i]:
#         qp[i] = ['.']*line[0]
#     else:
#         countX = str(qp[i][:]).count('x')
#         for j in range(countX):
#             index = qp[i].index('x')
#             countO = str(qp[i][0:index]).count('o')
#             if countO == 1:
#                 qp[i][(index - countO):index] = 'o'
#
#             elif countO ==0:
#                 qp[i][(index - countO):index] = ['.']*countO
#             else:
#                 qp[i][(index - countO):index] = ['o']*countO
#             qp[i][index] = 'm'
#             countD = str(qp[i][0:index]).count('.')
#             qp[i][0:(index - countO)] = ['.'] * countD






