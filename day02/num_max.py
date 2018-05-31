#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/5/31 21:56 
# @Author : Mars
# @Site :  
# @File : num_max.py 
# @Software: PyCharm
x = input("num1>>")
y = input("num1>>")
z = input("num1>>")


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


min(x, y, z)
max(x, y, z)
