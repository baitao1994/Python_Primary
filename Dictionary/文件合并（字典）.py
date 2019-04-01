#利用字典将两个通讯录文本合并为一个文本
def main():
        ftele1=open('TeleAddressBook.txt','rb')
        ftele2=open('EmailAddressBook.txt','rb')
 
        ftele1.readline()
        ftele2.readline()
        lines1 = ftele1.readlines()
        lines2 = ftele2.readlines()
 
        dic1 = {}   
        dic2 = {}
 
 
        for line in lines1:
                elements = line.split()
                dic1[str(elements[0].decode('gbk'))] = str(elements[1].decode('gbk'))
                #将中文文本读出来的bytes转换为str类型
                 
        for line in lines2:
                elements = line.split()
                dic2[str(elements[0].decode('gbk'))] = str(elements[1].decode('gbk'))
 
        lines = []
        lines.append('姓名\t    电话   \t  邮箱\n')
 
        for key in dic1:
            s= ''
            if key in dic2.keys():
                    s = '\t'.join([key, dic1[key], dic2[key]])
                    s += '\n'
            else:
                    s = '\t'.join([key, dic1[key], str('   -----   ')])
                    s += '\n'
            lines.append(s)
             
        for key in dic2:
            s= ''
            if key not in dic1.keys():
                    s = '\t'.join([key, str('   -----   '), dic2[key]])
                    s += '\n'       
            lines.append(s)
 
        ftele3 = open('4.txt', 'w')
        ftele3.writelines(lines)
 
        ftele3.close()
        ftele1.close()
        ftele2.close()
        print("The addressBooks are merged!")
 
if __name__ == "__main__":
        main()
