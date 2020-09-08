# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 17:12
import gevent
import time
from gevent import monkey
# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，全都换位gevent中自己实现的模块


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(2)  # 使用其他模块的函数时，需要声明monkey.patch_all()


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5)
])
