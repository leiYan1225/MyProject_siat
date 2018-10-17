'''
3 3
27 24 24
28 6 13
10 7 12

'''
import sys
line = sys.stdin.readline().split()
line = list(map(int,line))


def arrXor(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result^=arr[i]
    return result

data = []
for i in range(line[0]):
    line1 = sys.stdin.readline().split()
    line1 = list(map(int, line1))
    data.append(line1)

data1 = []
for i in range(len(data)):
    tmp = arrXor(data[i])
    data1.append(tmp)
data2 = []
for i in range(line[1]):
    temp = [x[i] for x in data]


print(data1)

