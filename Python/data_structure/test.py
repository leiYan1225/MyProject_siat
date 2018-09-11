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


print(recursive_mix(5))
recursive_conversion(23)
# recursive_back(1234)

## 堆栈实现字符串逆序

def func(str):
    lis = list(str)
    result = ''
    while lis:
        result+=result.pop()
    return result



