#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/18 20:26 
# @Author : mars 
# @Site :  
# @File : file_work.py 
# @Software: PyCharm
"""
展示一个三级菜单
1.将三级菜单内容存储到文件中
2.可以对菜单进行增删改查操作
涉及的方法：eval,with
"""
# #字符串转字典
# str = "{'湖南': [{'永州': ['祁阳', '祁东', '冷水滩']},{'长沙': ['长沙县', '浏阳县']}],'上海': [{'浦东新区':['张江', '浦东国际机场']}]}"
# dic = eval(str)
# print(dic)
with open("work", "r", encoding="UTF-8") as f:
    str = f.readline()
    dic = eval(str)
    # print(dic["欧美"])
    print("城市列表如下：")
    for x,y in enumerate(dic, 1):
        print(x, '>>>', y)
    city = input("请输入查询省份名称[退出：q]：")
    if city != 'q':
        if city in dic:
            city_list = dic[city]
            for x,y in enumerate(city_list, 1):
                print(x, '>>>', y)
            country = input("请输入查询城市名称[退出：q]：")
            if country in dic[city]:
                country_list = dic[city][country]
                for x,y in enumerate(country_list, 1):
                    print(x, '>>>', y)
            else:
                print("你输入的省份不存在！！")
        else:
            print("你输入的城市不存在!")
    else:
        print("程序退出！")

