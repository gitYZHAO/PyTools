# -*- codong:utf-8 -*-
# -*- coding: cp936 -*-

import os
import sys
from nt import chdir


# 去掉文件中每一行 内容开头的 几个数字。
def cutListName():
    fo = open("E:\\python\\temp", 'r')
    fc = fo.readlines()

    line = 1
    for l in fc:
        line = line + 1
        # 前十个只需要删掉开始的2个字符，比如"P403.如何计算算法的复杂度" ，删除"P4"
        if line < 10:
            l = l[2:]
            print(l)
        else:
            l = l[3:]
            print(l)

    fo.close()


# 重命名响应文件夹下的文件名
def rename():
    path = "G:\\BaiduYunDownload\\X文件夹\\"
    olds = ".blv"
    news = ".mp4"

    filelist = os.listdir(path)  # 该文件夹下的所有文件

    for file in filelist:  # 遍历所有文件 包括文件夹
        # print("原始文件名为 :%s"%file)
        index = file.rfind(olds)
        # print(index)
        if index > 0:
            newName = file.replace(olds, news)
            # newName=file[index+3:]
            print("新文件名为 :%s" % newName)

            # 先用chdir()函数进入到目标文件所在的路径
            chdir(os.path.dirname(path + file))  # 如果不是文件夹，需要添加此语句
            os.rename(file, newName)  # 重命名

        # 添加后缀名 `.mp4`
        # else:
        #    newName = str(file+".mp4")
        #    print("%s" %newName)
        #    chdir(os.path.dirname(path+file))
        #    os.rename(file,newName)

        #
        # Olddir = os.path.join(path,file)#原来文件夹的路径
        # if os.path.isdir(Olddir):#如果是文件夹，则跳过
        #    print("%s 是文件夹" %Olddir)
        # filename = os.path.splitext(file)[0]  #文件名
        # filetype = ".jpg"#os.path.splitext(file)[1]   文件扩展名
        # Newdir = os.path.join(path,str(count)+filetype) #新的文件路径
        # os.rename(Olddir,Newdir) #重命名


if __name__ == '__main__':
    # cutListName()
    rename()
