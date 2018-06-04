'''
给定一个Excel表格中的列名称，返回其相应的列序号。

输入: "A"
输出: 1

输入: "AB"
输出: 28

输入: "ZY"
输出: 701
'''


class Solution(object):
    def titleToNumber(self, s):
        if not s: return None
        num = 0
        for c in s:
            num = ((num * 26) + ord(c) - 64)
        return num
