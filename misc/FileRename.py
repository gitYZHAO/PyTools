# -*- codong:utf-8 -*-
# -*- coding: cp936 -*-

import os
import sys
from nt import chdir


# ȥ���ļ���ÿһ�� ���ݿ�ͷ�� �������֡�
def cutListName():
    fo = open("E:\\python\\temp", 'r')
    fc = fo.readlines()

    line = 1
    for l in fc:
        line = line + 1
        # ǰʮ��ֻ��Ҫɾ����ʼ��2���ַ�������"P403.��μ����㷨�ĸ��Ӷ�" ��ɾ��"P4"
        if line < 10:
            l = l[2:]
            print(l)
        else:
            l = l[3:]
            print(l)

    fo.close()


# ��������Ӧ�ļ����µ��ļ���
def rename():
    path = "G:\\BaiduYunDownload\\X�ļ���\\"
    olds = ".blv"
    news = ".mp4"

    filelist = os.listdir(path)  # ���ļ����µ������ļ�

    for file in filelist:  # ���������ļ� �����ļ���
        # print("ԭʼ�ļ���Ϊ :%s"%file)
        index = file.rfind(olds)
        # print(index)
        if index > 0:
            newName = file.replace(olds, news)
            # newName=file[index+3:]
            print("���ļ���Ϊ :%s" % newName)

            # ����chdir()�������뵽Ŀ���ļ����ڵ�·��
            chdir(os.path.dirname(path + file))  # ��������ļ��У���Ҫ��Ӵ����
            os.rename(file, newName)  # ������

        # ��Ӻ�׺�� `.mp4`
        # else:
        #    newName = str(file+".mp4")
        #    print("%s" %newName)
        #    chdir(os.path.dirname(path+file))
        #    os.rename(file,newName)

        #
        # Olddir = os.path.join(path,file)#ԭ���ļ��е�·��
        # if os.path.isdir(Olddir):#������ļ��У�������
        #    print("%s ���ļ���" %Olddir)
        # filename = os.path.splitext(file)[0]  #�ļ���
        # filetype = ".jpg"#os.path.splitext(file)[1]   �ļ���չ��
        # Newdir = os.path.join(path,str(count)+filetype) #�µ��ļ�·��
        # os.rename(Olddir,Newdir) #������


if __name__ == '__main__':
    # cutListName()
    rename()
