from tkinter import *  # 必须有一个父容器

def main():
    tk = Tk()  # 创建一个窗口对象，背景为白色，以屏幕左上角为原点，横坐标右为正，纵坐标下为正
    canvas = Canvas(tk, width=400, height=400)  # 在此窗口里设置画布，tk是按钮的父容器
    canvas.pack()  # 包装，放到主窗口
    # 在画布上创建文字
    canvas.create_text(200, 40, text="welcome to Tkinter", fill="blue", font=("Times", 16))#字体
    # 在画布上创建图片，tkinter只能显示gif文件
    myImage = PhotoImage(file="Python.gif")
    canvas.create_image(100, 70, anchor=NW, image=myImage)  # 以(100,70)为西北角显示图像

    def moverectangle(event):
        if event.keysym == "Up":#event.keysym 是按下的键码，键值
            canvas.move(3, 0, -5)
        elif event.keysym == "Down":
            canvas.move(3, 0, 5)#1 表示对canvas中第几个对象执行此操作，0为横坐标，5 为纵坐标
        elif event.keysym == "Left":
            canvas.move(3, -5, 0)
        elif event.keysym == "Right":
            canvas.move(3, 5, 0)

    canvas.create_rectangle(180, 180, 220, 220, fill="red")  # 创建小矩形，填充颜色
    # 让tkinter监视KeyPress事件，当该事件发生时调用moverectangle函数
    # bind_all 第2个参数是回调函数，不能接收参数传递，所以在函数内部建立回调函数
    canvas.bind_all("<KeyPress-Up>", moverectangle)#bind()响应事件的函数，bind_all()全局响应
    canvas.bind_all("<KeyPress-Down>", moverectangle)
    canvas.bind_all("<KeyPress-Left>", moverectangle)
    canvas.bind_all("<KeyPress-Right>", moverectangle)
    # canvas.unbind("KeyPress")
    mainloop()#主事件循环


if __name__ == '__main__':
    main()
