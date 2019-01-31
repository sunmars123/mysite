#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/18 16:12 
# @Author : mars 
# @Site :  
# @File : 日期与时间.py 
# @Software: PyCharm
# time（）当前时间戳
import time
# for i in range(1, 9):
#     print(time.time())
#     time.sleep(1)
# 本地时间
print(time.localtime())
# 格式化时间
print(time.asctime(time.localtime()))
# 自定义格式时间
print(time.strftime("%Y-%m-%d %H:%M:%m", time.localtime()))