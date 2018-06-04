#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/6/1 20:44 
# @Author : Mars
# @Site :  
# @File : data_type.py
# @Software: PyCharm
# 字符串str的方法
name = input("Name:")
age = input("Age:")
# isdigit函数，判断字符串都是由数字组成
if age.isdigit():
    print("{0} is a num".format(age))
else:
    print("{0} is not num".format(age))
