
# '''
# # 两数之和
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
# '''
#
# class Solution:
#
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i, num in enumerate(nums):
#             sub_num = target - num
#             if sub_num in nums:   # 判断另一个是否在数组中
#                 t_index = nums.index(sub_num)
#                 if t_index != i:
#                     return [i, t_index]
#
#
# nums = [2,1,9,4,4,56,90,3]  # 8
# obj = Solution().twoSum(nums,8)
# print(obj)

'''
两数相加（使用链表实现）
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#
#         tmp = ListNode(0) # 初始化一个值为0的节点
#         res = tmp
#         flag = 0  # 进位标志
#         while l1 or l2:
#             tmpsum = 0
#             if l1:
#                 tmpsum = l1.val
#                 l1 = l1.next
#             if l2:
#                 tmpsum += l2.val
#                 l2 = l2.next
#             tmpres = ((tmpsum + flag) % 10)  # 取模（余）
#             flag = ((tmpsum + flag) // 10)   # // 符号表示向下取整
#             res.next = ListNode(tmpres)
#             res = res.next
#         if flag:
#             res.next = ListNode(1)
#         res = tmp.next
#         del tmp
#         return res


# 无重复字符的最长子串的长度
# 给定一个字符串，找到不含重复字符的最长子串，例如："abcabcbb"-"abc"

# s = "abcabcbb"
# s_list = list(s)
# max_len = 0
# if len(s_list) != 0:
#     max_len = 1
# for i in range(len(s_list)):
#     flag = 1
#     for j in range(i + 1, len(s_list)):
#         if s_list[j] == s_list[i] and flag == 1:
#             flag = 0
#             len1 = j -i
#             if len1 >= max_len:
#                 max_len = len1
#         elif s_list[j] != s_list[i] and flag ==1:
#             max_len = len(s_list)
#
# print(max_len) ### 未完待续


# 给定一个 32 位有符号整数，将整数中的数字进行反转
# 123：321、-123：-321、120：21

# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         intMax = 2147483648  # 定义上下界，避免溢出
#         intMin = -2147483648
#         flag = 0 # 定义一个负数标志数
#         if x < 0:
#             flag = 1
#             x = -x
#         r = 0
#         while (x > 0):
#             r = r * 10 + x % 10 #这两句实现正数反转：不断求余取每一位 以及乘10
#             x //= 10  #  向下取整
#         if flag:
#             r = -r
#         if (r > intMax or r < intMin):
#             return 0
#         return r

# 给定一个正整数，返回它在Excel表中相对应的列名称。
# 例如 1：A、28：AB、701：ZY
#
# class Solution(object):
#     def convertToTitle(self, n):
#         result, dvd = "", n
#
#         while dvd:
#             result += chr((dvd - 1) % 26 + ord('A'))
#             dvd = (dvd - 1) // 26
#
#         return result[::-1]

# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 例如 A：1
# class Solution(object):
#     def titleToNumber(self, s):
#         if not s:return None # 判断是否为空，经典写法
#
#         num = 0
#         for c in s:
#             num = ((num*26) + ord(c) -64)
#         return num
# # 或者
# def titleToNumber(self, s):
#     result = 0
#     for i in range(len(s)):
#         result *= 26
#         result += ord(s[i]) - ord('A') + 1
#     return result

nums = [1,1,2]
num1 = list(set(nums))
print(len(num1))



digits = ['1','2','3']
dig_str = ''.join(digits)
dig1 = int(dig_str)+1
print(dig_str)