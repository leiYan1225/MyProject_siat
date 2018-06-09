'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.

输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = 0
        while (y or x):
            if x%2 !=y%2:
                n = n+1
            y = y>>1
            x = x>>1
        return n


# class Solution: ## 另一种解法：按位异或，然后看出现多少个1
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         n = x ^ y
#         s = 0
#         while n:
#             s += n & 1
#             n >>= 1
#         return s
