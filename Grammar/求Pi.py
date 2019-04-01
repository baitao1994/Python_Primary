# pi.py
from random import random
from math import sqrt
from time import process_time
DARTS = 1000000 #这是随机点的次数
hits = 0 #在圆内的点个数
process_time() #计算程序的运行时间
for i in range(1，DARTS):                 # 不理解
    x, y = random(), random()# random()函数： 生成一个[0，1.0)之间的随机小数
    dist = sqrt(x**2 + y**2) # 开方函数，定义为到圆心的距离
    if dist <= 1.0: 
        hits += 1
pi = 4 * (hits/DARTS)
print("Pi的值是 %s" % pi)
print("程序的运行时间为：%-5.5ss" %process_time())
#在1*1的正方形内随机地撒点，点到圆心的距离小于等于1的话就在圆内，在圆内的点
#数除以总点数再乘以4就是圆周率Pi
