#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

def solve(S, T):
    def func(s, t):
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for s1, t1 in zip(s, t):
            if s1 in dic1 and dic1[s1] != t1:
                return False
            else:
                dic1[s1] = t1

        for s1, t1 in zip(s, t):
            if t1 in dic2 and dic2[t1] != s1:
                return False
            else:
                dic2[t1] = s1
        return True

    s_len = len(S)
    t_len = len(T)
    num = 0
    for i in range(s_len):
        if func(S[i:i + t_len], T):
            num += 1
    return num


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")




def solve(S, T):
    def func(s, t):
        if len(s) != len(t):
            return False
        dic1,dic2 = {},{}
        for s1, t1 in zip(s, t):
            if s1 in dic1 and dic1[s1] != t1:
                return False
            else:
                dic1[s1] = t1

        for s1, t1 in zip(s, t):
            if t1 in dic2 and dic2[t1] != s1:
                return False
            else:
                dic2[t1] = s1
        return True
    s_len = len(S)
    t_len = len(T)
    num = 0
    for i in range(s_len-t_len):
        if func(S[i:i + t_len], T):
            num += 1
    return num


# s = "paper"
# t = "title"
s = 'ababcb'
t = 'xyx'
print(solve(s,t))

