from math import *

def main():
    a,b,c = eval(input('请输入一元二次方程的三个系数'))#想要把输入的几个数分别赋给abc，
                                                       #需要把输入的数用逗号隔开，不然程序不识别
    k = b**2 - 4*a*c
    if k >= 0:
        root1 = (-b + sqrt(k))/(2*a)
        root2 = (-b - sqrt(k))/(2*a)
        print('二次方程的实数解分别为：',root1,root2)#这里加逗号
    else:
        print('该方程不存在实数解')

main()

'''
a = input("随便输入yi个变量") #
b = input('请随便再输入一个变量')
print("返回相同值为:{},{}".format(a,b)) #字符串格式化方法： .format()
'''
