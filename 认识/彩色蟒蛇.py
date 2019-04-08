from turele import *
def drawSnake(rad,angle,len,neckrad):
    colors = ['green','red','blue','yellow','black']
    for i in range(len):
        pencolor(colors[i % 5])
        circle(rad,angle)
        circle(-rad,angle)
    color('pink')
    circle(rad,angle/2)
    fd(rad)
    color('gray')
    circle(neckrad+1,180)
    fd(rad*2/3)
    
def main():
    setup(800,600,0,0)
    pensize(7)
    seth(-40)
    drawSnake(40,80,5,15)
main()
    
