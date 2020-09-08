# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 15:19
from collections.abc import Iterable, Iterator
import time
# Iterable 可迭代对象
# Iterator 迭代器


class ClassMate:
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __next__(self):
        if self.current_num < len(self.names):
            c = self.names[self.current_num]
            self.current_num += 1
            return c
        else:
            raise StopIteration  # raise抛出异常，告诉for循环已经取完

    def __iter__(self):
        """
        如果想要一个对象成为一个可以迭代的对象，即可以使用for循环
        那么
            * 1. 必须实现__iter__方法
            * 2. 并且__iter__方法里面return一个实例对象，这个实例对象包含__iter__和__next__方法
        然后调用迭代器的时候就会调用实例对象的__next__方法
        """
        return self


classmate = ClassMate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

# print("判断classmate是否是可迭代对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)   # iter():创建一个迭代器
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))   # next():调用迭代器的next方法

for i in classmate:
    print(i)  # 结果返回1123，即ClassIterator中的返回值
    time.sleep(1)


# 总结:
#  1. 判断一个对象是否是可迭代对象，就是判断该对象是否有__iter__方法
#  2. 判断一个对象是否是迭代器，就是判断这个对象是否具有__iter__方法
#     并且该__iter__方法返回一个实例对象，并且这个实例对象具有__iter__和__next__方法
#  3. 综上所述，迭代器一定是可迭代对象，但是可迭代对象不一定都是迭代器
#  4. 使用iter()方法可以将一个可迭代对象转化为一个迭代器
