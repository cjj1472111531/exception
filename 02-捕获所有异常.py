# coding=gbk
# @file:02-���������쳣.py
# @data:2021/7/10 21:06
# Editor:clown
'''
try:
 ���ܷ����쳣�Ĵ���
except:  #ȱ�㲻�ܻ�ȡ�쳣������Ϣ
�����쳣ִ�еĴ���


try:
 ���ܷ����쳣�Ĵ���
except  Exception as  e:
    �����쳣ִ�еĴ���
    print(e)
    pass
'''
print("��������")
try:

    num=input("������һ������")
    num=10/int(num)
    print("����õ��Ľ���ǣ�",num)
except Exception as e:
    print('�������������ڴ�����',e)

print("��������")






