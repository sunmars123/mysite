#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 15:06 
# @Author : mars 
# @Site :  
# @File : 方法重写.py 
# @Software: PyCharm
class people:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("my name is {0},I age have {1}".format(self.name, self.age))


people1 = people("zero", 20)
people2 = people("mars", 30)
people1.print_info()
people2.print_info()


class student(people):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


s1 = student("mars", 10)
s1.print_info()
# 重写后调用父类方法
super(student, s1).print_info()
