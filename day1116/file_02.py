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
seek()设置游标位置，未设置开始位置时，从0开始
游标说明：英文字符占1个游标，中文字符UTP-8占3个游标，换行符占2个游标
"""
# tell方法学习
# f = open("test.txt", "r", encoding="UTF-8")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()
# f = open("test02.txt", "r", encoding="UTF-8")
# print(f.tell())
# print(f.read(1))
# print(f.tell())
# f.close()
# seek方法学习
f = open("test03.txt", "w+")
f.write("hello,word")
print(f.tell())
f.seek(0)
print(f.read())
f.close()
