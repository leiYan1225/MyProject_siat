

'''
comeonmandontconconnect
on
5
1 5
1 6
1 23
11 16
11 23

'''
import sys

if __name__ == '__main__':
    A = str(input())
    B = str(input())
    q = int(input())

    for i in range(q):
        arr = sys.stdin.readline().split()
        arr = list(map(int, arr))
        m = arr[0] - 1
        n = arr[1] - 1
        num = A[m:n + 1].count(B)
        print(num)


