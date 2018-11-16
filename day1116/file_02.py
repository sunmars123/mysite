#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/16 9:10 
# @Author : Aries 
# @Site :  
# @File : file_02.py 
# @Software: PyCharm
"""
文件方法学习：
tell()获取当前游标
游标说明：英文字符占1个游标，中文字符UTP-8占3个游标，换行符占2个游标
"""
f = open("test.txt", "r", encoding="UTF-8")
print(f.tell())
print(f.readline())
print(f.tell())
f.close()
# f = open("test02.txt", "r", encoding="UTF-8")
# print(f.tell())
# print(f.read(1))
# print(f.tell())
# f.close()
