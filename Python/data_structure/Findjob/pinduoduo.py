
import sys

## 第一题
# if __name__ == '__main__':
#     n = int(sys.stdin.readline().strip())
#     nor = int(sys.stdin.readline().strip())
#     buf = int(sys.stdin.readline().strip())
#     if nor * 2 >= buf:
#         if n % nor == 0:
#             print(n // nor)
#         else:
#             print(n // nor + 1)
#     else:
#         temp = n % buf
#         if temp == n and temp <= nor:
#             print(1)
#         elif temp == n and temp > nor:
#             print(2)
#         elif temp == 0:
#             print(n // buf * 2)
#         elif temp <= nor:
#             print(n // buf * 2 + 1)
#         else:
#             print(n // buf * 2 + 2)


import sys



## 第四题
# if __name__ == '__main__':
#     line = sys.stdin.readline().strip()
#     line = list(map(int,line))
#     n = line[0]
#     l = line[1]
#     res = []
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break
#         res.append(line)
#     lst = []
#     for i in range(l):
#         temp = list(map(lambda x: x[i], res))
#         lst.append(min(temp))
#     lst = ''.join(lst)
#     print(lst)


## 第三题
if __name__ == '__main__':
    x, y = map(int, input().split())

    a = []
    c = 1
    n = x % y
    a.append(n)
    f = 1
    while c:
        n = (10 * n) % y
        if n == 0:
            f = 0
            break
        elif n in a:
            loc = a.index(n)
            break
        else:
            a.append(n)
        c += 1
    if f == 0:
        print(str(c) + ' ' + '0')
    else:
        print(str(loc) + ' ' + str(c - loc))


