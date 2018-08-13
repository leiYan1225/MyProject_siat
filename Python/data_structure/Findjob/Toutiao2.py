
import sys

'''
10,10
0,0,0,0,0,0,0,0,0,0
0,0,0,1,1,0,1,0,0,0
0,1,0,0,0,0,0,1.0,1
1,0,0,0,0,0,0,0,1,1
0,0,0,1,1,1,0,0,0,1
0,0,0,0,0,0,1,0,1,1
0,1,1,0,0,0,0,0,0,0
0,0,0,1,0,1,0,0,0,0
0,0,1,0,0,1,0,0,0,0
0,1,0,0,0,0,0,0,0,0
'''



# line = sys.stdin.readline().split(',')
# line = list(map(int, line))

# people = []
# for i in range(line[0]):
#     line1 = sys.stdin.readline().strip().split(',')
#     people.append(line1)
# print(people)
#
# def oneGroup(arr):
#     row = len(arr)
#     col = len(arr[0])
#     flag = 0




'''
3
3 2 1
3 3 3

'''

#
# line = sys.stdin.readline().split()
# line = list(map(int, line))
# line1 = sys.stdin.readline().split()
# line1 = list(map(int, line1))
# line2 = sys.stdin.readline().split()
# line2 = list(map(int, line2))
# target = 0
# for i in range(line[0]):
#     for j in range(0,i+1):
#         if max(line1[j:i+1]) < min(line2[j:i+1]):
#             target+=1
# print(target)


'''
4
3 1
2 2
1 4
1 4

'''
line = sys.stdin.readline().split()
line = list(map(int, line))

list1 = []
for i in range(line[0]):
    line1 = sys.stdin.readline().split()
    line1 = list(map(int, line1))
    list1.append(line1)
# print(list1)
a = []
b = []
for j in range(len(list1)):
    a.append(list1[j][0])
    b.append(list1[j][1])
v = list(map(lambda x: x[0]-x[1], zip(a, b)))  #求两list对应元素的差
for k in range(line[0]):
    if sum(v[0:k+1]) == 0:
        print(a[k]+b[k])  # 未完待续


