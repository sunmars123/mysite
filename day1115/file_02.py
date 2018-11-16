#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/15 16:59 
# @Author : Aries 
# @Site :  
# @File : file_02.py 
# @Software: PyCharm
import time

f = open("test.txt", "a")
f.write("hello world")
time.sleep(10)
f.close()
