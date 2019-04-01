from graphics import *

win = GraphWin("Celsius Converter", 600,500)# 创建窗口对象，长宽400 ×300像素,默认为200×200
win.setCoords(0.0, 0.0, 3.0, 4.0)
# setCoords (xll, yll, xur,yur)   设置窗口的坐标系。 左下是(xll,yll)， 右上角是(xur,yur)。 所有后面的绘制都以这个坐标系做参照(plotPexil  除外)
# 绘制接口
Text(Point(1, 3), " Celsius Temperature:").draw(win)
#Text(anchorPoint, string) 对象：  以anchorPoint 点的位置为中心， 构建了一个内容为string 的文本对象。
#draw(aGraphWin)  在指定的窗口中绘制对象。
Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
input = Entry(Point(2, 3), 5)# graphics 库中Entry()只能先定义位置，在放入文本
#Entry() 对象：在某处设置一个长为5 的文本框，用于获取键盘输入
#Entry() 对象与Text() 对象都可以调用setText 和getText 方法，区别是Entry 可以被用户修改
input.setText("0.0")#setText() 设置文本对象的内容
input.draw(win)
output = Text(Point(2, 1), "")
output.draw(win)
button = Text(Point(1.5, 2.0), "Convert It")
button.draw(win)
Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
# 鼠标不点击不会往下执行
win.getMouse()#getMouse() 程序等待用户在窗口内点击鼠标， 返回值为点击处的位置， 并以Point 对象返回。
# 转换输入
celsius = eval(input.getText())
#getText() 返回当前文本内容
fahrenheit = 9.0 / 5.0 * celsius + 32.0
# 显示输出，改变按钮
output.setText(fahrenheit)
button.setText("Quit")
# 等待响应鼠标点击，退出程序
win.getMouse()
win.close()#关闭屏幕上的窗口