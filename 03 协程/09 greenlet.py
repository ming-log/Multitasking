# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 17:06
from greenlet import greenlet
import time


def test1():
    while True:
        print('---- A ----')
        gr2.switch()
        time.sleep(2)


def test2():
    while True:
        print('---- B ----')
        gr1.switch()
        time.sleep(2)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
