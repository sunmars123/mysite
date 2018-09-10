#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/10 23:53 
# @Author : Aries 
# @Site :  
# @File : file_demo.py 
# @Software: PyCharm
# 创建一个file对象，open参数可填写绝对路径和相对路径，相对路径与当前脚本目录一致
f = open("File.txt", "r", encoding="UTF-8")
str = f.read()
print(str)
f.close()
