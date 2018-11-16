#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/16 11:19 
# @Author : Aries 
# @Site :  
# @File : file_03.py 
# @Software: PyCharm
"""
file类学习
"""
# 创建文件对象
import time

f = open("test04.txt", "a+")
# flush方法:在操作未关闭或者程序未关闭时，写入的内容暂时存储在内存中，可以通过flush刷新缓存区域
# while True:
#     f.write("hello,world\n")
#     f.flush()
#     time.sleep(0.5)
# f.close()
# fileno方法：返回一个整型的文件描述符
print(f.readline())
print(f.tell())
f.write("my name is ")
print(f.tell())
f.close()