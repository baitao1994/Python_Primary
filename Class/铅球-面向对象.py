from Projectile import *
 
def getInputs():
    a = eval(input("Enter the launch angle (in degrees):"))
    v = eval(input("Enter the initial velocity (in meters/sec):"))
    h = eval(input("Enter the initial height (in meters):"))
    t = eval(input("Enter the time interval: "))
    return a,v,h,t
 
def main():
    angle,vel,h0,time = getInputs()
    shot = Projectile(angle,vel,h0)#这是类的实例化，会自动调用--init--方法里的属性
    while shot.getY() >=0:
        shot.update(time)#调用类的方法
    print("\nDistance traveled:{0:0.1f}meters.".format(shot.getX()))
   
if __name__ == "__main__":
    main()
