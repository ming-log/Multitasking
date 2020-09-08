# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 17:12

# greenlet已经实现了协程，但是这个还得人工切换，是不是觉得太麻烦，不要着急，
# python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

# 其原理是当一个greenlet遇到IO(指的是input/output 输入/输出，比如网络、文件操作等)
# 比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行

# 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO


import gevent


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(5)  # 必须使用自带的延时函数


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
