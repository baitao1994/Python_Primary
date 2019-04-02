from tkinter import *
import time


def main():
    def sendMsg():  # 发送消息
        strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime()) + '\n '
        # strftime(format, t) 函数接收时间元组，并返回以可读字符串表示的时间，格式由参数format决定
        #t 是struct_time 元组，可由localtime() 和 gmtime() 返回得到，如果未定义 t 则由localtime()返回当地时间
        txtMsgList.insert(END, strMsg, 'greencolor')#给strMsg  添加'greencolor’   标签
        txtMsgList.insert(END, txtMsg.get('0.0', END),'gg')#将输入消息（txtMsg）从头到尾添加到历史消息（txtMsgList）的末尾
        txtMsg.delete('0.0', END) #0.0 表示文本的开始

    def cancelMsg():  # 取消消息
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):  # 发送消息事件
        if event.keysym == "Up":
            sendMsg()

    # 创建窗口
    t = Tk()
    t.title('与python聊天中')# 这里可以交互识别

    # 创建frame容器
    frmLT = Frame(width=500, height=320, bg='white')
    frmLC = Frame(width=500, height=150, bg='white')
    frmLB = Frame(width=500, height=30)
    frmRT = Frame(width=200, height=500)

    # 创建控件：“控件类型“+“功能”
    txtMsgList = Text(frmLT)  #定义历史消息，frmLT表示Text文件的父容器/父窗口
    txtMsgList.tag_config('greencolor', foreground='blue')  # 创建并配置标签，tag_config()配置标签的样式；tag_add()是添加标签
    #上句意思：设置greencolor 为蓝色，“greencolor”是变量，“blue"是值
    txtMsgList.tag_config('gg', foreground='green')
    txtMsg = Text(frmLC);#定义输入消息
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)#绑定响应事件
    btnSend = Button(frmLB, text='发 送', width=8, command=sendMsg)
    btnCancel = Button(frmLB, text='取消', width=8, command=cancelMsg)
    imgInfo = PhotoImage(file="python.gif")#可以看成读取图片，将图片转为程序能识别的数据，python中能读gif 格式
    lblImage = Label(frmRT, image=imgInfo)#创建标签，并将图片放入标签中
    lblImage.image = imgInfo#

    # 窗口布局，columnspan选项可以指定控件跨越多列显示，即控件占据的列宽
     #而rowspan选项同样可以指定控件跨越多行显示，所占行数
    frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
    frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
    frmLB.grid(row=2, column=0, columnspan=2)
    frmRT.grid(row=0, column=2, rowspan=2, padx=2, pady=3)
    # 固定大小
    frmLT.grid_propagate(0)#这句就是固定控件的大小
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

#将这些控件装入其父容器
    #tkinter 库要求创建的每一个控件如：Text（frmLT）都要有父容器，但还未打包放入父容器，因此需要用到函数pack（）或grid（）
    btnSend.grid(row=2, column=0)
    btnCancel.grid(row=2, column=1)
    lblImage.grid()#无参数：默认放到0行0列
    txtMsgList.grid()
    txtMsg.grid()

    # 主事件循环
    t.mainloop()


if __name__ == '__main__':
    main()
