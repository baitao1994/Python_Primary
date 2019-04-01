import turtle #调用库

def drawSnake(rad, angle, len, neckrad):#定义一个函数
    for i in range(len): #循环：len = 5 
        turtle.circle(rad, angle)#函数：乌龟沿着圆形轨迹爬行，rad描述圆形轨迹半径的位置
        turtle.circle(-rad, angle)#圆心在乌龟运行的左侧rad远的地方，如果rad为负值，则圆心在右侧
    turtle.circle(rad, angle/2)#angle表示爬行的弧度值
    turtle.fd(rad)#沿直线爬行，等于turtle.forward()，里面的参数为爬行距离
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)#启动画图窗口，参数分别表示长（像素）、宽、和窗口左上角在屏幕的位置
    pythonsize = 30
    turtle.pensize(pythonsize)#小乌龟的轨迹宽度
    turtle.pencolor("blue")
    turtle.seth(-40)#小乌龟启动时运行的方向，东0，北90，西180，南270，负值相反方向
    drawSnake(40,80,5,pythonsize/2)#调用drawSnake函数

main()
 
#轨迹有宽度，turtle.circle()函数中第一个参数是圆心距离轨迹中心的长度

#由于 def 定义的函数在程序中未经调用不会被执行，整个程序的第一条语句是 main(),表示执行名为 main()的函数
