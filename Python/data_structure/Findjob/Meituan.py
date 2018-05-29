
'''
美团笔试，求字符串距离
规定 abab 与 bbaa 两者对应位置有两处字符不同，故表示两字符串距离为2.
规定 A的长度大于等于B的长度，A中能拆分出 len(A)-len(B)+1 个与B长度相等的子串
示例： A = ['a','a','a','b','b','a']  B = ['b','a','b']  num=5
'''
def strDis(a,b):
    a_len = len(a)
    b_len = len(b)
    num = 0
    for i in range(a_len-b_len+1): # 遍历a中每个与b长度相等的子串
        c = a[i:i + b_len]      # 存入c中
        for j in range(b_len):   # 遍历b
            if c[j] != b[j]:    # 判断列表中有元素不等则num加一
                num += 1
    return num

a = input("Please input array A:")
b = input("Please input array B:")
a_list = list(a)
b_list = list(b)
print(strDis(a_list,b_list))

'''
美团笔试，求由给定数字不能组成的最小正整数
例如只给定两个1，一个2，能组成正整数11，112等，但不能组成22。 112这组数字不能组成的最小正整数就是3

分两种情况讨论：如果0~9缺失数字，则缺失的数字中最小的非0数即为所求
如果0~9不缺数字，则先找到出现次数n最小且最小的非0数a，则(n+1)个a 即为所求。若出现次数最少的为0，则所求为 1(0的次数+1)
示例：001123344567789 出现次数最少且最小的非0数为：2  则不能组成的最小正整数为22
'''
def minInt(a): # a:输入列表
    b = list(range(10))
    # 可求得两个集合的差集，即在b 不在 a 的
    c = [item for item in b if item not in a]
    # d = list(set(a)^set(b))  求差集的高级方法
    result = 0  # 所求结果

    if len(c) != 0:  # 0~9有数字缺失的情况
        result = min(c)
        if result == 0:
            result = min(a) * 10
        return result
    else:           # 0~9无数字缺失的情况
        num_dic = {}  # 定义一个dict, key：数字0~9，value：某数字出现的次数
        list_key = []  # 用来存储次数最少的那些key值
        min_num = 0  # 最少的次数
        min_key = 0  # 存储list_key最小的值

        for i in a:  # 找出出现次数大于等于1的值，并存入字典
            if a.count(i) >= 1:
                num_dic[i] = a.count(i)
        min_val = min(num_dic.values())  # 找出最小的次数

        for key, value in num_dic.items():  # 遍历字典
            if value == min_val:
                list_key.append(key)  # 将key 存入数组中
        min_key = min(list_key)  # 找出最小的次数中对应的最小key
        if min_key == 0:
            result = 10 ** (min_val + 1)  #最小key为0时，所求即在前面加个1，为 100...
        else:
            for i in range(min_val + 1):
                result += min_key * 10 ** (i)  #最小key不为0时

        return result

a_list =list(input("Please input string A:"))
a = list(map(int,a_list))  # 将a_list 中的每个元素由 str 转换成 int，再加上list操作 将map 转换成list
print(minInt(a))