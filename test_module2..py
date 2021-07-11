# coding=gbk
# @file:test_module2..py
# @data:2021/7/11 10:35
# Editor:clown
__all__=['num','func']

num=2
def func():
    print("my_module1 func .....")

class Dog(object):
    @staticmethod
    def show_info():
        print("这是一个Dog类,test_module2 dog类")
    pass