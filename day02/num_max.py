#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/5/31 21:56 
# @Author : Mars
# @Site :  
# @File : num_max.py 
# @Software: PyCharm
# x = input("num1>>")
# y = input("num1>>")
# # z = input("num1>>")
# v = 0
"""
求最大值
"""


def max_num(x, y, z):
    if x > y:
        if x > z:
            print("{0}".format(x))
        else:
            print("{0}".format(z))
    else:
        if y > z:
            print("{0}".format(y))
        else:
            print("{0}".format(z))


"""
求最小值
"""


def min(x, y, z):
    if x < y:
        if x > z:
            print("{0}".format(z))
        else:
            print("{0}".format(x))
    else:
        if y > z:
            print("{0}".format(z))
        else:
            print("{0}".format(y))


x = 9
y = 1

"""
输出长方形
"""


def medo(x, y):
    while x > 0:
        while y > 0:
            print("#", end='')
            y -= 1
        print("")
        y = 4
        x -= 1


"""
输出九九乘法表
"""


def demo():
    for x in range(1, 10):
        for y in range(1, x + 1):
            print("{0}*{1}={2} ".format(x, y, x * y), end="")
        print("")


demo()
