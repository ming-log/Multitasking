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
        time.sleep(2)  # 必须使用自带的延时函数


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


print("---- 1 ----")
g1 = gevent.spawn(f1, 5)
print("---- 2 ----")
g2 = gevent.spawn(f2, 5)
print("---- 3 ----")
g3 = gevent.spawn(f3, 5)
print("---- 4 ----")
g1.join()
g2.join()
g3.join()
