#继承
#就是让类与类之间变成父子关系,子类默认继承父类的属性和方法
# 1.语法
# class 类名（父类名）:
#     代码块
# 1.1单继承
class Person:       #称为父类
    def eat(self):
        print("i can eat")
    def sing(self):
        print("i can sing")
class Girl(Person):  #Personl类的子类
    pass        #占位符,代码里面类不写任何东西,会自动跳过,不会报错
girl = Girl()
girl.eat()
class Boy(Person):  #Person的子类
    None
boy = Boy()
boy.sing()
#子类可以继承父类的属性和方法,就算子类没有，也可以继承父类的.

#1.2继承的传递(多重继承）
#A/B/C C(子类)继承于B(父类)，B类（子类）继承A类（父类）,C类同时具有A/B类的属性/方法
class Father:
    def eat(self):
        print('i can eat')
    def sleep(self):
        print('i can sleep')
class Son(Father):      #Father 类的子类
    pass
class Grandson(Son):    #Son类的子类
    pass
son = Son()
son.sleep()
grandson = Grandson()
grandson.eat()
#继承的传递性就是子类拥有父类以及父类的父类中的属性和方法


#1.3重写：在子类中定义与父类相同名称的方法（也叫覆盖）
#1.覆盖父类方法
# class Person:
#     def money(self):
#         print('100w to be append')
# class Man(Person):
#     def money(self):
#         print('earn 1000w by myself')
# person = Person()
# person.money()
# man = Man()
# man.money()


#1.4对父类方法进行扩展，继承父类的方法,子类也可以增加自己的功能
#(1)父类名.方法名（self）
#(2)super().方法名()    --推荐用
#(3)super(子类名,self).方法名()
#super 在python里是一个特殊的类，super（）是使用super类创建出来的对象，可以调用父类中的方法
class Person:
    def money(self):
        print('100w to be append')
    def sleep(self):
        print("i'm sleeping")
class Son(Person):
    def money(self):
        #Person.money(self)
        # super().money()
        # super().sleep()     #可以调用其他方法
        super(Son,self).money()
        print('earn 1000w by myself')
person = Person()
#person.money()
son = Son()
son.money()