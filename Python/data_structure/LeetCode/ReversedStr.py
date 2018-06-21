'''
请编写一个函数，其功能是将输入的字符串反转过来。
输入：s = "hello"
返回："olleh"
'''

s = 'hello'

#1. 简单的步长为-1, 即字符串的翻转(常用);
def string_reverse1(string):
    return s[::-1]

#4. 双端队列, 使用extendleft()函数;
from collections import deque
def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)
print(string_reverse4(s))