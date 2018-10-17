

'''
5 20
18 19 17 6 7


'''

# 变种1：在arr中找到第一个大于等于val的值
def bs(arr,val):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (right+left)//2
        if arr[mid]>=val:   # 如果题目是大于，这里也改成大于
            right = mid-1
        else:
            left = mid+1
    return arr[left]

n,x= map(int,input().split())
data = list(map(int,input().split()))
data.sort()
#
# minn = 100000
# for i in range(n-1,1,-1):
#     tmp = data[0]+data[i]
#     if tmp>x:
#         minn = min(tmp,minn)
#     elif tmp ==x:
#         minn = x
#     else:
#         tmp = data[0]+data[1]+data[i]
#         if tmp>x:
#             minn = min(tmp, minn)
#         elif tmp == x:
#             minn = x
#         else:
#             tmp = data[0]+data[1]+data[2]+data[i]
#             if tmp > x:
#                 minn = min(tmp, minn)
#             elif tmp == x:
#                 minn = x
#             minn = min(tmp,minn)
# print(minn)


minnum = 100000
for i in range(n):
    if data[i]>x:
        break
    elif data[i] ==x:
        minnum = x
    else:
        a = x-data[i]
        b = bs(data,a)
        tmp = data[i]+b
        minnum = min(tmp,minnum)
print(minnum)



t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    if 0 in data:
        print('No')
    else:
        s = sum(data)
        if s ==(n-1)*2:
            print('Yes')
        else:
            print('No')

