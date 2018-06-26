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
# dic = {(123, 456): 1, "name": "mars"}
# print(dic)
# print(dic["name"])
# 字典的函数
dic = {"name1": "zambian", "name2": "mars", "name3": "join"}
# 增加
dic["name4"] = "Janean"
# print(dic)
# 删除（pop,popitem,clear,del）
# x = dic.pop("name2")
# y = dic.popitem()
# dic.clear()
# del dic["name1"]
# del dic
# print(dic)
# print(x)
# print(y)
# 更改(update)
# dic["name4"] = "alic"
# dic2 = {"name1": 1}
# dic.update(dic2)
# print(dic)
# 查询（get,迭代器遍历items,keys键遍历值）
# print(dic.get("name1"))
# for x, y in dic.items():
#     print(x, y)
# for x in dic.keys():
#     print(x, dic[x])
# # 推荐使用
# for x in dic:
#     print(x, dic[x])
# 设置默认值,若键已存在值不更改值，若键不存在值则赋予默认
# dic.setdefault("name1", "2")
# print(dic)
# 格式化创建format,对列表的值进行初始化,当初始化的数据是列表是存在深浅拷贝
# dic2 = dict.fromkeys(["name1", "name2", "name3"], ["mars", "root"])
# print(dic2)
# dic2["name1"] = "root"
# print(dic2)
# 字典的嵌套
dic ={
    "欧美": {
        "www.baidu.com": ["百度", "度娘"]
    },
    "日韩": {
        "www.taobao.com": ["淘宝", "网上商城"]
    }
}
# 获取www.taobao.com的跌名
print(dic["日韩"]["www.taobao.com"])
# 更改www.taobao.com的跌名
dic["日韩"]["www.taobao.com"][0] = "京东"
print(dic)
# 字典的排序
dic2 = {5: "555", 4: "444", 1: "111"}
print(sorted(dic2.items()))