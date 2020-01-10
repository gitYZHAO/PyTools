# -*- coding:utf-8 -*-

import os

# 指定要转码的文件（支持遍历所有的文件夹）
path = r"C:\TEST"
path_out = path + "(压缩)"
SLASH = r'\\'

#
FFMPEG = 'ffmpeg'

# 输入格式
# INFMT=".m4a"
# INFMT=".wmv"
# INFMT=".flv"
# INFMT=".mov"
# INFMT=".mkv"
INFMT = ".mp4"

# 输出格式
# OUTFMT = "mkv"
OUTFMT = ".mp4"
# OUTFMT=".mp3"


def trans(p):
    files = os.listdir(p)
    for file in files:
        nf = p + SLASH + file
        if os.path.isdir(nf):
            # 如果是文件夹，但输出文件夹不存在，则生成
            if not os.path.exists(nf.replace(path, path_out)):
                os.makedirs(nf.replace(path, path_out))
            trans(nf)

        # print(file)
        if file[-4:] == INFMT:
            filePathName = p + SLASH + file[:-4]
            filePathNameOut = filePathName.replace(path, path_out)
            # print(filePathName)

            # 输入文件 全路径名
            input_file = filePathName + INFMT

            # 输出文件 全路径名
            output_file = filePathNameOut + OUTFMT

            c_args = [
                '-i \"%s\"' % input_file,
                # 音频
                # '-ab 96 -f mp3',

                # 视频
                '-max_muxing_queue_size 1024',
                '-r 18',  # 帧数
                '-b 1800k',  # 波特率（注意有k）
                # '-s 1280*720',  # 分辨率
                # '-c:v copy', # 不修改视频的编码格式
                # '-c:a copy',  # 不修改音频的编码格式
                '-ab 64k',  # 音频波特率（与video相同 有k）
                '-f mp4',
                # '-ss 0:00 -t 34:50', #截取开始和结束时间
                # '-n',  # 不覆盖视频
                '\"%s\"' % output_file
            ]

            # 音频
            # command = 'ffmpeg -i \"%s\" -ab 96 -f mp3 \"%s\"' % (input_file, output_file)
            # 视频
            command = ' '.join([FFMPEG] + c_args)

            print(command)
            # os.system(command)


if __name__ == '__main__':
    if not os.path.exists(path_out):
        os.makedirs(path_out)

    trans(path)
