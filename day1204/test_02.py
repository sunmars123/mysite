#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/5 22:34 
# @Author : mars 
# @Site :  
# @File : test_02.py 
# @Software: PyCharm
"""
可变集合：set，由不同元素组成的一组序列
不可变集合：frozenset
特点：
1.无序
2.去重
3.元素必须可哈希，即不可变类型
集合类型操作符
1.in与not in
2.集合等价与不等价（== , !=）
3.关系测试
    交集 intersection() ---> s1 & s2
    并集 union()  --->  s1 | s2
    差集 difference()定义内容为s1里面有的，s2没有的 ---> s1 - s2
    对称差集 symmetric_difference()  ---> s1 ^ s2
    父集 issuperset() s1是否包含s2
    子集  issubset（） s1是否被s2包含
"""
# 定义set
# 格式如下
# str = set("hello,world")
# print(str)  # {'w', 'h', 'o', 'r', ',', 'd', 'e', 'l'}
# str = set(["hello", "world"])
# print(str)  # {'hello', 'world'}
# str.add("my")  # 添加元素
# str.update("my")  # 根据类型添加元素，与创建集合类似
# str.remove("my")  # 移除删除一个元素
# str.pop()  # 随机删除一个元素并返回删除的元素
# str.clear()  # 清空集合
# del str  # 删除集合
s1 = set([1, 2, 4, 5])
s2 = set([3, 4])
print(s1.intersection(s2))  # 交集
print(s1.union(s2))  # 并集
print(s1.difference(s2))  # 差集
print(s1.symmetric_difference(s2))  # 对称差集
print(s1.issuperset(s2))  # 父集
print(s1.issubset(s2))  # 子集
