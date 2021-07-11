# coding=gbk
# @file:01-exception_fine.py
# @data:2021/7/10 20:10
# Editor:clown
# 异常：程序运行过程中 代码遇到错误 给出错误提示
# 异常捕获 ：是指程序代码运行打过程中，不然程序终止，让继续先进行
# 同时可以使用者提供一个提示信息
# 并记录这个错误，便于后期改进
'''
try:
   可能出现异常的代码
except(异常类型一，异常类型二。。。。):
    发生异常执行的代码
     ###两种方法  根据具体实例需要
try:
   可能出现异常的代码 as z    #z可以展示错误的描述信息
except 异常类型一:
    发生异常执行的代码
except 异常类型二:
    发生异常执行的代码
'''


# print("-----test1-----")
# open('test.txt',"r")
# print("-----test1-----")
print("其他代码")
try:

    num=input("请输入一个数字")
    num=10/int(num)
    print("计算得到的结果是：",num)
except (ZeroDivisionError,IOError) as f:
    print("请输入正确的数字",f)
except  ValueError as z:
    print("请输入规定正确的值",z)

print("其他代码")








