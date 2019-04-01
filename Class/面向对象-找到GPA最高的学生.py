# 找到GPA最高的学生
 
class Student:#定义一个类，里面是它的成员函数和成员变量
    def __init__(self, name, hours, qpoints):
        
        '''
        用类定义对象：先用__init__构造函数初始化对象的各属性，再定义其它函数
        定义类的成员函数时，必须默认一个变量代表类定义的对象本身（自行定义）
        每一个 student 类的对象（s和best都是类的对象）记录一个学生的信息（本程序中记录姓名、学时、成绩）
        __del__ 析构函数：销毁对象
        '''

        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
     #定义一系列能获得上面信息的“方法”，这些方法才能调用那些变量
    def getName(self):
        return self.name
     
    def getHours(self):
        return self.hours
     
    def getQPoints(self):
        return self.qpoints
     
    def gpa(self):
        return self.qpoints/self.hours
     
def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)#返回的是一个对象？给类赋初始属性（值），__init__最初定义了三个参数
     
def main():
    # 打开输入文件
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')
    # 设置文件中第一个学生的记录为best
    best = makeStudent(infile.readline())#已经将第一行读取，后面讲从第二行开始
 
    # 处理文件剩余行数据
    for line in infile:
        # 将每一行数据转换为一个记录
        s = makeStudent(line)
        # 如果该学生是目前GPA最高的，则记录下来
        if s.gpa() > best.gpa():
            best = s
    infile.close()
 
    # 打印GPA成绩最高的学生信息
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())
 
if __name__ == '__main__':#当直接运行文件时，下面的main()被执行；当import此文件时，下面的不执行
    main()
