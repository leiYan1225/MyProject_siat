

# 找最可能认识的人
'''
input:
5 0
1 2 3
0 4
0 4
0 4
1 2 3
output：
4
-------------
input:
6 0
1 2 3
0 4 5
0 4 5
0 4 5
1 2 3
1 2 3
output：
4
'''
'''
思路：
定义一个二维list:arr 来存储输入数组
1. 从arr 中取出给定用户的朋友列表arr0
2. 将所有用户列表于上诉列表做差集,并去除给定的用户自身，即得到给定用户的非朋友列表arr2
3. 循环遍历arr2,取arr0与arr[i]的交集元素个数(i 表示用户编号)，存入字典，key:个数 value:i
4. 取字典最大的key,同时取该key对应的最小的value
'''
import sys
def findFriend():
    line1 = sys.stdin.readline().split()
    line1 = list(map(int, line1))  # 第一行存到 line1 中，line[0]：第一行第一个数，line[1]:第一行第二个数
    arr = []  # 用arr[] 来保存输入的数组
    for i in range(line1[0]):
        line2 = sys.stdin.readline().split()
        line2 = list(map(int, line2))
        arr.append(line2)

    arr0 = arr[line1[1]]  # 给定用户的朋友列表
    arr1 = [i for i in range(line1[0])]  # 所有用户
    arr2 = [i for i in arr1 if i not in arr0]
    arr2.remove(line1[1])  # arr2 表示不是选定用户的朋友列表

    dict1 = {}  # key: 共同朋友的个数 value:用户编号
    for i in arr2:
        inter = [j for j in arr[i] if j in arr0]  # 取两个交集
        inter_len = len(inter)
        if inter_len in dict1.keys():
            dict1[inter_len].extend([i])
        else:
            dict1[inter_len] = [i]  # 这边的value 必须要写成list,这样后续才能extend()

    dict1_key = dict1.keys()
    if dict1_key:  # 如果有共同朋友
        print(min(dict1[max(dict1_key)]))  # 取最大的key对应的value,再对value取最小
    else:
        print(-1)


'''
字符串拆分
input:
123
output：
4
说明：[[1,23],[12,3],[1.2,3],[1,2.3]]
input:
00011
output：
2
说明：[[0.001,1],[0,0.011]
'''
'''
思路：
1.分割后的arr头尾不能同时是0
2.如果分割后的arr头部为0，则必须在第一个0后加小数点，仅1种
  如果分割后的arr尾部为0，则不能在任何位置加小数点，仅1种
3.分割后的arr非上诉情况，则小数点加在中间任意位置都可，有 len(arr)-1 种
'''

def judge(arr): # arr头尾同时是0，则返回0，否则返回1
    flag = 1
    if len(arr)>1:
        flag = int(arr[0]) | int(arr[-1])
    return flag

def coutJudge(arr):
    if arr[0] == '0':
        return 0
    elif arr[-1] == '0':
        return 0
    else:
        return len(arr)-1

def strSplit(): # main
    arr = sys.stdin.readline().strip()
    num = 0
    for i in range(len(arr)-1):
       arr1 = arr[:i+1]
       arr2 = arr[i+1:]
       if judge(arr1) & judge(arr2): # 分割后的两个数组都必须满足头尾不能同时是0
           num += 1
           num += coutJudge(arr1)
           num += coutJudge(arr2)
    print(num)

'''
顺时针输出字符串,并呈正方形
input:
abcdefghijklmnop
output:
abcde
p   f
o   g
n   h
mlkji

'''
import sys
if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    k = len(line) // 4
    line1 = line[0:k + 1]
    line2 = line[k + 1:2 * k]
    line3 = line[2 * k:3 * k + 1]
    line4 = line[3 * k + 1:]
    res = [[' '] * (k + 1) for i in range(k + 1)]
    for i in range(k + 1):
        res[0][i] = line1[i]
        res[k][i] = line3[k - i]
    for i in range(1, k):
        res[i][0] = line4[k - i - 1]
        res[i][k] = line2[i - 1]
    for i in res:
        print(''.join(i))