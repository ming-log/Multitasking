# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 9:53
import time
import threading


def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("---- 正在唱:菊花台 ----")
        time.sleep(1)


def dance():
    """跳舞5秒钟"""
    for i in range(5):
        print("---- 正在跳舞 ----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

# 单核CUP在实现多任务的时候就采用时间片轮转方法
# 雨露均沾
# 真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量
# 所以，操作系统也会自动把很多任务轮流调度到每个核心上执行
# 真的多任务: 并行   (CUP核数 >= 任务数)
# 假的多任务: 并发   (CUP核数 < 任务数)


