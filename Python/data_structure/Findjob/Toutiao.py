
import sys


line1=sys.stdin.readline().strip()
str1 = ''
while line1:
    line1 = sys.stdin.readline().strip()
    str1 +=line1
print(str1)

list1 = []
num = 0





def isOne(str):
    zhushi = []
    for i in range(len(str)):
        flag1 = False
        flag2 = False
        if str[i] =='"':
            flag1 = True
        for j in range(i+1, len(str)) :
            if str[j] == '"' and flag1 ==True :
                flag1 = False
                zhushi.append(str[i])
                zhushi.append(str[j])
        if str[i] =='//':
            flag2 = True
            i+=1
        if str[i] =='//' and flag2==True:
            flag2= False
            zhushi.append(i)
    return zhushi

print(isOne(str1))