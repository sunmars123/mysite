#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/4 23:23 
# @Author : mars 
# @Site :  
# @File : test_01.py 
# @Software: PyCharm
"""
深浅拷贝
浅拷贝：copy,只复制第一层
深拷贝：deepcopy，全部复制
"""
import copy
# 浅拷贝
amount = ["17673637740", [10000, 5000]]
amoun_copy = amount.copy()
amoun_copy[1][0] -= 3000
print(amount)
print(amoun_copy)
# 深拷贝
amoun_deepcopy = copy.deepcopy(amount)
amoun_copy[1][0] += 2000
print(amount)
print(amoun_deepcopy)