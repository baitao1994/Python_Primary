# drawtree.py
 
from turtle import Turtle, mainloop
 
def tree(plist, l, a, f):
    """ plist is list of pens
    l is length of branch，分支的长度
    a is half of the angle between 2 branches，镜像，角度为一半
    f is factor by which branch is shortened from level to level. 缩短的比例"""
    if l > 5: #
        lst = []#做个空列表，将几个分支储存进去，一遍下一次递归
        for p in plist:
            p.forward(l)#沿着当前的方向画画Move the turtle forward by the specified distance, in the direction the turtle is headed.
            q = p.clone()#Create and return a clone of the turtle with same position, heading and turtle properties.
            p.left(a) #Turn turtle left by angle units
            q.right(a)# turn turtle right by angle units, nits are by default degrees, but can be set via the degrees() and radians() functions.
            lst.append(p)#将元素增加到列表的最后，此元素可以是字符串、数字、列表等
            lst.append(q)#函数extend()：只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中
        tree(lst, l*f, a, f)
   
            
 
def main():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    #p.setundobuffer(None)
    p.hideturtle() #Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing,
    #because hiding the turtle speeds up the drawing observably.
    #p.speed(10)
   # p.getscreen().tracer(1,0)#Return the TurtleScreen object the turtle is drawing on.
    p.speed(100)
    #TurtleScreen methods can then be called for that object.
    p.left(90)# Turn turtle left by angle units. direction 调整画笔
 
    p.penup() #Pull the pen up – no drawing when moving.
    p.goto(0,-200)#Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
    p.pendown()# Pull the pen down – drawing when moving. 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    #否则turtle一移动就会自动的把线画出来
 
    #t = tree([p], 200, 65, 0.6375)
    tree([p], 200, 65, 0.6375)#看不懂
     
main()

