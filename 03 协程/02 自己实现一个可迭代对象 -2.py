# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 14:59
from collections.abc import Iterable, Iterator
# Iterable 可迭代对象
# Iterator 迭代器


class ClassMate:
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """
        如果想要一个对象成为一个可以迭代的对象，即可以使用for循环
        那么
            * 1. 必须实现__iter__方法
            * 2. 并且__iter__方法里面return一个实例对象，这个实例对象包含__iter__和__next__方法
        然后调用迭代器的时候就会调用实例对象的__next__方法
        """
        return ClassIterator(self)


class ClassIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        c = self.obj.names[0]
        return c


classmate = ClassMate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

print("判断classmate是否是可迭代对象:", isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)   # iter():创建一个迭代器
print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
print(next(classmate_iterator))   # next():调用迭代器的next方法

for i in classmate:
    print(i)  # 结果返回1123，即ClassIterator中的返回值
