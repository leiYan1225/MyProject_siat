# 满足条件：全局最优即局部最优

## 剪绳子问题
'''
题目：
一根长度为n的绳子，将绳子剪为m段（剪m-1次），每段绳子的长度为k[0] ~ k[m]；要求k[0] * k[1] * k[2] * ~~k[m]的乘积为最大。n >1 且 m> 1

分析：
只需要满足至少切一刀就好，切成几段由面积最大决定。
第一刀下去后，绳子分成两部分，假设在i处下刀，绳子两部分就分别为：[0~i]与[i~n]，长度分为表示为i与n-i；那么找出第一刀最合适的位置，
其实就是找i在哪下刀，可以使得[0~i]与[i~n]的乘积最大，函数表示为：f(n) = max(f(i) * f{n-i))

'''
def jianshengzi(n):
    # 先对边界问题进行求解，因为明显剪的值小于不剪的值
    # 则提出先讨论这三种情况
    if n < 2:
        return 0
    if n == 2:
        return 1    #长度为2，只能剪成1*1
    if n == 3:
        return 2    #长度为3，剪成2*1 > 1*1*1

    # 大于3的绳子，剪开可能比本身大，或至少等于本身，3是一个底线
    # 定义h[1],h[2]是因为不可能绳子程度都是三的倍数，一定会需要1和2来保证相加起来等于绳子的长度
    h = [0]*50  # 定义一个数组用来存中间值
    h[0] = 0
    h[1] = 1
    h[2] = 2
    h[3] = 3
    # 递归问题是 f(n) = max{f(i)*f(n-i)}
    for i in range(4,n+1):
        maxs = 0
        for j in range(1,i//2+1):
            mult = h[j] * h[i-j]
            maxs = max(maxs,mult)
        h[i] = maxs     # 每次J的迭代轮询出该长度的最大值
    print(h)
    return h[n]

# print(jianshengzi(8))

## 走楼梯
'''
问题：
一个人每次只能走一层楼梯或者两层楼梯，问走到第80层楼梯一共有多少种方法。
分析：
走到第i层楼梯，可以从i-1层走一层，或者从i-2走两层
递推公式：DP[i]=DP[i-1]+DP[i-2]
'''
def DP(n):
    dp = [0] * 81
    dp[1] = 1
    dp[2] = 1
    for i in range(3,len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp

# print(DP(81))

## 拼凑钱币
'''
题目：
有面值为1元3元5元的硬币若干枚，如何用最少的硬币凑够11元？
分析：
最后一步可拿的硬币数为：1，3，5
状态转移方程：
f(n) = min(f(n-vi)+1)
'''
def leastCoins(n):
    coins = [1,3,5]
    dp = [0]*50
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1
    if n<6:
        return dp[n]
    for i in range(6,n+1): #从下往上的思维解决
        mins = n  ## 没什么意义，就是给定一个初始值
        for j in coins:
            mins = min(mins,dp[i-j]+1)
        dp[i] = mins
    return dp
# print(leastCoins(7))

'''
最长上升子序列
题目：
对于序列：4 1 2 2 4，它的最长上升子序列是 1 2 4，长度为3。
对于序列：4 2 4 2 5 6，它的最长上升子序列是 2 4 5 6，长度为4。

分析：
dp[i]表示以nums[i]为结尾的最长递增子串的长度，对于每一个nums[i]，我们从第一个数再搜索到i，如果发现某个数小于nums[i]，
我们更新dp[i]，更新方法为：
dp[i] = max(dp[i], dp[j] + 1)
即比较当前dp[i]的值和那个小于num[i]的数的dp值加1的大小
使用dp算法，O(n^2),不是很好。。
'''

# 得到dp数组
def lisDP(arr):
    dp = [1]*len(arr)
    for i in range(len(arr)):
        dp[i] = 1
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp
# 得到最长上升子序列
def generateLIS(arr, dp):
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]
    # 从右向左
    for i in range(index, 0 - 1, -1):
        # 关键
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            n -= 1
            lis[n] = arr[i]
            index = i
    return lis

arr = [4,1,2,2,4]
# print(max(lisDP(arr)))
# print(generateLIS(arr,lisDP(arr)))


'''
最长上升子序列
改进一下算法，O(nlogn)的复杂度
思路：
先建立一个数组ends，把首元素放进去，然后比较之后的元素，如果遍历到的新元素比ends数组中的首元素小的话，替换首元素为此新元素，
如果遍历到的新元素比ends数组中的末尾元素还大的话，将此新元素添加到ends数组末尾(注意不覆盖原末尾元素)。如果遍历到的新元素比ends数组首元素大，
比尾元素小时，此时用二分查找法找到第一个不小于此新元素的位置，覆盖掉位置的原来的数字，以此类推直至遍历完整个nums数组，
此时ends数组的长度就是我们要求的LIS的长度，特别注意的是ends数组的值可能不是一个真实的LIS,只是长度一致
'''
def lisDP2(arr):
    n = len(arr)
    ends = []
    ends.append(arr[0])
    for i in range(1,n):
        if arr[i] < ends[0]:
            ends[0] = arr[i]
        elif arr[i] > ends[-1]:
            ends.append(arr[i])
        else:  ## 比最后一位小，比第一位大，ends数组是一个增序数组，可以用二分查找来找到第一个大于等于arr[i]的值，然后替换
            left = 0
            right = n-1
            while left <= right:
                mid = (right + left)//2
                if ends[mid] >= arr[i]:
                    right = mid-1
                else:
                    left = mid+1
            ends[left] = arr[i]
    return ends

arr = [4,1,2,2,4]
# print(lisDP2(arr))  ## 还有点错误，待完善


