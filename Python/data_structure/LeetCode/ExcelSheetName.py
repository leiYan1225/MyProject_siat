'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

输入: 1
输出: "A"

输入: 701
输出: "ZY"
'''


class Solution(object):
    def convertToTitle(self, n):
        result, dvd = "", n

        while dvd:
            result += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) // 26

        return result[::-1]