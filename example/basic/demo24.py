# -*- coding:utf-8 -*-
#操作列表、元组、集合、字典
"""
python中的五种标准的数据类型：Numbers、String、List、Tuple、Dictionary
 Numbers中包含：int、long、float、complex
序列是python中的最基本的数据结构，序列都可进行索引、切片、加、乘、检查成员的操作
python中有6中内置的序列，其中列表和元组是最常见的序列
"""
import sys
# for i in range(101):
#     print(i)
def allDataType():
  Tuple=()
  List=[]
  Set=set()
  Dictionary={}
  print(type(Tuple))
  print(type(List))
  print(type(Set))
  print(type(Dictionary))


def checkDataType():
  checkData1=[1,float(123),complex(1,2),'朱海强']
  checkData2=[1,1.1,3.14j]
  recyclic(checkData1)
  print("=".center(20,"="))
  recyclic(checkData2)
def recyclic(obj):
   print(isinstance(obj,list))
   for i in obj:
     itype=type(i)
     print("我是%s类型的对象：%s " % (itype,i)) 
     print(isinstance(i,List))
def oplist():
  print("测试列表的操作")
  f=open('my.txt','w')
  #使用一对[]来声明一个列表，列表中的元素使用','号隔开，列表中的元素类型没有要求
  firstlist=[1,2,3,4,'我是列表元素']
  print(firstlist,sep='',end='',file=f)

  #索引
  # for i in range(len(firstlist)):
  #   print("第%-2d个元素:%2s" % (i,firstlist[i]))
  # for i in firstlist:
  #   print(i)
  #切片
  # print(firstlist[:1])
  # print(firstlist[1])
  #修改列表中的元素
  print(firstlist[0],file=f)
  firstlist[0]=0
  print(firstlist[0],file=f)
  #删除列表中的元素
  del firstlist[0]
  print(firstlist[0],file=f)
  # for i in firstlist:
  #   del i
  # print(len(firstlist))
  # for i in range(len(firstlist)):
  #   del firstlist[i]
  # print(len(firstlist))
   #向列表中添加元素
  firstlist.append(34)
  #列表的+:列表的拼接、*：重复列表操作

  firstlist=firstlist+[35,'36']
  firstlist=firstlist*2
  print(firstlist.copy())
  print(firstlist)
  # for i in firstlist:
    
  #   print(i,end='')
  print('列表操作结束')
  f.close
 
  
  pass
def optemp():
  pass
def opset():
  pass
def opdict():
  pass
print("我是demo24.py，我被别人import了")
if __name__=="__main__":
  pass
  #  oplist()
  # checkDataType()
  # allDataType()