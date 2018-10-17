'''
一种改进的字符串匹配算法，时间复杂度O(n+m)
传统思维：从目标串Target的第一个字符开始扫描，逐一与模式串的对应字符进行匹配，若该组字符匹配，则检测下一组字符，如遇失配，
则退回到Target的第二个字符，重复上述步骤，直到整个Pattern在Target中找到匹配，或者已经扫描完整个目标串也没能够完成匹配为止，算法复杂度O(N^2)

'''

# 传统方法
def naive_match(s,p):
    m = len(s)
    n = len(p)
    for i in range(m-n+1):
        if s[i:i+n] == p:
            return True
    return False




# 求匹配字符串的部分匹配表(PMT)
# -creat by will
def PMT(arr):
    m_len = []
    for i in range(len(arr)):
        pre = []
        suf =[]
        arr1 = arr[0:i+1]
        for j in range(len(arr1)-1):
            pre.append(arr1[0:j+1])
            suf.append(arr1[j+1:])
        ret_list = list(set(pre).intersection(set(suf))) # 求交集
        tmp = list(map(lambda x: len(x), ret_list))
        if tmp: # 判断tmp 是否为空
            pass
        else:
            tmp.append(0)
        m_len.append(max(tmp))
    return m_len

#基本版
# 失配时，模式串向右移动的位数为：已匹配字符数 - 失配字符的上一位字符所对应的最大长度值

def kmpMatch(s,p):
    table = PMT(p)
    m = len(s)
    n = len(p)
    cur = 0
    while cur<=m-n:
        # if s[cur]!=p[cur]:
        #     cur+=1
        #     continue # 结束当次循环
        for i in range(n): # 按字符依次匹配模式串
            if p[i] != s[cur+i]:
                cur += max(i - table[i - 1], 1)  # 这边取max(,1)就包含了if 的情况,i 这边刚好等于已匹配的字符数
                break # 跳出整个for 循环
            else:
                return True
    return False

# 优化版
def kmpMatchPro(s,p):
    print()

a = "BBC ABCDAB ABCDABCDABD"
b = "ABCDABD"
# print(naive_match(a,b))
kmpMatch(a,b)

print(PMT('ababcabcacbab'))



