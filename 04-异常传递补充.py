# coding=gbk
# @file:04-�쳣���ݲ���.py
# @data:2021/7/10 23:48
# Editor:clown
def func1():
    print("-------1-------")
    num=input("����������")
    print("***********")
    num=10/int(num)
    # print("������������������")
    print(num)
    print("-------2-------")

def func2():
    print("-------3-------")
    func1()
    print("-------4-------")

try:
    print("-------5-------")
    func2()
    print("-------6-------")
except Exception as e:
    print('-------7--------')
    print(e)

