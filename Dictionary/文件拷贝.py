def main():
    #输入用户文件名
    f1 = input('Enter a souce file:').strip()
    f2 = input('Enter a souce file:').strip()

    #打开文件
    infile = open(f1,'r')
    outfile = open(f2,'w')#创建一个文件

    #拷贝数据
    countLines = countChars = 0
    for x in infile:#遍历每一行,这里的x已经被定义，且x就是文件中的一行 
        countLines += 1
        countChars += len(x)
        outfile.write(x)#拷贝行
    print(countLines, "lines and", countChars, "chars copied")

    infile.close()
    outfile.close()
        
main()
