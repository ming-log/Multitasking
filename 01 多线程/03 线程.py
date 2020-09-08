# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 10:12

# 一个程序运行起来以后，一定有一个执行代码的东西
# 这个东西就称之为线程

import threading
import time


def say_sorry():
    print("I am sorry for you!")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=say_sorry)
        t.start()
    print("---- end ----")
