#需求：5个Turtle对象， 1个绘制外表盘+3个模拟表上针+1个输出文字
# Step1：建立Turtle对象并初始化
# Step2：静态表盘绘制
# Step3：根据时钟更新表针位置与时间信息



from turtle import *
from datetime import *


def skip(step):
    penup()
    forward(step)
    pendown()


def mkHand(name, length):
    # 注册Turtle形状，建立三个表针Turtle
    reset()#重置所有设置，包括pen的位置
    skip(-length * 0.1)#画笔先往表盘中心后退一点，在画出整个指针，神似！
    begin_poly()# 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    forward(length * 1.1)
    end_poly()# 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    handForm = get_poly()# 返回最后记录的多边形
    # 注册Turtle形状命令register_shape(name,shape=None)
    register_shape(name, handForm)


def init():
    global secHand, minHand, hurHand, printer
    #全局语句是一个声明，它适用于整个循环代码块。这意味着列出的标识符将被解释为全局标识符

    mode("logo")  # 重置Turtle指向北
    #设置乌龟模式(“standard”，“logo” or “world”)，并执行重置。如果没有指定模式，则返回当前模式。


    # 建立三个表针Turtle并初始化
    mkHand("secHand", 125)#第二个参数为长度
    mkHand("minHand", 130)
    mkHand("hurHand", 90)


    secHand =Turtle()#新建一个Turtle 类的对象？，（在调用Turtle类的时候，默认创建TurtleScreen 对象）将secHand 对象放入TurtleScreen 中
    secHand.shape("secHand")#将turtle形状设置为具有给定名称的形状，如果没有指定名称，则返回当前形状的名称。
    # 带有名称的形状必须存在于TurtleScreen的形状字典中，因此需要（mkHand）注册形状：register_shape(name,t)
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand =Turtle()
    hurHand.shape("hurHand")

    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 4)# shapesize(stretch_wid=None, stretch_len=None, outline=None)，三个参数分别是拉伸宽度、长度、外形宽度
        hand.speed(0)# Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning，but 0 is fastest

    # 建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):#范围：[0,60)
        skip(radius)
        if i % 5 == 0:#逢5，画一个大刻度，其余的画小刻度
            forward(10)
            skip(-radius - 10)#将pen移回原点
        else:
            dot(5)#turtle.dot(size=None, *color)画一个直径为size的圆，颜色默认黑色
            skip(-radius)
        right(6)


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]#weekday()：Return the day of the week as an integer, where Monday is 0 and Sunday is 6


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s年 %d月 %d日" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)#turtle.setheading(to_angle)为海龟设置方向，因为是360度，min和sec都要乘60
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center", font=("Courier", 14, "bold"))
    #turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
    # arg – object to be written to the TurtleScreen
    # move – True/False，默认False 不移动
    # align – one of the strings “left”, “center” or right”
    # font – a triple (fontname, fontsize, fonttype)

    printer.back(130)
    printer.write(Date(t), align="center", font=("Courier", 14, "bold"))
    printer.home()#pen回原点
    tracer(True)

    ontimer(Tick, 100)  # 100ms后继续调用tick
    #turtle.ontimer(fun, t=0)  安装一个计时器，在t 毫秒之后调用fun


def main():
    tracer(False)  #打开小海龟动画
    init()#建立三个指针Turtle 以及一个输出文字Turtle
    SetupClock(160)#建立表盘图形
    tracer(True)#关闭小海龟动画
    Tick()#设置延迟
    mainloop()


if __name__ == "__main__":
    main()
