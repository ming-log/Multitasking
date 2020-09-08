# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 13:24

num = 100
nums = [1, 2, 3]


def test():
    global num
    num += 100


def test1():
    nums.append(100)


print(id(num))
print(id(nums))

test()
test1()

print(id(num))
print(id(nums))

# 即要修改全局变量的存储地址，必须使用global参数进行声明
# 如果不需要修改全局变量的存储地址则不需要global声名
