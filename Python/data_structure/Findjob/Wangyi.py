
# case = [3,3]
# job = [[1,100],[10,1000],[1000000000,1001]]
# nubi = [9,10,1000000000]
# job_dic = set(job)
# print(job_dic)
#
# def seljob(ai,job):
#     print("12")


def erwei(n):
    line = [[0] * n] * n
    for i in range(n):
        line[i] = list(input())
    return line

def getmid(n):
    if n % 2 == 1:
        mid_num = int((n + 1) / 2 - 1)
        mid = line[mid_num][mid_num]
        return mid
    else:
        print("please input a odd!")

n=int(input("please input a odd N:"))
m=int(input("please input a odd M:"))


line = erwei(n)
line_m =[[0]*m]*m

mid_n = getmid(n)
for i in range(m):
    mid_num = int((m + 1) / 2 - 1)
    line_m[mid_num][mid_num] = mid_n
    for i in range(n):
        for j in range(n):
            line_m[mid_num-i][mid_num-j] =1 ## 未完待续




