# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 14:16

# 解决资源竞争问题

# 同步的概念
# 同步就是协同步调，按预定的先后次序进行运行。如:你说完，我再说
# "同"字从字面上容易理解为一起动作
# 其实不是，“同”字应是指协同、协助、互相配合。
# 如进程、线程同步，可以理解为进程或线程A和B一块配合，A执行到一定程度时要依靠B的某个结果，于是停下来，示意B运行；
# B执行，再将结果给A；A再继续操作。

# 解决线程同时修改全局变量的方式
# 对于上一小节提出的那个计算错误的问题，可以通过线程同步来进行解决
# 思路，如下:
# 1. 系统调用t1，然后获取到g_num的值为0，此时上一把锁，即不允许其他线程操作g_num
# 2. t1对g_num的值进行+1
# 3. t1解锁，此时g_num的值为1，其他的线程就可以使用g_num了，而且是g_num是值不是0而是1
# 4. 同理其他线程在对g_num进行修改时，都要先上锁，处理完后再解锁，
# 在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性

import threading
import time

g_num = 0


def work1(num, lock):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前已经被上锁，那么此时会堵塞在这里，直到这个锁被解开为止
    for i in range(num):
        # 锁上的代码越少越好,但是相应会降低程序的运行效率，因为一直在开关锁
        lock.acquire()
        g_num += 1
        lock.release()
    print("work1:", g_num)
    # 解锁


def work2(num, lock):
    global g_num
    for i in range(num):
        lock.acquire()
        g_num += 1
        lock.release()
    print("work2:", g_num)


def main():
    start = time.time()
    lock = threading.Lock()
    t1 = threading.Thread(target=work1, args=(1000000, lock))
    t2 = threading.Thread(target=work2, args=(1000000, lock))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("times:", str(end - start))
    time.sleep(1)


if __name__ == '__main__':
    main()
