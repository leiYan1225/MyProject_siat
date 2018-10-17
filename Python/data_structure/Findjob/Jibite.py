



# def func(a,b,c):
#     r = 1
#     a%=c
#     while(b>1):
#         if (b&1)!=0:
#             r = (r*a)%c
#         a = (a*a)%c
#         b//=2
#     return (r*a)%c
#
#
# if __name__ == '__main__':
#     a, b, c = map(int, input().split())
#     print(func(a, b, c))

n,m = map(int, input().split())
data = []
for i in range(n):
    line = input().split()
    line = list(map(int,line))
    data.append(line)

result = 1
num1 = 0
num0 = 0
for i in range(n):
    num1 +=data[i].count(1)
    num0 += data[i].count(0)

result +=num1
result+=num0
print(result)

# leetcode 岛屿的个数
def infect(arr, i, j,  w,  h):
    if (i < 0 or i >= h or j < 0 or j >= w or arr[i*w + j] != 1):
        return w
    arr[i*w+j] = 2
    infect(arr, i - 1, j, w, h)
    infect(arr, i + 1, j, w, h)
    infect(arr, i, j - 1, w, h)
    infect(arr, i, j + 1, w, h)

def calcIsland(arr,  w,  h):
    res = 0
    for i in range(h):
        for j in range(w):
            if arr[i*w + j] == 1:
                res+=1
                infect(arr, i, j, w, h)
    return res


