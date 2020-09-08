# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 14:45

# 死锁
# 在线程间共享多个资源的时候，如果两个线程分别占有一部分资源且同时等待对方的资源就会造成死锁。
# 尽管死锁很少发生，但一旦发生就会造成应用的停止响应。
import threading
import time


class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程把mutexB上锁
        print(self.name + '---- do1 --- up ----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()                                    # 堵塞，等到B解锁才会继续执行
        print(self.name + '---- do1 --- down ----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程把mutexA上锁
        print(self.name + '---- do2 --- up ----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()                                    # 堵塞，等到A解锁才会继续执行
        print(self.name + '---- do2 --- down ----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
# 两边同时堵塞，造成死锁，程序无法进行
# 避免死锁方法
# 1. 添加超时时间
# 2. 程序设计时要尽量避免(银行家算法：解决死锁问题)
