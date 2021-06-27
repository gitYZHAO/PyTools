import os
import shutil

# 需要遍历的文件夹 路径
ROOT_WORK_PATH = r"C:\Work\code\Pro"
# 需要删除的文件夹名称
NEED_TO_DEL_FOLDER = "values-"
# 需要保留的文件夹名称
RESERVE_FOLDER = "values-zh-rCN"


def traverse_folders_find_spec_folder(folders, del_folder, exclude_folder):
    for root, dirs, files in os.walk(folders):
        for f in dirs:
            if str(f).startswith(del_folder):
                # 保留指定文件夹
                if str(f) == exclude_folder:
                    continue
                fnp = os.path.join(root, f)
                print(fnp)
                # PermissionError: [WinError 5]
                # os.rmdir(fnp)
                # 注意：删除！
                shutil.rmtree(fnp)
            traverse_folders_find_spec_folder(f, del_folder, exclude_folder)


if __name__ == '__main__':
    traverse_folders_find_spec_folder(ROOT_WORK_PATH, NEED_TO_DEL_FOLDER, RESERVE_FOLDER)
