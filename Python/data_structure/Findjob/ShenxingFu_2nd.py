# import sys
#
#
# def quick_sort(array):
#     def recursive(begin, end):
#         if begin > end:
#             return
#         l, r = begin, end
#         pivot = array[l]
#         while l < r:
#             while l < r and array[r] > pivot:
#                 r -= 1
#             while l < r and array[l] <= pivot:
#                 l += 1
#             array[l], array[r] = array[r], array[l]
#         array[l], array[begin] = pivot, array[l]
#         recursive(begin, l - 1)
#         recursive(r + 1, end)
#
#     recursive(0, len(array) - 1)
#     return array
#
#
# if __name__ == '__main__':
#     line = sys.stdin.readline().split()
#     line = list(map(int, line))
#     line1 = sys.stdin.readline().split()
#     line1 = list(map(int, line1))
#
#     n = line.pop(0)
#     list1 = [i for i in line]
#     list1 = quick_sort(list1)
#     print(str(list1[n // 2]))
#     m = line1.pop(0)
#     list2 = [i for i in line1]
#     list1.extend(list2)
#     list3 = quick_sort(list1)
#     print(str(list3[(n + m) // 2]))



x = [1, 2, 3, 4, 5, 6, 7]
y = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]

"""完成拟合曲线参数计算"""


def liner_fitting(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    average_x = 0
    average_y = 0
    while i < size:
        sum_xy += data_x[i] * data_y[i]
        sum_y += data_y[i]
        sum_x += data_x[i]
        sum_sqare_x += data_x[i] * data_x[i]
        i += 1
    average_x = sum_x / size
    average_y = sum_y / size
    return_k = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
    return_b = average_y - average_x * return_k
    return [return_k, return_b]

import numpy as np
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)