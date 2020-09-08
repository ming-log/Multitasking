# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/8 15:55
# 列表生成式
nums = [x*2 for x in range(10)]

# 生成器generator
nums = (x*2 for x in range(10))
# 使用next()方法取生成器的值
next(nums)

# 生成器是一种特殊的迭代器
# 生成器都是迭代器，但是迭代器不一定是生成器
