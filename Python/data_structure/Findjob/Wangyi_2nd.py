import sys

def getAB(a):
    a_list = list(a)
    a_len = len(a_list)
    yunsuan = []
    for i in range(a_len):
        if a_list[i] == "+" or a_list[i] == "-" or a_list[i] == "*" or a_list[i] == "/":
            num1 = a_list[:i]
            yunsuan.append(a_list[i])
            b = a_list[i + 1:]
            for j in range(len(b)):
                if b[j] == "=":
                    num2 = b[:j]
                    num3 = b[j+1:]
                    return num1,num2,num3,yunsuan

# def getLetter(a):
#     getNum = []
#     getLe = []
#     a_len = len(a)
#     for i in range(a_len):
#         if a[i].isalpha():
#             print(a[i])


def tihuan(a,b,c):
    for i in range(len(a)):
        if a[i] ==str(b):
            a[i] =c
    return a
# print(tihuan([1,2,'A'], "A",3))

# 12A+BB4=239

a = sys.stdin.readline().strip()
num1,num2,num3,yunsuan = getAB(a)

def gw(a,b,c):
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)
    if a_len > b_len:
        for i in range(b_len):
            if b[b_len-i-1].isalpha():
                let=b[b_len-i-1]
                b[b_len - i - 1] = int(c[c_len-i-1])-int(a[a_len-i-1])
                return b,let
    else:
        for i in range(a_len):
            if a[a_len-i-1].isalpha():
                let = a[a_len - i - 1]
                a[a_len - i - 1] = int(c[c_len-i-1])-int(b[b_len-i-1])
                return a, let

print(gw(num1,num2,num3))






