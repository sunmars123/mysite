#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 14:08 
# @Author : mars 
# @Site :  
# @File : 类学习.py 
# @Software: PyCharm
class Employee:
    '所有员工的基类'
    num = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num += 1

    def print_info(self):
        print("name is {0},salary is {1},num is {2}".format(self.name, self.salary, Employee.num))


emp1 = Employee("Zara", 2000)
emp2 = Employee("lead", 2000)
emp1.print_info()
emp2.print_info()
