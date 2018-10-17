

import sys


def func(a, b, c):
    t = a % b
    temp = t
    for i in range(b):
        if temp == c:
            return "YES"
        else:
            temp = (temp+t) % b
    return "NO"


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        line = [int(i) for i in line.split(' ')]
        arr.append(line)
    for i in range(n):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[i][2]
        lst = func(a, b, c)
        print(lst)