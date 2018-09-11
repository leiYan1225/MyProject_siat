'''
张博，教师节快乐！
虽然你现在已经远离科研一线，但对曾经在一线奋斗过的你表示致敬！
作为我的老师，不仅仅是知识的传输，更重要的是对我做人的影响，
感谢以往对我的教诲与宽容，以及今后还未到来的帮助；
同时也庆幸我有个这么平易近人的"老板"。
感谢！
'''

import collections
import sys

def func(arr, n):
    result = []
    ori = [i+1 for i in range(n)]
    for i in range(1, n+1):
        arr[i] = list(set(ori) ^ set(arr[i]))
        result.append(arr[i])
    result = list(set([tuple(t) for t in result]))
    result = list(map(lambda x: list(x), result))
    return result


if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    arr1 = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        line = [int(i) for i in line.split(' ')]
        arr1.append(line)
    a = 0
    for i in range(t):
        n = arr1[a][0]
        m = arr1[a][1]
        matrix = arr1[a + 1:m + a + 1]
        a = m + a + 1
        arr2 = collections.defaultdict(list)
        for u, v in matrix:
            arr2[u].append(v)
            arr2[v].append(u)
        # print(dic)
        resultult = func(arr2, n)
        count = 0
        for k in resultult:
            count += len(k)
        if count == n:
            print('Yes')
        else:
            print('No')