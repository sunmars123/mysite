#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/16 13:00 
# @Author : Aries 
# @Site :  
# @File : file_04.py 
# @Software: PyCharm
# f = open("test04.txt", "r+",encoding="UTF-8")
# num = 1
# for i in f:
#     if num == 6:
#         f.write("mysql")
#     num += 1
# f.close()
f2 = open("test05.txt", "w", encoding="UTF-8")
f2.writelines(["123\n", "456\n"])
f2.close()