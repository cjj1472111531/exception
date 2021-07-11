# coding=gbk
# @file:04-__name__变量.py
# @data:2021/7/11 11:02
# Editor:clown

# 自己定义的模块名字 不要跟系统中使用的模块名字相同
# 所以 当有与系统名字一样的话  就是先使用自己有的

#模块的搜索目录：当前目录-》系统目录-》程序报错
import sys
import os
import  random
print(sys.path)
z=os.getcwd()
print(z)

a=random.randint(1,5)
print(a)