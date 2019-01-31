#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 15:33 
# @Author : mars 
# @Site :  
# @File : test.py 
# @Software: PyCharm
# os模块提供了不少与操作系统相关联的函数
# import os
# # 获取当前工作路径
# print(os.getcwd())
# print(dir(os))
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob
# 匹配当前所在目录下python文件
print(glob.glob("*.py"))