

# Refer to:https://www.cnblogs.com/eniac12/p/5329396.html


# 快速排序：
# 选取一个数据（比如数组最后一个数）作为基准数，然后将所有比它小的放在它前面，比他大的放在它后面
# def swap(arr, i, j):
#     z = arr[i]
#     arr[i] = arr[j]
#     arr[j] = z
# def Partition(arr, left, right):
#     pivot = arr[right]
#     tail = left-1
#     for i in range(left,right):
#         if arr[i] <= pivot:
#             swap(arr, ++tail,i)
#     swap(arr, tail+1, right)
#     return tail + 1
#
# def QuickSort(arr,left,right):
#     if(left >= right):
#         return
#     pivot_index = Partition(arr,left,right)
#     QuickSort(arr,left,pivot_index-1)
#     QuickSort(arr,pivot_index+1, right)
#
# QuickSort(numbers,0,n-1)
# print("快速排序的结果：")
# for i in range(n):
#     print(numbers[i])



# 一趟快速排序的算法是：
# 1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
# 2）以第一个数组元素作为基准数据，赋值给key，即key=A[0]；
# 3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
# 4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
# 5）重复第3、4步，直到i=j。
# def QuickSort(myList,start,end):
#     # 判断low是否小于high,如果为false,直接返回
#     if start < end:
#         i,j = start,end
#         # 设置基准数
#         base = myList[i]
#         while i < j:
#             # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1
#             # 如找到,则把第j个元素赋值给第i个元素,此时表中i,j元素相等
#             myList[i] = myList[j]
#             # 同样的方式比较前半区
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j] = myList[i]
#         # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
#         myList[i] = base
#
#         # 递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList
#
# numbers = [6,5,3,7,2,8,4]
# n = len(numbers)
# print("Quick Sort: ")
# QuickSort(numbers,0,n-1)
# print(numbers)

def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return


def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


arr = [1, 4, 7, 5, 3, 8, 2, 0]

print("initial array:\n", arr)
QuickSort(arr, 0, len(arr) - 1)
print("result array:\n", arr)