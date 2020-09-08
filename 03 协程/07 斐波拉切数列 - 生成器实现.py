# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 16:00


# 使用生成器,生成斐波拉且数列
def fibo(num):
    n, before, after = 1, 0, 1
    while n <= num:
        # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        cc = yield before
        print('cc:', cc)
        print('-'*50)
        before, after = after, before + after
        n += 1
    return 'done'


# 如果在调用fibo的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器
a = fibo(10)
b = a.send(None)       # 第一次send如果没有next，只能传一个send(None)
print("b:", b)
b = a.send('123')  # 使用send可以往生成器内部传入参数
print("b:", b)
