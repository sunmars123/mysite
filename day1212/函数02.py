#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/20 21:57 
# @Author : mars 
# @Site :  
# @File : 函数02.py 
# @Software: PyCharm
"""
    1.默认参数
        def function(age=10):
            pass
    注：默认参数需要放在常规参数后面
    2.不定长无命名参数*args
        def function(*args):
            pass
    3.不定长命名参数**kwargs
        def function(kwargs):
            pass
    4.混合使用
        def function(*args, **kwargs):
            pass
    注意事项：传参时需要根据形参的类型传参，且命令参数**kwargs必须放在*args后面
    5.默认参数
        def function(a, b = 10):
            print (a + b)
    备注：传值时使用传入的值，未传值时使用默认值
    6.return返回
        def function(a, b)
            return a + b
    备注：方法执行后返回一个数据，并在return后退出
"""


# 默认不传y时，传入10
# def add(x, y=10):
#     print(x + y)
#
#
# add(1)
# 不定长加法器
def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print("和为：%d" % sum)


add(1, 3, 6, 8)


def print_info(**kwargs):
    print(kwargs)
    for i in kwargs:
        print("%s:%s" % (i, kwargs[i]))


print_info(name="zhangsan", age=17, hex="男")
