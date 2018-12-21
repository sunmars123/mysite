#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/12 23:29 
# @Author : mars 
# @Site :  
# @File : 函数.py 
# @Software: PyCharm
import time
def logger():
    time_format = "%Y-%d-%m %X"
    now = time.strftime(time_format)
    with open("saas.log","a") as f:
        f.write("%s\n" % now)
def add(a, b):
    print(a+b)
    logger()
def sub(a, b):
    print(a-b)
    logger()
add(1, 3)
sub(10, 5)
