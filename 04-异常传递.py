# coding=gbk
# @file:04-异常传递.py
# @data:2021/7/10 21:50
# Editor:clown
'''
是python异常处理的底层机制，是原理层面上
不需要我们自己写代码实现，是python已经实现好的

异常传递：当一行代码发生异常之后，会向代码发生异常之后，
会向外层将这个异常进行传递
'''
# try 嵌套
num = input("请输入一个数字")
# 内层try代码中发生的异常，没有被捕获，会向外层进行传递
try:
    try:
        a=int(num)
    except ZeroDivisionError:
        print("发生异常")
    finally:
        print("我都执行了")
    num = 10 / int(num)
    print(f"计算的结果是<{num}>")
except Exception as  z:
    print("异常错误的信息：", z)


print("计算得到的结果是：", num)
print("其他功能代码")
