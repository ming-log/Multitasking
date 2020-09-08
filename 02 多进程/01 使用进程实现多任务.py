# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 9:29
import multiprocessing
import time


def test1():
    while True:
        print('----- 1 ------')
        time.sleep(1)


def test2():
    while True:
        print('----- 2 ------')
        time.sleep(1)


def main():
    m1 = multiprocessing.Process(target=test1)
    m2 = multiprocessing.Process(target=test2)
    m1.start()
    m2.start()


if __name__ == '__main__':
    main()
