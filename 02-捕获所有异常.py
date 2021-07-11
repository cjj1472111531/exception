# coding=gbk
# @file:02-捕获所有异常.py
# @data:2021/7/10 21:06
# Editor:clown
'''
try:
 可能发生异常的代码
except:  #缺点不能获取异常描述信息
发生异常执行的代码


try:
 可能发生异常的代码
except  Exception as  e:
    发生异常执行的代码
    print(e)
    pass
'''
print("其他代码")
try:

    num=input("请输入一个数字")
    num=10/int(num)
    print("计算得到的结果是：",num)
except Exception as e:
    print('你输入有误，请在此输入',e)

print("其他代码")






