# coding=gbk
# @file:05-抛出自定义异常.py
# @data:2021/7/10 23:59
# Editor:clown
'''
程序为什么会报错
因为不符合语法  因为python的作者在待命中使用了if判断
如果除数为0  就会在代码中抛出异常


抛出异常：
    raise 异常对象 #当程序代码遇到raise的时候 程序就报错了

异常对象=异常类（参数）

抛出自定义异常：
1.自定义异常类，继承Exception或者 BaseExceptio
2.选择书写，定义__init__方法 定义__str__方法
3.在合适的实际排除异常对象

'''
import os


class PasswordLengthError(Exception):
    print("fuck everything")
    def __str__(self):  #重写就是调用自己的信息
        return "zzzzzz"
    pass

def get_password():
    pass_word=input("请输入密码")
    if len(pass_word)>=6:
        print("密码长度合格")
    else: #抛出异常
        raise  PasswordLengthError("长度密码不足6位")
        print("clown fuck")

try:
    get_password()
except PasswordLengthError as z:
    print("捕获异常出现的内容为:",z)


print("其他代码")



