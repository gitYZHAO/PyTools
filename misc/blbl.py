# -*- coding:utf-8 -*-
import os
import json

'''
NOTE:
哔哩哔哩保存视频的提取合成（2019年后缓存的视频不再是flv格式，需要将音频和视频合成）
这里默认使用FFMPEG来合成音视频
'''

# 指定工作路径(Windows环境路径)
PATH = r"E:\BaiduYunDownload\80342641"

BACKSLASH = '\\'
WORK_FOLDER = PATH + BACKSLASH


def decodeJsonFile(subp):
    files = os.listdir(subp)
    for file in files:
        if file.rfind("entry.json") >= 0:
            curr = WORK_FOLDER + subp + BACKSLASH
            with open(curr + file, encoding='utf-8') as jsonfile:
                entry = json.load(jsonfile)
                folder_name = entry['type_tag'] + BACKSLASH
                res_name = entry['page_data']['part'] + '.mp4'
                print("资源文件夹：" + folder_name)
                print("视频文件名：" + res_name)
                i = curr + folder_name
                o = WORK_FOLDER + res_name
                print("资源路径：" + i + " ,输出文件名路径：" + o)
                if folder_name.startswith('lua.flv'):
                    rename(i, o)
                else:
                    merge(i, o)


def rebuild(path):
    os.chdir(os.path.dirname(path))
    subpaths = os.listdir()
    for subp in subpaths:
        decodeJsonFile(subp)


def rename(inpath, outpath):
    infn = inpath + '0.blv'
    command = "move \"%s\" \"%s\"" % (infn, outpath)
    print(command)
    os.system(command)


def merge(inpath, outpath):
    command = 'ffmpeg -i %s -i %s -codec copy \"%s\"' \
              % (inpath + r'audio.m4s'
                 , inpath + r'video.m4s'
                 , outpath)
    print(command)
    os.system(command)


if __name__ == '__main__':
    rebuild(WORK_FOLDER)
