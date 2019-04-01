#文件是多行数字组，每行数据以逗号隔开
def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
    #为line中的值更新其count和sum
        for xStr in line.split(","):#以,分割成一列字符串，然后给他们加起来
            sum += eval(xStr)
            count += 1
        line = infile.readline()
    print("\nThe average of the numbers is",sum / count)

#嵌套：外循环：while语句对每一行循环一次，内循环：for语句对一行中每一个数字进行循环

main()
