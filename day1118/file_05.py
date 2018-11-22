#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/18 19:07 
# @Author : Aries 
# @Site :  
# @File : file_05.py 
# @Software: PyCharm
"""
修改文件在第六行最后增加zero
"""
# 方案一
# f1 = open("test03.txt", "r", encoding="UTF-8")
# data = f1.readlines()
# f1.close()
# num = 0
# for i in data:
#     if num == 5:
#             data[num] = "".join([i.strip(), "zero", "\n"])
#     num += 1
# f2 = open("test03.txt", "w", encoding="UTF-8")
# f2.writelines(data)
# f2.close()
# 方案二
f1 = open("test03.txt", "r", encoding="UTF-8")
f2 = open("test04.txt", "w", encoding="UTF-8")
num = 1
for line in f1:
    if num == 6:
        line = "".join([line.strip(), "zero", "\n"])
    num += 1
    f2.write(line)

