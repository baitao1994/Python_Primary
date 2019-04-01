#交互式代码
def main():    #缺点：提示太多
    sum = 0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >>"))
        sum += x
        count += 1
        moredata = input("Do you have more numbers (yes or no)?")
    print("\nThe average of the numbers is", sum / count)


def main2():#哨兵循环：空字符串为哨兵
    sum = 0.0
    count = 0
    xStr = input("Enter a number")
    while xStr != "":#空字符串，双引号中间没有空格
        x = eval(xStr)
        sum += x
        count += 1
        xStr = input("Enter a number")
    print("\nThe average of the numbers is",sum / count)

main2()
