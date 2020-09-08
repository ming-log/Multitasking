# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 11:05
import threading
import time


def test1():
    for i in range(5):
        print('----- test1 ---- %d ---' % i)
        time.sleep(1)


def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1, name='thread1')

    # 在调用Thread之后打印
    print(threading.enumerate())
    t1.start()

    # 在调用start之后打印
    print(threading.enumerate())


if __name__ == '__main__':
    main()

# [<_MainThread(MainThread, started 5260)>]
# [<_MainThread(MainThread, started 5260)>]
# [<_MainThread(MainThread, started 5260)>, <Thread(thread1, started 11492)>]
# 说明当调用threading的时候不会创建线程，
# 当调用Thread实例对象对象的start方法时才开始创建线程，并开始线程，
# 主线程默认等待子线程结束，主线程要是先结束，不管子线程是否结束,都会直接结束
