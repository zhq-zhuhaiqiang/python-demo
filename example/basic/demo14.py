#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
随机产生验证码
"""
from functools import wraps
import random

code = ""
for i in range(4):

    num = random.randrange(0, 2)

    # 当前位显示字母或者数字各有50%几率
    if num == 0:
        # 随机显示数字
        r1 = random.randrange(0, 10)
        code += str(r1)
    else:
        # 随机显示字母
        i = random.randrange(65, 91)
        c = chr(i)
        code += c

# print(code)
# print("最外层装饰器".rjust(20, "="))
def sayHi(name="我是朱海强"):
  def myself():
    return '''我是
            默认的朱海强
          '''
  def otherP(name):
    return name
  if name=="我是朱海强":
    return myself
  else :
    return otherP
  
def sayHi2(func):
  return func()()

##################################################################函数装饰器
# print(sayHi2(sayHi))

def decoratorss(func):
  @wraps(func)
  def inners():
    print("执行函数func前")
    func()
    print("执行函数后")
  return inners
@decoratorss
def paraF():
  """被装饰的函数"""
  print("我是函数类型参数")

paraF()
# paraF=decoratorss(paraF)
# paraF()
print(paraF.__name__,paraF.__doc__)
# otherRepleace=sayHi
# del sayHi
# # print(sayHi())
# print(otherRepleace())
# print(chr(1114112))
####
def mydef(*args,**paras):
  print(args)
mydef([123])
###类装饰器
class myclass():
  def __init__(self,func):
    self._func=func
  def __call__(self):
    print("class decorator running  ")
    self._func()
    print("class decorator ending")
@myclass
def bar():
  print("我是被装饰的函数")

bar()
print(bar.__name__)

