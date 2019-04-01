def main():
    n = eval(input('How many numbers are there?'))
    max = eval(input("Enter a number"))
    for i in range(n-1):
        x = eval(input("Enter a number"))
        if x > max:
            max = x
    print("The maximum is:",max)#这句放在循环里：输入一个数打印一次当前最值
    #如果放在循环外面，就是将所有的数都输入后打印它们的最值

main()

'''还有一种方法：利用Pyhon自带的 max()函数：
def main()
    x1, x2, x3 = eval(input("输入三个数（a, b, c）:"))
    print("最值为：",max(x1, x2, x3))
main()
'''
