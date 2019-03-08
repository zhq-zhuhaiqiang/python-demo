# coding:utf-8
"""
set集合是一个无序的元素不能重复的元素序列
可以使用{}或set()的方式创建，
创建一个空集合时，不能使用{}，必须使用set(),因为{}是用来创建空字典的
注意：python中的可hash与不可hash的概念
      可变的类型是不可hash的
      不可变的类型是可hash的
注：
可能你会问，set 不是可以接受 list，并将其转换为 set 吗？比如set([1, 2, 3])，注意，上文说的可哈希，不可哈希，是对可迭代类型（iterables）所存储元素（elements）的要求，[1, 2, 3]是可迭代类型，其存储元素的类型为int，是可哈希的，如果set([[1, 2], [3, 4]])，[[1, 2], [3, 4]]list of lists（list 构成的 list）自然是可迭代的，但其元素为 [1, 2] 和 [3, 4]是不可哈希的。
     
"""
# firstSet={2,1,1,3}
# secSet=set((1,))
# print(type(firstSet))
# print(type(secSet))
# print(firstSet)
#集合的运算：补集（-）、并集（|）、交集（&）、不同时包含于a和b的元素(^)
a=set([1,2,3,4])
b={3,4,5}
print(a-b)
print(a|b)
print(a&b)
print(a^b)
#集合的操作：添加、删除、
#添加一个元素
a.add((5,6))
#添加多个元素(参数可以是列表，元组，字典等),参数可添加多个用','号分割
a.update({'7':'qi','8':'ba'},(9,10))
# a.add([5,6])
#删除元素,元素不存在会报错
a.remove(9)
#删除元素，不存在时不抛异常
a.discard((10,9))
print(a)
