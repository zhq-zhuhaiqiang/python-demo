#coding:utf-8
"""
定义一个类
"""
#类对象支持两种操作：属性引用和实例化。
class People:
  #定义公共的基本属性
  arms=2
  legs=2
  #定义私有属性,私有属性在类外部无法直接进行访问
  __weight = 0
  #定义类的私有方法
  def __sayName():
    print("我是私有方法，不能在类的外部访问")

  #定义方法，类方法中的第一个参数必须为self，该self表示的类的实例对象，self非python关键字，可使用任意值代替
  def showBody(s):
    print("人有%d 只手，%d 只脚" % (s.arms,s.legs))
  #类的转有方法，可以被重写
  def __init__(s):
    print("我是类对象的构造方法")
"""
类的继承
当基类跟子类在同一作用域时：
方式1：class DerivedClassName(BaseClassName1): 
当基类跟子类不在同一作用域时：
方式2：class DerivedClassName(modname.BaseClassName):
多继承：
方式3：class DerivedClassName(Base1, Base2, Base3):
      需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索，默认调用的是在括号中排前地父类的方法

"""
class Me(People):
   def showBody(s):
    print("me有%d 只手，%d 只脚" % (s.arms,s.legs))


if __name__=="__main__":
    people=People()
    people.showBody()
    # print(people.__weight)
    me=Me()
    
    me.showBody()
    #用子类对象调用父类已被覆盖的方法
    super(Me,me).showBody()
  