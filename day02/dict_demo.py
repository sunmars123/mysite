#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/6/25 21:12 
# @Author : Mars
# @Site :  
# @File : dict_demo.py 
# @Software: PyCharm
# 字典的学习
# 创建字典
# 推荐创建的方法
# dic = {1: 2, 3: 4}
# # 类实例的创建方法
# dic2 = dict((("name", "mars"),))
# print(dic)
# print(dic2)
# 字典的特性（字典是无序的，字典的键必须是不可更改的类型）
dic = {(123, 456): 1, "name": "mars"}
print(dic)
print(dic["name"])
