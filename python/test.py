class Test:
    def __init__(self,name,age,game,sex):
        self.name = name
        self.age = age
        self.game = game
        self.sex = sex
        if sex == '女':
            print(f"{self.name} is {self.age} years old,and she likes playing {self.game}")
        else:
            print(f"{self.name} is {self.age} years old,and he likes playing {self.game}")
    def meme(self):
        pass
test = Test('jy',22,'genshin impact',"男")
class Ts(Test):
    pass
ts = Ts('jy',22,'honkai third','女')

print(Ts.mro())

class MyClass:
    def __dir__(self):
        return ["attr1", "attr2"]

obj = MyClass()
print(dir(obj))  # 输出: ['attr1', 'attr2']