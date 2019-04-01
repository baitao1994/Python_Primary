import math
def main():
    print('This program finds the real solutions to a quadratic.\n')
    try:
        a,b,c = eval(input("Please enter the coefficients(a,b,c):"))
        discRoot = math.sqrt(b*b - 4*a*c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
    except ValueError as excObj:
        if str(excObj) == 'math domain error':
            print('No Real Roots.')
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:#包括eval()函数，里面必须是字符串
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form.Missing comma?")
    except:
         print("There's no error")
    else:
        print('\nThe solutions are:',root1,root2)#如果try无异常，就执行else语句
    finally:
        print('Always executing the final clause')#不管程序有无异常都执行finally这步
        
main()
