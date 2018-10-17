
import sys

def fun(n):
    if(n ==1):
        return 1
    return n*fun(n-1)

def fun1(c,n,a):
    if (c ==n):
        return fun(c)

    res = 0
    i = 0
    for j in range(n):
        if a[j]>a[i]:
            i =j
    j =i
    a[j] -=1
    x = c-2*a[j]
    res = fun1(c-1,n,a)*x
    for i in range(n):
        if i!=j and a[i]>1:
            a[i]-=1
            res=res+2*fun1(c-2,n,a)
            a[i]+=1
    a[j]+=1
    return res

line = sys.stdin.readline().split()
line = list(map(int, line))
np,nq,nr = line[0],int(line[1]),int(line[2])

num = np+nq+nr
n = 3
print(fun1(num,n,line)//(fun(np)*fun(nq)*fun(nr)))