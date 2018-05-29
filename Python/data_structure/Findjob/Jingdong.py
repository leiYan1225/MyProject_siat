import sys
## 给定一个整数是否可以分解成一个基数和一个偶数相乘

#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     num = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         num.append(values[0])
#
#     for N in num:
#         result = N & (N - 1)  # 判断是否为2的幂次
#         if result == 0:
#             print("%d是2的幂次，请重新输入" % N)
#         else:
#             if (N & 1):
#                 print("NO")
#             else:
#                 x = 0
#                 while ((N & 1) == 0):
#                     x = x + 1
#                     N >>= 1
#                 print(N, 2 * x)

## 统计去除字符串后构成回文串的方案数

# s = sys.stdin.readline().strip()
s = 'XXY'
s_list = list(s)
re_s = list(reversed(s))
re_str = ''.join(re_s)
n1 = len(re_str)


def isHw(a): # 输入一个list
    a_list = list(reversed(a))  # reversed()函数可以对list 或者str 进行翻转
    if a_list ==a:
        return True
    else:
        return False

## 只考虑了去除的相邻的n个元素。。。。
n = 0
for x in range(len(s_list)-1):
    for i in range(len(s_list)-x):
        left = s_list[:i]
        right = s_list[i+x+1:]
        res = left + right
        print(res)
        if isHw(res):
            n = n+1
print(n)
# x = 0
# for i in range(len(s_list)-x):
#     left = s_list[:i]
#     right = s_list[i+x+1:]
#     res = left + right
#     print(res)

