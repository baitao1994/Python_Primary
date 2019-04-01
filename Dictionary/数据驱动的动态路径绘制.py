#编写程序，根据文件data.txt中的数据，使用turtle库来动态绘制图形路径
#文件第一列是乌龟爬行的距离，第二列0是向左转，1是向右转，第三列是转动角度
#第四、五、六列是颜色RGB

import turtle 
 
def main():
    #设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800, 600, 0, 0)
    #设置画笔
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)
    #读取文件
    result=[]#这里必须建一个空列表，将下面几个列表放进去，表中表
    file = open("data.txt","r")
    for line in file: #循环文件的每一行
        result.append(list(map(float, line.split(','))))#list()新建一个列表
        #这句话的意思：建一个列表，line字符串中的东西放进去，再将每个列表放到上面的result列表中
    print(result)
    #动态绘制
    for i in range(len(result)):#len() 是长度，返回的是整型数，不能被迭代，前面必须加range()
        pen.color((result[i][3],result[i][4],result[i][5]))
        #循环result列表每一个元素，而每个元素都是列表，所以要以result[][]区分
        pen.forward(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])#向右转，相当于right
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)
'''
line.split()返回一个列表
map(function, iterable, ...) --> map object,返回一个map对象，而不是列表，不能被订阅，所以前面必须加list()函数
def square(x) : # 计算平方数
return x ** 2
map(square, [1,2,3,4,5]) # 计算列表各个元素的平方

range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。

list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
'''

if __name__ == '__main__':
    main()
