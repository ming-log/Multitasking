# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 15:40
class Fibonacci:
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)
for num in fibo:
    print(num)

list(num)  # 也是通过迭代取当中的值，然后再放入list中返回
tuple(num)  # 也是通过迭代取当中的值，然后再放入tuple中返回
