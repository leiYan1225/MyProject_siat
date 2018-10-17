


def Prime():
    maxn = 10000
    prime = [True for i in range(maxn)]
    prime[0] = False
    prime[1] = False
    i = 2
    while i*i < maxn:
        if prime[i]:
            j = i*2
            while j <= maxn:
                prime[j] = False
                j+=i
        i+=1
    return prime

if __name__ == '__main__':
    prime = Prime()
    n = input()
    num = 2
    flag = 0
    for i in range(1, n + 1):
        if prime[i]:
            ans = i
            while ans <= n // i:
                ans *= i
            flag = (n // ans + 1) * ans
            if num < flag:
                num = flag
    print(num)
