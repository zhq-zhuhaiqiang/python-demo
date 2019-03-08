#-*- coding:utf-8 -*-
'''
元组操作
'''
#使用()来声明一个元组，如果元组中只有一个元素的话，需要在第一个元素后面加','号，否则括号会被当成运算符来使用

import demo24,sys
def say():
  pass

# firsttuple=()
# print(type(firsttuple))
# firsttuple=('123')
# print(type(firsttuple))
# firsttuple=('123',)
# print(type(firsttuple))
####循环
def recy():
  i=0
  j=0
  while j<20:
    j+=1
    while i<10:
      i+=1
      if i==5:
        continue
      elif i==10:
        break
      elif i==12:
        return 
      print(i)
    else :
      print("循环前提不成立")
  else:
    print(20)
# a=1
# print(a)
import demo24
#索引、切片、加、乘、检查成员的操作
#元组的索引、切片类似与列表的操作
#元组是不可变的，不能进行修改操作
# a=(1,)
# b=(2,)
# b=a
print(dir())
# print(sys.path)
print(__doc__)
if __name__=="__main__":
  recy()

