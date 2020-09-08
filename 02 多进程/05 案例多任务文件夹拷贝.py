# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 11:34
import os
import multiprocessing
import time
import random


def copy_file(q, file, old_folder_name, new_folder_name):
    """完成文件的复制"""
    old_file_path = os.path.join(os.getcwd(), old_folder_name, file)
    new_file_path = os.path.join(os.getcwd(), new_folder_name, file)
    with open(old_file_path, 'rb') as f:
        data = f.read()
    with open(new_file_path, 'wb') as f:
        f.write(data)
    # print("%s ----->  %s" % (old_file_path, new_file_path))
    time.sleep(random.random())
    q.put(file)


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹名字:")

    # 2. 创建一个新的文件夹
    new_folder_name = old_folder_name + "[复件]"
    try:
        os.mkdir(new_folder_name)
    except:
        pass
    # 3. 获取文件夹的所有的待copy的文件名字    listdir()
    file_names = os.listdir(old_folder_name)
    # print(file_names)

    # 4. 创建进程池
    pool = multiprocessing.Pool(2)

    # 5. 创建队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加copy文件的任务
    for file_name in file_names:
        pool.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    # 6. 复制原文件夹中的文件，到新文件夹中的文件去
    pool.close()
    # pool.join()
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print("%s 已经copy完成!" % file_name)
        copy_ok_num += 1
        rate = copy_ok_num / all_file_num
        # 进度条
        print("\rcopy完成进度:[" + '=' * int(rate * 30) + '>' * (1-int(rate)) +
              '-' * (30 - int(rate * 30)) + '] %.2f %%' % (rate * 100), end="")
        if copy_ok_num >= all_file_num:
            break
    print()

if __name__ == '__main__':
    main()
