# coding=gbk
# @file:02-module_导入.py
# @data:2021/7/11 9:50
# Editor:clown
# 使用前必须要导入模块
import random
import os
#方法一： import 模块名
import test_module
print(test_module.num)  #函数中的变量调用
test_module.func()  #模块中的函数调用
dog=test_module.Dog  #函数中的类调用
dog.show_info()

# 方法二 from 模块名  import 功能名1,功能名2.....
#使用功能名
# 注意点：如果存在同用的方法名，则会被覆盖
# from test_module1 import func,num
# from test_module import num
# func()
# print(num)

'''
方法三： from 模块名  import * 使用模块中所有的功能进行导入
使用功能名
'''
from test_module import *
print(num)
func()
dog=Dog()
dog.show_info()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# as  起别名，可以对模块和功能起别名
# 注意 如果使用as别名 将不能再使用原来的名字
import test_module as nnnn
nnnn.func()
print("*"*30)
# 想要使用模块中的类容，必须现代如模块
# 注意点：如果导入的是自己书写的模块
# 使用的模块和代码文件需要在一个目录中
#嵌套的目录里面：Mark directory as  之后点击 sources boot

import test_module_01
print(num)
