from tkinter import *
tk = Tk()
canvas = Canvas(width=500,height=500)
canvas.pack()
#canvas.create_polygon(0,0,250,250,fill = 'red')

def echo_event(evt):
    #打印键盘事件
    if evt.type == "2":
        print("键盘：%s" % evt.keysym)
    #打印鼠标操作
    if evt.type == "4":
        print("鼠标： %s" % evt.num)
    #
    print(evt.type)

#键盘事件
canvas.bind_all("<KeyPress>",echo_event)
#如果绑定指定的键盘，则"<Key>" 或者"<KeyPress>"都可以，具体到指定键的话后面加入下划线和指定的键就好了，如：绑定小写字母t和Left键
canvas.bind_all("<KeyPress-t>",echo_event)
canvas.bind_all("<KeyPress-Left>",echo_event)
#鼠标事件
canvas.bind_all("<Double-Button-1>",echo_event)
canvas.bind_all("<Button-1>",echo_event)
canvas.bind_all("<Button-2>",echo_event)
canvas.bind_all("<Button-3>",echo_event)
mainloop()