# coding=gbk
# @file:04-�쳣����.py
# @data:2021/7/10 21:50
# Editor:clown
'''
��python�쳣����ĵײ���ƣ���ԭ�������
����Ҫ�����Լ�д����ʵ�֣���python�Ѿ�ʵ�ֺõ�

�쳣���ݣ���һ�д��뷢���쳣֮�󣬻�����뷢���쳣֮��
������㽫����쳣���д���
'''
# try Ƕ��
num = input("������һ������")
# �ڲ�try�����з������쳣��û�б����񣬻��������д���
try:
    try:
        a=int(num)
    except ZeroDivisionError:
        print("�����쳣")
    finally:
        print("�Ҷ�ִ����")
    num = 10 / int(num)
    print(f"����Ľ����<{num}>")
except Exception as  z:
    print("�쳣�������Ϣ��", z)


print("����õ��Ľ���ǣ�", num)
print("�������ܴ���")
