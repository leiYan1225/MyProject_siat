
## 二分查找
## 前提arr是排好序的数组

# 从arr中找到val对应的下标

def bs(arr,val):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (right+left)//2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            right = mid - 1
        else:
            left = mid+1
    return -1  # 如果没找到，返回-1
# arr = [1,2,3,4,6,7,8,9]
# print(bs(arr,4))

# 变种1：在arr中找到第一个大于等于val的值
def bs1(arr,val):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (right+left)//2
        if arr[mid]>=val:   # 如果题目是大于，这里也改成大于
            right = mid-1
        else:
            left = mid+1
    return arr[left]        ## 注意是left
arr = [1,2,3,4,6,7,8,9,10]
print(bs1(arr,5))

# 变种2：在arr中找到最后一个小于val的值
def bs1(arr,val):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (right+left)//2
        if arr[mid] < val:  # 如果题目是小于等于，这里也改成小于等于
            left = mid + 1
        else:
            right = mid - 1
    return arr[right]   ## 注意是right
# arr = [1,2,3,5,6,7,8,9,10]
# print(bs1(arr,7))
