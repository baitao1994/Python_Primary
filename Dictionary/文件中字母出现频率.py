# -*- coding:utf-8 -*-
from turtle import *
count = 10
yScale = 6
xScale = 30
data = []
letters = []
def main():
    filename = input("Please input the filename:").strip()
    with open(filename, 'r') as infile:
        fstring = infile.read()#返回所有字符
        fstring = fstring.lower()
    counters = {}
    characters = 'abcdefghijklmnopqrstuvwxyz'
    for i in characters:
        counters[i] = fstring.count(i)#计算i的次数
        print(i,"\t",counters[i])

    list1 = list(counters.items())
    list2 = [[x,y]for(y,x)in list1]
    list2.sort(reverse = True)
    
    for i in range(0 ,count,1):
       data.append(list2[i][0])
       letters.append(list2[i][1])
    infile.close()

    title('字母频率图')
    setup(900,750,0,0)
    width(3)
    hideturtle()
    color('green')
    drawGraph()
def drawGraph():
    drawLine(0,0,360,0)
    drawLine(0,300,0,0)
    for x in range(count):
        x=x+1 #向右移一位,为了不画在原点上
        drawText(x*xScale-4, -20, letters[x-1])#在(x*xScale-4,-20)处写下word[0]
        drawText(x*xScale-4, data[x-1]*yScale-270, data[x-1])
    drawBar()
def drawLine(x1, y1, x2, y2):
    penup()
    goto (x1, y1)
    pendown()
    goto (x2, y2)
def drawText(x, y, text):
    penup()
    goto (x, y)
    pendown()
    write(text)
def drawBar():
    for i in range(count):
        drawRectangle(i+1, data[i])

def drawRectangle(x, y):
    x = x*xScale
    y = y*yScale - 270#放大倍数显示
    drawLine(x-5, 0, x-5, y)
    drawLine(x-5, y, x+5, y)
    drawLine(x+5, y, x+5, 0)
     
if __name__ == "__main__":
    main()
