# coding=gbk
# @file:test_module3.py
# @data:2021/7/11 10:36
# Editor:clown
__all__=['num','func']
num=3
def func():
    print("my_module1 func .....")

class Dog(object):
    @staticmethod
    def show_info():
        print("����һ��Dog��,test_module3 dog��")
    pass