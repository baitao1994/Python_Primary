from math import pi,sin,cos,radians
 
'''def main():   
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval: "))
 
    xpos = 0
    ypos = h0
 
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)     
 
    while ypos >= 0:
        xpos = xpos + time * xvel
        yvell = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvell)/2.0
        yvel = yvell
    print("\nDistance traveled:{0:0.1f} meters.".format(xpos))
'''
def main():#上面是程序化思维，这个是模块化
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos,ypos,yvel = updatePosition(time,xpos,ypos,xvel,yvel)
    print("\nDistance traveled : {0:0.1f} meters.".format(xpos))

def getInputs():
    a = eval(input("Enter the launch angle (in degrees):"))
    b = eval(input("Enter the initial velocity (in meters/sec):"))
    c = eval(input("Enter the initial height (in meters):"))
    d = eval(input("Enter the time interval: "))
    return (a, b, c, d)

def getXYComponents(a,b):
    theta = radians(b)
    n = a * cos(theta)
    m = a * sin(theta)
    return (n, m)

def updatePosition(a,b,c,d,e):
    b = b + a * d
    yvell = e - a * 9.8
    c = c + a * (e + yvell)/2.0
    e = yvell
    return (b, c, e)
     
if __name__ == "__main__":
    main()
