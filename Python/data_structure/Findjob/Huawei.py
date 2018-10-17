'''
大数相乘

解题思路：
    A=13，B=19
    a=(3,1),b=(9,1)
    c=(3∗9,3∗1+1∗9,1∗1)=(27,12,1)=(7,14,1)=(7,4,2)
    C=247

（1）转换并反转，字符串转换为数字并将字序反转；
（2）逐位相乘，结果存放在result_num[i+j]中；
（3）处理进位，消除多余的0；
（4）转换并反转，将计算结果转换为字符串并反转。
'''
def main():
    a = input().strip()
    b = input().strip()
    data1 = list(map(int, a[::-1]))
    data2 = list(map(int, b[::-1]))

    n = len(data1) + len(data2)
    result = [0 for i in range(n)]
    for i in range(len(data1)):  # 将每一位相乘的结果放到result[i+j]中
        for j in range(len(data2)):
            tmp = data1[i] * data2[j]
            result[i + j] += tmp

    for i in range(n - 1):  # 处理进位
        x = result[i] // 10
        y = result[i] % 10
        result[i] = y
        result[i + 1] += x

    result.reverse()  # 翻转并处理多余的0
    for i in range(n):
        if result[i] != 0:
            break
        else:
            result.pop(0)

    data3 = ''.join(list(map(str, result)))
    print(data3)


'''
字符串重排
输入：eeefgghhh
输出：efghegheh

'''

# 查找val为0的key
def func(dic):
    for k,v in dic.items():
        if v ==0:
            return k
    return False


def main2():
    s = input().strip()
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1

    n = sum(dic.values())
    result = [0 for i in range(n)]
    keys = sorted(dic.keys())
    i = 0
    while i < n:
        for k in keys:
            if dic[k] == 0:
                continue
            else:
                result[i] = k
                i += 1
                dic[k] -= 1

    s = ''.join(result)
    print(s)

'''
字符翻转
翻转每个单词
'''

def main3():
    s = input().split(' ')  # 返回一个以空格分割的list
    data = []
    for i in s:
        data.append(i[::-1])
    print(' '.join(data))



