#!/usr/bin/python3
#类定义
class people:

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
        print("这个第一个打印")
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

class student(people):
    def __init__(self,n,a,w,g):

#调用父类的构函
        people.__init__(self,n,a,w)#相当于 super(student,self).__init__(self,n,a,w)
        self.grade = g
        print("这个第二个打印")

#覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

#另一个类，多重继承之前的准备
class speaker():

    def __init__(self,n,t):
        self.name = n
        self.topic = t
        print("这个第三个打印")
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):

    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
        print("这个第四个打印")
        
test = sample("Tim",25,80,4,"Python")   #实例化时：会将构造函数中的内容调用一遍
test.speak()


#若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索,所以，student类中的speak方法就不执行了

#用子类对象调用父类已被覆盖的方法

#super(sample,test) 先找到sample的最近父类speaker，再将sample中的对象转化为speaker的对象

super(student,test).speak()#调用student父类（people）中被覆盖的speak方法
