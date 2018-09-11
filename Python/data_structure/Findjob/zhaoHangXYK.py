'''

海报覆盖问题

5
1 4
2 6
8 10
3 4
7 10
'''

import sys

# line = sys.stdin.readline().split()
# line = list(map(int, line))
# n = line[0]
#
# data = []
# dict = {}
# for i in range(n):
#     line1 = sys.stdin.readline().split()
#     line1 = list(map(int,line1))
#     x = line1[0]
#     y = line1[1]
#     tmp = [i for i in range(x, x+y)]
#     for j in tmp:
#         if j in dict.keys():
#             dict[j]+=1
#         else:
#             dict[j] = 1
# for k,v in dict.items():
#     if v == 1:
#         print(k)



def test(val,dict=[]):
    dict.append(val)
    return dict

print(test(10))
print(test(20,[]))
print(test('a'))

dic1  = dict(zip(['a','b','c','d'],[1,2,3,4]))
dic2 = [i for i in range(5)]
dic3 = [i for i in dic2]

print(dic1)
print(dic2)
print(dic3)

if 'a' in dic1:
    print('123')



