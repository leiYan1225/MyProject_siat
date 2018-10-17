'''
2
5 5
#####
#...#
#...#
#.#.#
#E#S#
9 5
#########
#.#.#.#.#
S.......E
#.#.#.#.#
#########

output:
7
17
'''
import sys


def findSE(data):
    n,m = len(data),len(data[0])
    flagS,flagE = -1,-1
    xS,yS = 0,0
    xE,yE = 0,0
    if 'S' in data[0]:
        flagS = 0
        xS,yS = 0,data[0].index('S')
    if 'E' in data[0]:
        flagE = 0
        xE,yE = 0, data[0].index('E')
    if 'S' in data[-1]:
        flagS = 2
        xS, yS = n-1, data[-1].index('S')
    if 'E' in data[-1]:
        flagE = 2
        xE, yE = n-1, data[-1].index('E')
    for i in range(1,n-1):
        if 'S' == data[i][0]:
            flagS = 3
            xS, yS = i,0
        elif 'S' == data[i][-1]:
            flagS = 1
            xS, yS = i, m-1
        if 'E' == data[i][0]:
            flagE = 3
            xE, yE = i,0
        elif 'E' == data[i][-1]:
            flagE = 1
            xE, yE = i, m - 1
    # return flagS,flagE,[xS,yS],[xE,yE]

    while xS ==xE and yS==yE:
        if flagS ==0:
            print()#----------------------------




num = int(input())
for i in range(num):
    data = []
    line = sys.stdin.readline().split()
    n = int(line[0])
    m = int(line[1])
    for j in range(m):
        line1 = sys.stdin.readline().strip()
        data.append(list(line1))

    print(data)
    print(findSE(data))