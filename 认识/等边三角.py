'''from turtle import *

def main():
    setup(1200, 500, 0, 0)
    length = 120
    width = 2
    pensize(width)
    pencolor("black")
    seth(0)
    fd(length)
    seth(120)
    fd(length)
    seth(240)
    fd(length)

main()
'''
from turtle import *

def drawTriangle(t,len,s):
    for i in range(t):# for 循环语句
        seth(s)#角度转到s，而不是转了s
        fd(len)
        s += 120
def main():
    setup(1200, 800, 0, 0)
    size = 2
    pensize(size)
    pencolor("black")
    drawTriangle(3,120,0)

main()
