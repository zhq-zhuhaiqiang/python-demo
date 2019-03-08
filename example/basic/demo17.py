#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
利用生成器实现并行效果
"""

import time


def consumer(name):
    print("%s进入包子店" % name)
    while True:
        print("我是顾客，等待包子上来")
        # baozi=0
        baozi1,baozi2=yield '第一个yield'
        print("执行完 %s" % baozi2)
        xifan=yield '第二个yield'
        print("执行完 %s" % xifan)
        # print(baozi)
        # print("yield方法阻断结束，开始享受包子")
        # print("第[%s]笼包子来了，被[%s]吃了" % (baozi, name))


def producer():
    c1 = consumer("顾客A")
    # c2 = consumer("顾客B")
   
    # bc1=c1.__next__()
    # bc2=c2.__next__()
    print(next(c1))
    # print(c1.send(1,2)) 
    print(c1.send([1,2])) 
    # next(c2)
    # print(bc1)
    # print(123)
    # for i in range(1, 3):
    #     time.sleep(3)
    #     print("厨师做了第%d笼包子".center(20, "=") % i)
    #     c1.send(i)
    #     c2.send(i)
        # next(c1)

def create_counter(n):
    print("create_counter")
    while True:
        yield n
        print("increment n")
        n +=1
        print(n)
 
# gen = create_counter(2)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))


producer()
