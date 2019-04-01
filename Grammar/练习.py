from math import *
def main1():
    try:
        a,b,c = eval(input("请输入三个系数（a,b,c）"))
        d = b*b - 4*a*c
        if d >= 0:
            root1 = (-b + sqrt(d)) / (2 * a)
            root2 = (-b - sqrt(d)) / (2 * a)
            print("根为",root1,root2)
        else:
            print("没有实数根")
    except SyntaxError:
        print("\nYour input was not in the correct form.Missing comma?")
    except NameError:
        print("\nYou didn'enter three coefficients")
    else:
        print("Finish")
            
    
def main2():
    for n in range(2,10):
        if n % 2 == 0 :
            print("基数")
        else:
            print("偶数")

def main3():
    t, l = eval(input("Enter your weight and stature(kg/m)"))
    BMI = t / (l * l)
    if BMI < 18.5:
        a = "偏瘦"
    elif BMI < 25:
        a = "正常"
    elif BMI < 30:
        a = "偏胖"
    else:
        a = "肥胖"
    if BMI < 18.5:
        b = "偏瘦"
    elif BMI < 24:
        b = "正常"
    elif BMI < 28:
        b = "偏胖"
    else:
        b = "肥胖"
    print("您的BMI为{},国内BMI建议为{},国际BMI建议为{}".format(BMI, a, b))

        
main3()
