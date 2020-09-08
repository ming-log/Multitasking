# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 9:53
import time


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
    sing()
    dance()


if __name__ == '__main__':
    main()
