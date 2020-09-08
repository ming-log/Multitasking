# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 17:00
import time


def task1():
    while True:
        print('----- 1 -----')
        time.sleep(0.1)
        yield


def task2():
    while True:
        print('----- 2 -----')
        time.sleep(0.)
        yield


def main():
    t1 = task1()
    t2 = task2()
    while True:
        # t1.send(None)
        # t2.send(None)
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
