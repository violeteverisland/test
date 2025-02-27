# class a:
#     def __init__(self,param1,param2):
#         self.attribute1 = param1
#         self.attribute2 = param2
#
# class Washer:
#     height = 500
#     width = 460
#     def wash(self):
#         print("我会洗衣服")
#         print("self:",self)
# wa = Washer()   #实例化对象 对象 = 类名
# print(wa)   #显示对象在内存中地址
# wa.wash()
# wa2 = Washer()
# print(wa2)
#
# class Person:
#     name = "bingbing"
#     def run(self):     #self代表对象本身
#         print("self:",self)
#         wa3 = Washer()
#         print(wa3)
#         print("人类会跑步")
# pe = Person()
# print(pe)
# pe.run()
#
#
#
# #实例属性和类属性的区别
# #类属性是属于类的，是公共的，大家都能访问到
# #实例属性是属于对象的，是私有的，只能由对象名访问，不能由类名访问
# class Person1:
#     name = "bingbing"           #类属性
#     def introduce(self):        #实例方法
#         print("我是实例方法")
#         print(f"{Person1.name}的年龄：{self.age}")          #self.age是实例属性
# pe1 = Person1()
# pe1.age = 18
# pe1.sex = '女'       #实例属性，只有pe1能访问
# #实例属性只能由对象名访问不能由类名访问
# print(pe1.sex)
# #类属性可以由类名访问也可以由对象名访问
# print(Person1.name)
# print(pe1.name)
# pe1.introduce()
# pe2 = Person1()
# pe2.sex = '男'
# print(pe2.sex)
#
#
#
# #每实例化一次就需要添加一次，效率不高
# #构造函数__init__
# #作用：通常用来做属性初始化或赋值操作
# #注意：在类实例化对象的时候会被自动调用
# class Test:
#     def __init__(self):
#         print("这是__init__()函数")
# #实例化对象 ： 对象名 = 类名（）
# te = Test()

class PersonTest():
    name = 'bing'       #类属性
    def __init__(self,name,age):
        self.name = name      #实例属性
        self.age = age
    def play(self,game):
        self.game = game
        print(f"{self.name}在打{self.game}")
    def introduce(self,height):
        self.height = height
        print(f"{self.name}的年龄是{self.age},身高是{self.height}")
print(PersonTest.name)
pet1 = PersonTest('jy',22)
pet1.play('ys')
pet1.introduce(173)
pet2 = PersonTest('jlj',23)
pet2.play('wzry')
pet2.introduce(183)


#析构函数__del__()
#删除对象的时候解释器默认调用__del__()方法
class PersonDel():
    def __init__(self):
        print("我是__init__()")
    def __del__(self):
        print("被销毁了")
p = PersonDel()
del p
#del p语句执行时内存会立即被回收,会调用对象本身的__del__()方法
print("这是倒数第二行代码")
print("这是最后一行代码")
#正常运行不会调用__del__(）,对象执行结束之后,系统会自动调用__del__()
#__del__()主要是表示该程序块或函数已经全部执行结束


#面向对象的三大特性：封装 继承 多态
#封装:指的是隐藏对象中一些不希望被外部所访问到的属性或方法
#隐藏属性(私有权限)：只允许在类的内部使用，无法通过对象访问
#在属性名或方法名前面加两个下划线__
class personnel:
    name = 'bingbing'
    __age = 28      #隐藏属性
    # 方法2 在类的内部访问（推荐使用）
    def introduce(self): #实例方法
        print(f"{personnel.name}的年龄是{personnel.__age}")
        personnel.__age = 18
        print(f"{personnel.name}的年龄修改后是{personnel.__age}")     #在实例方法中访问类属性和隐藏属性
p1 = personnel()
print(p1.name)
personnel.name = 'ziyi'
print(personnel.name)
# #访问隐藏属性方法1：
# #隐藏属性实际上是把名字改为：_类名__属性名
# print(p1._personnel__age)
# p1._personnel__age = 18
# print(p1._personnel__age)
p1.introduce()

class Per:
    def __init__(self,name,age,game):
        print("this is __init__")
        self.name = name
        self.age = age
        self.game = game
        print(f"my name is {self.name},i'm {self.age} years old,my favorite game is {self.game}")
    def __del__(self):
        print("this is __del__")
    def nam(self,name):
        self.name = name
        print(f"my name is {self.name}")
    def age(self,age):
        self.age = age
    def game(self,game):
        self.game = game
per1 = Per('jy',18,'genshin impact')
print(per1.game)
#per1.__init__('jy',18,'genshin impact')
per1.nam('jy')
#私有属性/方法
# xxx:普通属性/方法，如果在类中定义,则类可以在任意地方使用
#_xxx:私有属性/方法,定义在类中，外部可以使用，子类也可以继承
#       但是在另一个py文件中from xxx import *无法导入
#       一般是为了避免与python关键字冲突使用的方法
#__xxx：双下划线开头,隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承
#       要访问只能通过间接的方式，另一个py文件from xxx import * 也无法导入
#       这种命名一般是python中魔术方法或属性,都是有特殊含义或功能的,自己不要轻易定义

class PerP:
    name = 'jj'
    __age = 54
    _sex = 'girl'
    def __init__(self):
        print("this is __init__()")
    def agel(self):
        print(self.__age)
perp = PerP()
print(perp._sex)    #会报错，使用对象名._属性名才可以调用
print(perp._PerP__age)  #隐藏属性方法1
perp.agel()     #隐藏属性方法2

class Man:
    def __play(self):       #隐藏方法
        print("玩手机")
    def funa(self):         #普通方法
        print("平平无奇的实例方法")
        Man.__play(self)        #实例方法中调用隐藏方法    -不推荐
        self.__play()           #推荐
man = Man()
man.funa()
man._Man__play()



#私有方法
class Girl:
    def _buy(self):     #私有方法
        print("整天买买买")
girl = Girl()
girl._buy()