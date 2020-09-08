# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 13:24
# 定义一个全局变量
import threading
import time



def test1(temp):
    temp.append(33)
    print("----- in test1 temp=%s -----" % str(temp))


def test2(temp):
    print("----- in test1 temp=%s -----" % str(temp))


g_nums = [11, 22]


def main():
    # target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据过去
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(0.5)

    t2.start()
    time.sleep(0.5)

    print("----- in main thread g_num = %s -----" % g_nums)


if __name__ == '__main__':
    main()
# ----- in test1 temp=[11, 22, 33] -----
# ----- in test1 temp=[11, 22, 33] -----
# ----- in main thread g_num = [11, 22, 33] -----
# 子线程之间共享全局变量
# 多任务往往相互配合
