'''
数组中重复的数字
- 里面所有数字都在0-(n-1)的范围内
'''

## one method   Time complexity:O(n),Space complexity:O(n)
# 需要利用哈希表来解决，所以Space complexity = O(n) ？？
# arr1 = [2,3,1,0,2,5,5,3,2,3]
# arr2 = []
# for i in range(len(arr1),1):
#     # a = arr1[i]
#     arr1.pop(i)
#     print(arr1)
#     # if a in arr1:
#     #     arr2.append(a)
# print(arr1)

## another method，Time complexity:O(n),Space complexity:O(1)
# -- 思路：由于数字都是在0-(n-1)的范围内(关键！)，所以对应下标值i应该与元素值m相等。
# 分两步：若m与i不相等，判断下标为m的元素值是否为m
# --如果不为m,则将下标i和下标m 的元素值进行交换,以确保m在正确的位置上，重复判断。
# --如果为m,则表示找到一个重复的元素

arr1 = [2,3,1,0,2,5,5,3,2,3]
# arr1 = [0,2,5,6,8,7,1,4,3]
arr2 = []

def duplicate(arr):
    if max(arr)>=len(arr) or len(arr)==0:
        return False

    for i, m in enumerate(arr1):  # 类似字典结构
        if i != m:
            if arr1[m] != m:
                b = arr1[i]
                arr1[i] = arr1[m]
                arr1[m] = b
            else:
                arr2.append(m)

    print(set(arr2))

duplicate(arr1)