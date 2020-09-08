# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 13:51

# 假设两个线程t1和t2都要对全局变量g_num（默认是0）进行加1运算，t1和t2都各对g_num加10次，g_num的最终结果应该为20
# 但是由于是多线程同时操作，有可能出现下面情况：
# 1. 在g_num=0时，t1取得g_num=0.此时系统把t1调度为"sleeping"状态，把t2转换为"running"状态，t2也获得g_num=0
# 2. 然后t2对得到的值进行加1并赋给g_num，使得g_num=1
# 3. 然后系统又把t2调度为"sleeping"，把t1转为"running"线程t1又把它之前得到的0加1后赋值给g_num。
# 4. 这样导致虽然t1和t2都对g_num加1，但结果仍然是g_num=1

import threading
import time

g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work1:", g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work2:", g_num)


def main():
    t1 = threading.Thread(target=work1, args=(1000000,))
    t2 = threading.Thread(target=work2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(5)
    print("result:", g_num)


if __name__ == '__main__':
    main()

# work1: 1156620
# work2: 1241692
# result: 1241692
# 产生资源竞争，最终得不到正确结果
