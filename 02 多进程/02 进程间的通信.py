# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 10:32

# 1. socket    效率低
# 2. 文件的读写     效率低，硬盘的读写速度太慢
# 3. Queue队列    先进先出，使用内存存储临时数据
#          栈     后进先出
import multiprocessing

q = multiprocessing.Queue(4)
while True:
    if not q.full():   # 判断队列是否存满
        q.put(1)
    else:
        break
q.put(1)    # 存数据
q.get()          # 取数据
q.get_nowait()  # 取数据不等待
q.put_nowait()   # 存数据不等待
q.empty()  # 判断队列是否为空
