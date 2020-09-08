# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 10:53
#
# 当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，但如果
# 是上百个甚至上千个目标，手动的取创建进程的工作量巨大，此时就可以用到multiprocessing模块中的Pool方法

# 初始化Pool时,可以指定一个最大进程数，当有新的请求提交到Pool中时,如果池还没有满，那么就会创建
# 一个新的进程用来执行请求;但如果池中的进程数已经达到指定的最大值,那么该请求就会等待,直到池中有
# 进程结束,才会用之前的进程来执行新的任务。
# 进程池出现故障时不会显示故障信息
import os
import time
import random
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%s" % (msg, os.getpid()))
    # random.random()  随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕,耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)   # 定义一个进程池,最大进程数为3
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标，(传递给目标的参数元组,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i, ))

    print("--- start ---")
    po.close()   # 关闭进程池，关闭后po不再接收新的请求
    po.join()    # 等待po中所有的子进程执行完成，必须放在close语句之后
    print("--- end ---")
