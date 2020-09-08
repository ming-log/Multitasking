# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 11:55
from threading import Thread
import time


class MyThread(Thread):
    # 重写run()方法
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()    # start()会自动调用run(),run()方法执行完,线程结束
