#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/16 9:00 
# @Author : Aries 
# @Site :  
# @File : file_01.py 
# @Software: PyCharm
"""
文件读取
"""
# 读取全部
# f = open("test.txt", "r", encoding="UTF-8")
# print(f.read())
# f.close()
# 按行读取-readLines,注：通过readLines读取读取消耗资源
# f = open("test.txt", "r", encoding="UTF-8")
# data = f.readlines()
# for i in data:
#     print(i, end="")
# f.close
# 通过迭代器获取
# f = open("test.txt", "r", encoding="UTF-8")
# for i in f:
#     print(i, end="")
# f.close()
# 实例：在文件第六行添加末尾，查看时添加hello，word
f = open("test.txt", "r", encoding="UTF-8")
num = 1
for i in f:
    if num == 6:
        i = "".join([i.strip(), "hello,word"])
    print(i.strip())
    num = num+1
f.close()
