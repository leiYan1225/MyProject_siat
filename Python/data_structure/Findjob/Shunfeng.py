#
# '''
#
# 6
# 1
# 1
# 1
# 2
# 2
# 3
# '''
# import sys
#
# n = int(input())
#
# num = []
#
# for i in range(n):
#     arr = sys.stdin.readline().split()
#     arr = list(dic(int, arr))
#     num.append(arr[0])
#
#
# def topk(nums):
#     set01 = set(num)
#     dic = {}
#     for item in set01:
#         dic.update({item: num.count(item)})
#
#     L = sorted(dic.items(), key=lambda item: item[1], reverse=True)
#     L = L[:2]
#     dictdata = {}
#     for l in L:
#         dictdata[l[0]] = l[1]
#     return sum(dictdata.keys())
#
# print(topk(num))
#
#
# def schedule(data):
#     ls = sorted([x[1], x[0]] for x in data)
#     end = -0x7FFFFFF
#     ans = 0
#     for e, s in ls:
#         if s >= end:
#             end = e
#             ans += 1
#     return n - ans
#


# _data_cnt = 0
# _data_cnt = int(input())
# _data_i=0
# _data = []
# while _data_i < _data_cnt:
#     _data_item = float(input())
#     _data.append(_data_item)
#     _data_i+=1
# print(_data)

# -*- coding:utf-8 -*-
import sys


def main():
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        line = [int(i) for i in line.split()]
        if line[0] > line[1]:
            line[0], line[1] = line[1], line[0]
        lst.append(line)
    ls = sorted([x[1], x[0]] for x in lst)
    end = -0x7FFFFFF
    ans = 0
    for e, s in ls:
        if s >= end:
            end = e
            ans += 1
    print(n-ans)


# def topk(nums):
#     if len(nums) == 0:
#         return 0
#
#     dic = {}
#     for i in nums:
#         if dic.get(i, 0) != 0:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#
#     first, second = sorted(list(dic.values()), reverse=True)[:2]
#     # print first, second
#
#     for i in nums:
#         if dic[i] == first:
#             a = i
#             break
#
#     for i in nums:
#         if dic[i] == second and i != a:
#             b = i
#             break
#
#     return a + b
#
#
# if __name__ == '__main__':
#     main()

n = int(sys.stdin.readline().strip())
lst = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line = [int(i) for i in line.split()]
    if line[0] > line[1]:
        line[0], line[1] = line[1], line[0]
    lst.append(line)
print(line)