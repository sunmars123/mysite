#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 15:10 
# @Author : mars 
# @Site :  
# @File : 类的私有属性.py 
# @Software: PyCharm
class people:
    name = ""
    age = 0
    __salary = 0
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
    def prin_info(self):
        print(self.name, self.age, self.__salary)
    def __print_info(self):
        print("{0} age".format(self.name, self.age, self.__salary))
p1 = people("zero", 10, 50)
p1.prin_info()
print(p1.name)