# coding=UTF-8
#对象是对客观物体的抽象，类是对对象的抽象
#定义类
# class classname(object):
#     """
#     docstring
#     """
#     pass

class student:                      #类名是student，其中包含两个方法，分别打印一句话
    def gotoclass(self):
        print('gotoclass')
    def eat(self):
        print('eat')

#创建完类之后，可以创建对象
s1= student()
s1.gotoclass()                      #对对象进行调整
s1.eat()

s2=student()
s2.name='aa'
s2.age=22
print(s2.name)

#self   表示主动使用的对象
class car:
    def show(self):
        print('车品牌是%s,颜色是%s'%(self.brand,self.color))

c1=car()
c1.brand='奔驰'
c1.color='黑色'
c1.show()                           #调用show函数的是c1这个对象所以，self自动赋值为c1
