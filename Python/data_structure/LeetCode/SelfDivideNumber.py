'''
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

注意：
每个输入参数的边界满足 1 <= left <= right <= 10000。
'''

def isSelfDivide(n):
    str_n = str(n)
    list_n = list(str_n)
    for i in list_n:
        i = int(i)
        if i == 0 or n % i != 0:
            return False
    return True

left = 1
right = 22
result = []
for i in range(left,right+1):
    if isSelfDivide(i):
        result.append(i)
print(result)

a = 'abcd'
s = reversed(a)
print(s)