# -*- coding:utf-8 -*-
import os
import random
import re
import string
import time
import traceback
import zipfile
from os import chdir

a = time.time()


def unzip(pwd):
    fp = 'E:\\test.zip'
    chdir(os.path.dirname(fp))
    zfile = zipfile.ZipFile(fp)  # 把要破解的zip的文件名替换ZipFile里面的参数

    # print(str(pwd))
    try:
        zfile.extractall(pwd=str.encode(str(pwd)), path='E:\\')
        print(u'密码是：' + str(pwd))
        print(u'破解时间是：' + str(time.time() - a))  # 破解时间减去开始那个时刻的时间，得到的就是破解这个压缩文件的时间

        exit(0)

    except Exception as error:
        # traceback.print_exc()
        pass  # 对应的异常处理就省略了


def zipcrackl(start, end):
    for i in range(start, end):
        if i % 10000 == 0:
            print('当前' + str(i))
        unzip(i)


def genrandompw(count, len):
    # count = int(input('请输入密码个数(必须大于0)： '))
    i = 0
    passwds = []
    while i < count:
        tmp = random.sample(string.ascii_letters + string.digits, len)
        passwd = ''.join(tmp)
        if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
            passwds.append(passwd)
            i += 1
    # print(passwds)
    return passwds


def forceunzip():
    print("开始数字+字母")
    i = 1
    while i < 10:
        for l in range(4, 10):
            # tmp = random.sample(string.ascii_letters + string.digits, l)
            tmp = random.sample(string.ascii_lowercase + string.digits, l)
            passwd = ''.join(tmp)
            # print(passwd)
            unzip(passwd)

        # if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
        # unzip(passwd)
        # i += 1


def main():
    """
    主函数
    """
    # zipcrackl(10970000, 9999999999)

    forceunzip()


if __name__ == '__main__':
    main()
