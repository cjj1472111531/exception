# coding=gbk
# @file:03-异常完整结构.py
# @data:2021/7/10 21:33
# Editor:clown
'''
try:
    可能出现异常的代码
except Exception as e:
    发生异常执行的代码
else:
    代码没有发生异常会执行
finally：
    不管发不发生异常都会执行


'''
try:
    num=input("请输入一个数字")
    num=10/int(num)
    print("计算得到的结果是：",num)
except Exception as e:
    print('你输入有误，请在此输入',e)
else:
    print("else就是：代码没发生异常输出")
finally:
    print("无论如何我都会把这个打印出来嘿嘿")




