# coding=gbk
# @file:02-module_����.py
# @data:2021/7/11 9:50
# Editor:clown
# ʹ��ǰ����Ҫ����ģ��
import random
import os
#����һ�� import ģ����
import test_module
print(test_module.num)  #�����еı�������
test_module.func()  #ģ���еĺ�������
dog=test_module.Dog  #�����е������
dog.show_info()

# ������ from ģ����  import ������1,������2.....
#ʹ�ù�����
# ע��㣺�������ͬ�õķ���������ᱻ����
# from test_module1 import func,num
# from test_module import num
# func()
# print(num)

'''
�������� from ģ����  import * ʹ��ģ�������еĹ��ܽ��е���
ʹ�ù�����
'''
from test_module import *
print(num)
func()
dog=Dog()
dog.show_info()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# as  ����������Զ�ģ��͹��������
# ע�� ���ʹ��as���� ��������ʹ��ԭ��������
import test_module as nnnn
nnnn.func()
print("*"*30)
# ��Ҫʹ��ģ���е����ݣ������ִ���ģ��
# ע��㣺�����������Լ���д��ģ��
# ʹ�õ�ģ��ʹ����ļ���Ҫ��һ��Ŀ¼��
#Ƕ�׵�Ŀ¼���棺Mark directory as  ֮���� sources boot

import test_module_01
print(num)
