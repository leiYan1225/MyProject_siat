# '''
# 4 1 0 0 1 -1 0 0 -1
# 2 0 0 1 1
#
# '''
# import sys
# def isPo(point, rangelist):
#     lnglist = []
#     latlist = []
#     for i in range(len(rangelist)-1):
#         lnglist.append(rangelist[i][0])
#         latlist.append(rangelist[i][1])
#     maxlng = max(lnglist)
#     minlng = min(lnglist)
#     maxlat = max(latlist)
#     minlat = min(latlist)
#     if (point[0] > maxlng or point[0] < minlng or
#         point[1] > maxlat or point[1] < minlat):
#         return False
#     count = 0
#     point1 = rangelist[0]
#     for i in range(1, len(rangelist)):
#         point2 = rangelist[i]
#         if (point[0] == point1[0] and point[1] == point1[1]) or (point[0] == point2[0] and point[1] == point2[1]):
#             return False
#         if (point1[1] < point[1] and point2[1] >= point[1]) or (point1[1] >= point[1] and point2[1] < point[1]):
#             point12lng = point2[0] - (point2[1] - point[1]) * (point2[0] - point1[0])/(point2[1] - point1[1])
#             if (point12lng == point[0]):
#                 return False
#             if (point12lng < point[0]):
#                 count +=1
#         point1 = point2
#     if count%2 == 0:
#         return False
#     else:
#         return True
#
#
# if __name__ == '__main__':
#     line = sys.stdin.readline().split()
#     line = list(map(int, line))
#     line1 = sys.stdin.readline().split()
#     line1 = list(map(int, line1))
#     n = line.pop(0)
#     m = line1.pop(0)
#
#     shape = []
#     i = 0
#     while i < len(line):
#         shape.append([line[i], line[i + 1]])
#         i = i + 2
#
#     idot = []
#     i = 0
#     while i < len(line1):
#         idot.append([line1[i], line1[i + 1]])
#         i = i + 2
#
#     num = 0
#     for i in range(m):
#         if isPo(idot[i], shape):
#             num += 1
#     print(num)


# def find_lcseque(s1, s2):
#     m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
#     d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
#
#     for p1 in range(len(s1)):
#         for p2 in range(len(s2)):
#             if s1[p1] == s2[p2]:
#                 m[p1 + 1][p2 + 1] = m[p1][p2] + 1
#                 d[p1 + 1][p2 + 1] = 'ok'
#             elif m[p1 + 1][p2] > m[p1][p2 + 1]:
#                 m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
#                 d[p1 + 1][p2 + 1] = 'left'
#             else:
#                 m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
#                 d[p1 + 1][p2 + 1] = 'up'
#     (p1, p2) = (len(s1), len(s2))
#     s = []
#     while m[p1][p2]:
#         c = d[p1][p2]
#         if c == 'ok':
#             s.append(s1[p1 - 1])
#             p1 -= 1
#             p2 -= 1
#         if c == 'left':
#             p2 -= 1
#         if c == 'up':
#             p1 -= 1
#     s.reverse()
#     return ''.join(s)
#
#
# print(len(find_lcseque('abdfg', 'abcdfg')))


import sys
def lcseque(s1, s2):
    m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                d[p1 + 1][p2 + 1] = 'ok'
            elif m[p1 + 1][p2] > m[p1][p2 + 1]:
                m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                d[p1 + 1][p2 + 1] = 'left'
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                d[p1 + 1][p2 + 1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(s1[p1 - 1])
            p1 -= 1
            p2 -= 1
        if c == 'left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return ''.join(s)

if __name__== '__main__':
    s1 = str(input())
    s2 = str(input())
    print(len(lcseque(s1, s2)))


