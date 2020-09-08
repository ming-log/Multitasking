# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 13:24
# 定义一个全局变量
import threading
import time

g_num = 100


def test1():
    global g_num
    g_num += 1
    print("----- in test1 g_num=%d -----" % g_num)


def test2():
    print("----- in test2 g_num=%d -----" % g_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(0.5)

    t2.start()
    time.sleep(0.5)

    print("----- in main thread g_num = %d -----" % g_num)


if __name__ == '__main__':
    main()
# ----- in test1 g_num=101 -----
# ----- in test2 g_num=101 -----
# ----- in main thread g_num = 101 -----
# 子线程之间共享全局变量
