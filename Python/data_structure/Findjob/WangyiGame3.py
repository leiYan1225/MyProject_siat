'''

input:
5
1 21 168 110
2 24 170 120
3 26 170 130
4 22 173 120
5 23 180 130

output:
1 2 10.63
2 4 3.61
3 2 10.2
4 2 3.61
5 3 10.44
'''
import sys
import math

n = int(input())
data = []
for i in range(n):
    dic = {}
    line = sys.stdin.readline().split()
    line = list(map(int, line))
    data.append(line)

result = []
list1 = [i for i in range(n,-1)]
for i in range(n):
    id1,id2 = 0,0
    val = 1000000
    for j in range(n):
        if j!=i:
            tmp = pow(data[i][1] - data[j][1], 2) + pow(data[i][2] - data[j][2], 2) + pow(data[i][3] - data[j][3], 2)
            tmp1 = round(math.sqrt(tmp), 2)
            if tmp1 < 20 and tmp1<val:
                val = tmp1
                id1 = data[i][0]
                id2 = data[j][0]
    result.append([id1, id2, val])

for i in range(len(result)):
    print(result[i][0],result[i][1],result[i][2])

