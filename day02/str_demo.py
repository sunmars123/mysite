#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/6/25 22:32 
# @Author : Mars
# @Site :  
# @File : str_demo.py 
# @Software: PyCharm
# String 操作
# 单引号和双引号的区别(单引号不支持字符串内包含引号，双引号支持字符串内包含单引号)
a = "let's go"
# print(a)
# 重复输出字符串
# print(a * 2)
# 切片理论
# print(a[1:])
# print(a[:])
# in的判断
# print(" " in a)
# 格式化字符串
# print("i speak %s" % a)
# 字符串的拼接
# a = "123"
# b = "456"
# +拼接，特别耗内存不建议使用
# c = a+b
# print(c)
# join拼接(调用join方法的对象为拼接的字符)
# c = "".join([a, b])
# print(c)
# string的内置方法
a = "hello123，"
print(a.count("h", 0, -1)) #统计元素个数，可以设置开始索引和结束索引，也可以不设置
print(a.capitalize()) #首字母大写
print(a.center(50, "-")) #居中显示，不足补‘-’
print(a.endswith("d")) #判断是否以某个元素结尾
print(a.startswith("hell")) #判断是否以某个元素开始
print(a.expandtabs(tabsize=10))
print(a.find("ll")) #查找到第一个元素，并将索引值返回
print(a.format(name='mars')) #格式化输出
print("{name} is my dear".format(name='yangyang'))
print("{name} is my {what}".format_map({"name": "yangyang", "what": "dear"}))
print(a.index("l")) #通过find查找时，没有查找到元素不会报错，通过index查找没有的话会报错
print(a.isalnum()) #判断字符串是否只包含字母和数字
print("100.9".isdecimal()) #判断字符串是否是一个十进制的数
print("123".isdigit()) #判断字符串是否是一个整型
print("123".isnumeric()) #判断字符串是否是一个整型
print("123qwe".isidentifier()) #判断是否非法变量
print("Abc".islower()) #判断是否全部小写
print("ABC".isupper()) #判断是否全部大写
print(" ".isspace()) #判断是否是一个空格
print("Abc".istitle()) #判断字符串是否是一个标题，即首字母大写
print("Abc".lower()) #将字符串大写变小写
print("abc".upper()) #将字符串小写的变大写
print("Abc".swapcase()) #将字符创的大小写反转
print("hello".ljust(50, '*')) #向左对其
print("hello".rjust(50, '*')) #向右对其
print("   hello world!".strip()) #将左右空格以及换行符去掉
print("   hello world!".lstrip()) #将左空格以及换行符去掉
print("   hello world!".rstrip()) #将右空格以及换行符去掉
print("hello,world".replace("world", "yangyang")) #替换字符串，可加上第三个参数控制替换的数量
print("I'm is chentao".split(" ")) #将字符串以某个元素分割为列表，也可将list通过join函数拼接成字符串
print("I'm is chentao".rsplit(" ")) #将字符串从右往左以某个元素分割为列表，也可将list通过join函数拼接成字符串
print("i'm is chentao".title()) #将字符串转化为title格式