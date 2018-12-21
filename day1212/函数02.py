#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/20 21:57 
# @Author : mars 
# @Site :  
# @File : 函数02.py 
# @Software: PyCharm
"""
    1.默认参数
        def function(age=10):
            pass
    注：默认参数需要放在常规参数后面
    2.不定长参数*args
        def function(*args):
            pass
"""


# 默认不传y时，传入10
# def add(x, y=10):
#     print(x + y)
#
#
# add(1)
# 不定长加法器
def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print("和为：%d" % sum)
add(1, 3, 6, 8)