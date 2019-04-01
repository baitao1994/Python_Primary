#红色五角星

from turtle import *
color("green","red")#color(*args)  Return or set the pencolor and fillcolor.
#color() = pencolor() + fillcolor() 里面必须是字符串
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
