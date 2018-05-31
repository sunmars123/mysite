#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/5/31 16:32
# @Author : Mars
# @Site :  
# @File : check_admin_file2.py
# @Software: PyCharm

# f = open("admin.txt")
# 写文件
# f.write("admin")
# f.closed()
# 读文件
# s = f.read()
# print(type(s),s)

"""
    需求：有一个原始的账号，现在对输入数据账号进行判断如果存在输入错误三次就锁定账号，锁定账号提示
    思路：基础数据（原有 需要定义），判断是否锁定，判断是否正确，判断错误是否达到三次
"""
admin = 'root'
pwd = '123456'
count = 1
box = ""

# with open("admin.txt", "r") as f:
#     input_admin = input("请输入用户名：")
#     input_pwd = input("请输入密码：")
#     for line in f.readlines():
#         if admin == line:
#             print("该用户已锁定")
#         else:
#             while count > 3:
#                 if input_admin == admin and input_pwd == pwd:
#                     print("校验成功")
#                 else:
#                     count += 1
def is_sockt(is_lock_user: object) -> object:
    with open("admin.txt", "r") as lock_user:
        for line in lock_user.readlines():
            if line == is_lock_user:
                return False
        return True


'''
    对一个用户连续三次输入密码错误后锁定
'''
input_admin = input("请输入用户名：")
if is_sockt(input_admin):
    input_pwd = input("请输入密码：")
    while True:
        if count < 3:
            if input_admin == admin and input_pwd == pwd:
                print("欢迎{}使用系统".format(input_admin))
                continue
            else:
                print("密码错误")
                if count == 1:
                    box = input_admin
                    count += 1
                    input_admin = input("请重新输入用户名：")
                    input_pwd = input("请重新输入密码：")
                else:
                    if box == input_admin:
                        count += 1
                        input_admin = input("请重新输入用户名：")
                        input_pwd = input("请重新输入密码：")
                    else:
                        box = input_admin
                        count = 1
                        input_admin = input("请重新输入用户名：")
                        input_pwd = input("请重新输入密码：")
        elif count == 1:
            box = input_admin
            count += 1
        else:
            f = open("admin.txt", "a")
            f.write("\n{0}".format(input_admin))
            f.close()
            print("密码错误已达三次，用户 {0} 将被锁定".format(input_admin))
            break
else:
    print("{0}已被锁定".format(input_admin))
