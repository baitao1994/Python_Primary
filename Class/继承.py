#!/usr/bin/python3
#类定义
class people:

#定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):#每个方法都需要一个参数名，一半为self
        
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
#单继承示例
class student(people):

    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)#调用父类的构函
        
        self.grade = g
    def speak(self):#覆写父类的方法
        
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('ken',10,60,3)#类的实例化，得到一个对象
s.speak()

#类是对象的集合，这些对象拥有相同的属性和方法
