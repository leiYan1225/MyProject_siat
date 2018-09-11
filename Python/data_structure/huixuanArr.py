
## 回旋矩阵

def generateMatrix(n):
    arr = [[0 for i in range(n)] for i in range(n)]
    chose = 0
    a = 0
    i,j = 0,0
    arr[i][j] = a
    weight = 0

    while a < n*n:
        if chose == 0:
            j+=1
            arr[i][j] = a
            if j == n - weight:
                chose = 1
        if chose == 1:
            i+=1
            arr[i][j] =a
            if i == n - weight:
                chose = 2
        if chose ==2 :
            j-=1
            arr[i][j] = a
            if j == weight -1:
                chose =3
        a+=1


# def func(arr,m,n):
#     arr1 = [[1 for i in range(n)] for i in range(m)]
#     i,j =0,0
#     while i<n and j<m:
#         if i
#
#
#     return arr1

arr = [[0,0,1],[0,1,1],[1,0,1]]
arr[0][:] = [0]*3
arr[:][0] = [0]*3
print(arr)
