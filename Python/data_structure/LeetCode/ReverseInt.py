'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21

'''




class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        intMax = 2147483648
        intMin = -2147483648
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        r = 0
        while (x > 0):
            r = r * 10 + x % 10
            x //= 10
        if flag:
            r = -r
        if (r > intMax or r < intMin):
            return 0
        return r