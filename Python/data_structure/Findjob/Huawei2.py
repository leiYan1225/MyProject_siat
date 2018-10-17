


dr = [1,0,-1,0]
dc = [0,-1,0,1]

def dfs(matrix,x,y,cache):
    if cache[x][y]:
        return cache[x][y]
    res = 1
    for i in range(4):
        nx = x+dr[i]
        ny = y+dc[i]
        if nx < 0 or nx >= matrix.size() or ny < 0 or ny >= len(matrix[0]) or matrix[nx][ny] >= matrix[x][y]:
            continue
        res = max(res,dfs(matrix,nx,ny,cache)+1)
        return cache[x][y] == res

def lonPath(matrix):
    if matrix is None or matrix[0] is None:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    cache = [[0]*n for i in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            cache[i][j] = dfs(matrix,i,j,cache)
            res = max(res,cache[i][j])

    return res


m,n,h = map(int,input().split())

data = []
for i in range(m):
    line = input().split()
    line = list(map(int,line))
    data.append(line)


result = lonPath(data)
print(result)









