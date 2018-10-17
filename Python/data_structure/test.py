# try:
#     a = input()
# except IOError:
#     print("error:缺少输入")
# else:
#     print(a)

# 递归求N!
def recursive_mix(n):
    if n == 2:
        return 1
    return n * recursive_mix(n - 1)


# 十进制转二进制
def recursive_conversion(n):
    if n == 0:
        return

    recursive_conversion(int(n / 2))
    print(n % 2)
    # return n%2


# 递归实现数字倒叙
def recursive_back(n):
    if n == 0:
        return
    print(n % 10)
    recursive_back(int(n / 10))


# print(recursive_mix(5))
# recursive_conversion(23)
# recursive_back(1234)

## 堆栈实现字符串逆序

def func(str):
    lis = list(str)
    result = ''
    while lis:
        result+=result.pop()
    return result


def towSum(num, target):
    d = {}
    for i, val in enumerate(num):
        if target - val in d:
            return [d[target - val], i]
        d[val] = i


# print(towSum([4,2,1,6,7],5))

def withoutRep(s):
    my = ''
    maxlen = 0
    for i in range(len(s)):
        if s[i] not in my:
            my = my+s[i]
        else:
            maxlen = max(maxlen,len(my))
            left = s.index(s[i])+1
            right = i
            my = s[left:right+1]
    return maxlen


def withoutRep1(s):
    temp = 0
    d = {}
    start = 0
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
            start = d[s[i]] + 1
        temp = max(i - start + 1, temp)
        d[s[i]] = i
    return temp

def withoutRep2(s):
    prev = 0
    ans = 0
    sub = ''
    for i in range(len(s)):
        if len(s) - i <= prev:
            break
        while i < len(s) and s[i] not in sub:
            ans += 1
            sub += s[i]
            i += 1
        if prev < ans:
            prev = ans
        ans = 0
        sub = ''
    return prev

print(withoutRep1('pwwkew'))


'''
滑动窗口
维护一个dict,逐一将元素添加进去
若存在重复元素a，则更新dict,并将left设为dic[a]+1
'''
def withoutRept(s):
    dic = {}  ## 用一个dic 来存储
    left = 0
    maxlen = 0
    for i in range(len(s)):
        if s[i] in dic and left <= dic[s[i]]: # 如果出现重复元素a,后面这个and 貌似也很重要。。。
            left = dic[s[i]] +1  # 中
        maxlen = max(maxlen,i-left+1)
        dic[s[i]] = i
    return maxlen


# print(withoutRep1('abba'))

s = 'aaabbcccaa'
def tranStr(s):
    st = ''
    st1 = ''
    for i in range(len(s)-1):
        st1 += s[i]
        if s[i+1] not in st1:
            a = len(st1)
            st = st + str(a)+s[i-1]
            st1 = ''
    return st


print(tranStr(s))
