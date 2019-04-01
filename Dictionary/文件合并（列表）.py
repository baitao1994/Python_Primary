#思路：将两个文件分别存到两个列表中，建立一个新列表存放合并后的数据，再将新列表存储到文件中
#关键步骤：遍历列表1的人，将信息创建在列表3中，遍历列表2中的人，将剩余人的信息也加到列表3中
def main():
    ftele1=open('TeleAddressBook.txt','rb')
    ftele2=open('EmailAddressBook.txt','rb')
 
    ftele1.readline()#跳过第一行，readline()是读一行，返回字节，并跳转到下一行
    ftele2.readline()#readline(5)表示返回前5个字节
    lines1 = ftele1.readlines()#读所有行
    lines2 = ftele2.readlines()
 
    list1_name = []  
    list1_tele = []
    list2_name = []  
    list2_email = []
 
    for line in lines1:#获取第一个文本中的姓名和电话信息
        elements = line.split()#返回一个列表，默认为在空格、换行(\n)，制表符(\t)处切片
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))    #将文本读出来的bytes转换为str类型
 
    for line in lines2:#获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))#因为是中文文本，所以在读取的时给他解码，防止乱码
        list2_email.append(str(elements[1].decode('gbk')))
 
    ###开始处理###
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')
 
    #按索引方式遍历姓名列表1
    for i in range(len(list1_name)): 
        s= ''
        if list1_name[i] in list2_name:
                j = list2_name.index(list1_name[i]) #找到姓名列表1对应列表2中的姓名索引位置
                s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
                #对于列表来说，index()函数用于从列表中找出某个值索引位置
                #对于字符串来说，index()方法检测字符串中是否包含子字符串>>>str.index(str, beg=0, end=len(string))
                s += '\n'
        else:
                s = '\t'.join([list1_name[i], list1_tele[i], str('   -----   ')])#为什么加str
                s += '\n'
        lines.append(s)
    print(lines)
         
    #处理姓名列表2中剩余的姓名        
    for i in range(len(list2_name)): 
        s= ''
        if list2_name[i] not in list1_name:
                s = '\t'.join([list2_name[i], str('   -----   '), list2_email[i]])
                #join()方法用于将序列(字符串、元组、列表、字典)中的元素以指定的(join前的)字符连接生成一个新的字符串
                #list = ['1','2','3']>>>a = ''.join(list)>>> 结果a是字符串'123'，以空字符连接 
                s += '\n'
        lines.append(s)  #现在的lines是一个包含所有信息的列表
 
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)
    ftele3.close()
    ftele1.close()
    ftele2.close()
 
    print("The addressBooks are merged!")
 
if __name__ == "__main__":
    main()

