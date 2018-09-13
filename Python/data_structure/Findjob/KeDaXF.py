
'''
2
3
10 20 30
4
40 50 60 40

'''
import sys


# line = sys.stdin.readline().split()
# line = list(map(int, line))
# data = []
# for i in range(line[0]):
#     line1 = sys.stdin.readline().split()
#     line1 = list(map(int, line1))
#     for j in range(line1[0]):
#         line2 = sys.stdin.readline().split()
#         line2 = list(map(int, line2))
#         data.append(line2)



## 杀手

import sys

def test(line):
    i = -1
    total = len(line)
    while total != -i:
        if line[i] < line[i-1]:
            line.pop(i)
            total -= 1
        else:
            i -= 1
    return line

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    line = [int(i) for i in line.split(' ')]
    count = 0
    while line != sorted(line):
        line = test(line)
        count += 1
    print(count)
