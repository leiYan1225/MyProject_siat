'''
bwbwb

'''

import sys
def isgood(arr):
    list1 = []
    flag = False
    n = len(arr)
    while n:
        if n == 1:
            flag = True
        elif arr[n - 1] != arr[n - 2]:
            flag = True
        else:
            flag = False
        n = n - 1
    return flag

def func(line):
    res = []
    for j in range(1, len(line)):
        result = 0
        if isgood(line[:j]):
            result = j + 1
        else:
            if line[0] != line[-1]:
                result = result + 1
                line[j:] = line[j].reverse()
        res.append(result)
    return max(res)

arr1 = list(sys.stdin.readline().strip())
print(func(arr1))