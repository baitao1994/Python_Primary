#课后练习
def main():
    fileName = input('Please enter a file:').strip()
    infile = open(fileName,'r')
    list1 = []
    for line in infile:#相当于readline()
        for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.lower()
            line = line.replace(ch,' ')
            #这里必须是line = ,因为line是个不可变量，如果不赋值，还是原来的
        list1.extend(line.split())
    infile.close()
    #str.lower()和str.replace()都只能是字符串操作    

    words ={}
    for i in list1:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    list2 = [[x,y] for (y,x) in words.items()]
    list2.sort(reverse = True)

    k = 10
    for i in range(k):
        print(list2[i][1],'\t',list2[i][0])

def main2():
    fileName = input('Please enter a file:').strip()
    infile = open(fileName,'r')
    file = infile.read()#read()函数是返回字符，包括空格,相当于把原文搬过来
    #readlines()是返回一个列表
    file = file.lower()
    for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
        file = file.replace(ch," ")
    list1 = []
    list1.extend(file.split())
    infile.close()

    words ={}
    for i in list1:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    list2 = [[x,y] for (y,x) in words.items()]
    #Dictionary.items()返回的是dict_items,格式为:(( , ),( , ))而非(( : ),( : ))
    list2.sort(reverse = True)

    k = 10
    for i in range(k):
        print(list2[i][1],'\t',list2[i][0])
    
if __name__ == '__main__':
    main2()
