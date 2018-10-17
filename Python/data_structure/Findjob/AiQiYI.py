

# n = int(input())
# data = input().split()
# data = list(map(int,data))
# dic = {}
# for i in data:
#     a = 1
#     if i in dic:
#         a=a+1
#     dic[i] = a
# print(max(dic.values()))

if __name__ == '__main__':
    n = int(input())
    data = input().split()
    data = list(map(int, data))

    set01 = set(data)
    dic = {}
    for i in set01:
        dic.update({i: data.count(i)})
    print(max(dic.values()))