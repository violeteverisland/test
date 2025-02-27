#实例方法 静态方法 类方法
class Dress(object):
    name = 'jy'
    def jk(self):
        print('wear jk')
    def lolita(self):
        print('wear lolita')
    def maid(self):
        print('wear maid clothes')
    def nun(self):
        print('wear nun')

    @classmethod
    def dress(cls):
        print(f'{cls.name} wear dress')

    @staticmethod
    def wedding(name):
        print(f'{name} wear wedding')

#接口
def wed(obj,name):
    obj.wedding(name)
#调用
wed(Dress,'jy')
Dress.wedding('jy')
dre = Dress()
dre.jk()
Dress.dress()
dre.dress()

