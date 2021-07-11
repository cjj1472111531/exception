# coding=gbk
# @file:03-__all__变量.py
# @data:2021/7/11 10:37
# Editor:clown
'''
__all__ 变量，可以在每个代码文件中（模块中）定义,类型是元组和列表
作用：影响 from 模块名 import * 导入行为
1.如果没有定义__all__变量，模块中的所有功能，都可以被导入
2.如果定义__all__变量  只能导入 变量中定义的内容
'''
from test_module3 import *
print(num)
func()
dog1=Dog() #会报错
dog1.show_info()



