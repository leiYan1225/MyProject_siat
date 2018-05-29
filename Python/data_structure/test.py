

def testFun():
    temp = [lambda x:i*x for i in range(4)]
    return temp

for everyLambda in testFun():
    print(everyLambda(2))

def adder(x):
    def wrapper(y):
        return x + y**2
    return wrapper

adder5 = adder(5)
# 输出 15
print(adder5(10))
# 输出 11
adder5(6)


try:
    a = input()
except IOError:
    print("error:缺少输入")
else:
    print(a)
