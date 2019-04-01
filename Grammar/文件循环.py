#文件循环 
def main():#for循环模式
    fileName = input("What file are the numbers in?" )#输入的格式？文件名.XXX
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    for line in infile:#变量line遍历文件的每一行
        sum += eval(line) #不能有空行，有的话不能返回值，直接报错
        count += 1
    print("\nThe average of the numbers is",sum / count)

def main2():# 哨兵循环模式
    fileName = input('What file are the numbers in?')
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()# readline()函数依行读取，每次读取一行；返回的是一个字符串对象
    while line != "":#空字符串为哨兵
        sum += eval(line)
        count += 1 #处理每一行
        line = infile.readline()
    print("\nThe average of the numbers is",sum / count)

    
main2()

'''在文本文件中，空行包括一个换行符
因此readline()返回的是 \n 而不是 ""
因此，在 while line != "": 这句中，遇到空行依然执行，但在本程序中不能有空行
因为eval()只能将字符串返回成值，不能返回 \n
'''
