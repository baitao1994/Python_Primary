def main1(): 
    fileName = input("Enter the name of the file you want to open")
    infile = open(fileName,'rb')
    for i in range(5):
        line = infile.readline()
        print(line[:-1])#不读换行符，文本文件，空行不是空串，而是\n

def main2():
    outfile = open("2.txt",'w')# 'w'，是写一个文件，如果文件不存在创建一个
    outfile.writelines(["Hello"," ","World"])
    outfile.close()#必须得关掉文件才能将刚刚写的储存进去
    infile = open("2.txt",'r')
    infile.read()

def main3():#遍历文件的所有行的方式
    file = open(someFile,'r')
    for line in file.readlines():
        #执行操作
    file.close()

def main4():
    str = '123456733289212'
    print(str.strip('21'))#strip()函数是除去字符串首尾的特定字符，默认为空格和换行符
    #结果为：3456733289，开头从左往右删，结尾从右往左删
    #只要有1和2 都删掉，但中间的不删
main2()
    
