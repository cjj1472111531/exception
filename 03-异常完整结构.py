# coding=gbk
# @file:03-�쳣�����ṹ.py
# @data:2021/7/10 21:33
# Editor:clown
'''
try:
    ���ܳ����쳣�Ĵ���
except Exception as e:
    �����쳣ִ�еĴ���
else:
    ����û�з����쳣��ִ��
finally��
    ���ܷ��������쳣����ִ��


'''
try:
    num=input("������һ������")
    num=10/int(num)
    print("����õ��Ľ���ǣ�",num)
except Exception as e:
    print('�������������ڴ�����',e)
else:
    print("else���ǣ�����û�����쳣���")
finally:
    print("��������Ҷ���������ӡ�����ٺ�")




