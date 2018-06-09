'''
初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到原来的位置。
移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有 R（右），L（左），U（上）和 D（下）。输出应为 true 或 false，表示机器人移动路线是否成圈。

输入: "UD"
输出: true

输入: "LL"
输出: false
'''


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        def strNum(s,str1):
        # python中有内置函数可以代替
        # 即 str1.count("U")
            n = 0
            for i in str1:
                if i == s:
                    n +=1
            return n
        flag1 = 0
        flag2 = 0
        if strNum("U",moves) ==strNum("D",moves):
            flag1 = 1
        if strNum("L",moves) ==strNum("R",moves):
            flag2 = 1
        if flag1 and flag2:
            return True
        else:
            return False

obj = Solution()
print(obj.judgeCircle("UDDU"))