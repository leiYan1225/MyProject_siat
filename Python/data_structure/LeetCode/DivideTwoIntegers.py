

# 两数相除

def divide(a,b):
    c = 0
    while a>=b:
        a = a-b
        c+=1


import sys
def compute(s):
    list = []
    if s is None or len(s)==0:
        return list
    pattern = str(s[0])
    count = 1
    for i in s[1:]:
        if i==pattern:
            count+=1
        else:
            list.append(str(count)+pattern)
            pattern = i
            count = 1
    list.append(str(count)+pattern)
    print(list)
    return list


if __name__=='__main__':
    str1 = sys.stdin.readline().split()#['aaabbccd']
    ls = []
    for i in str1:
        ls.extend(i) #转换成这种形式['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']

    print(compute(ls))
