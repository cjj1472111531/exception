# coding=gbk
# @file:05-�׳��Զ����쳣.py
# @data:2021/7/10 23:59
# Editor:clown
'''
����Ϊʲô�ᱨ��
��Ϊ�������﷨  ��Ϊpython�������ڴ�����ʹ����if�ж�
�������Ϊ0  �ͻ��ڴ������׳��쳣


�׳��쳣��
    raise �쳣���� #�������������raise��ʱ�� ����ͱ�����

�쳣����=�쳣�ࣨ������

�׳��Զ����쳣��
1.�Զ����쳣�࣬�̳�Exception���� BaseExceptio
2.ѡ����д������__init__���� ����__str__����
3.�ں��ʵ�ʵ���ų��쳣����

'''
import os


class PasswordLengthError(Exception):
    print("fuck everything")
    def __str__(self):  #��д���ǵ����Լ�����Ϣ
        return "zzzzzz"
    pass

def get_password():
    pass_word=input("����������")
    if len(pass_word)>=6:
        print("���볤�Ⱥϸ�")
    else: #�׳��쳣
        raise  PasswordLengthError("�������벻��6λ")
        print("clown fuck")

try:
    get_password()
except PasswordLengthError as z:
    print("�����쳣���ֵ�����Ϊ:",z)


print("��������")



