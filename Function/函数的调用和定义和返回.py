#return语句：结束函数调用，并将结果返回给调用者
#return语句：程序退出该函数，并返回到函数被调用的地方
def main():
    def add(x):#这里定义add函数，括号中的x是形式参数,x并没被定义
        x += 1#这里x也是形参
        return x#x也是形参                           整个定义函数中的所有变量都是形参
    x = add(1)#这里调用add函数并赋值给x（括号中的1 是已赋值的实际参数），这里的x才第一次被定义
    print(x)

def main2():
    a = input("Please enter teh name of your friend")
    print("Happy Brithday to you!\nHappy Brithday to you!\nHappy Brithday to {}!\nHappy Brithday to you!\n".format(a))



from math import * #计算两点的距离 
def square(x):
    y = x * x
    return y
def main3():
    x1, y1 = eval(input("请输入第一个点的坐标"))
    x2, y2 = eval(input("输入第二个点的坐标"))
    dist = sqrt(square(x1 - x2)+square(y1 - y2))
    print("两点距离为：",dist)


def addInterest1(balance,rate):#计算银行盈利
    newbalance = balance * (1 + rate)
    return newbalance#没有返回值的语句等价于return None,所以没有这句话，最终会输出None
def main4():
    acount = 1000
    rate = 0.05
    Interest = addInterest1(acount,rate)
    print(Interest)
#用列表储存账户信息，计算所有的盈利情况

def addInterest2(balances,rate):
    for i in range(len(balances)):
       balances[i] = balances[i] * (1 + rate)
def main5():
    acounts = [1000,200,3000,4000]#变量是列表，返回修改后的列表
    rate = 0.05
    addInterest2(acounts,rate)
    #改变形参的值并不影响实参的值，如果实参是可变对象（列表和图形），则返回后会的实参呈现修改后的状态
    print(acounts)

main5()
