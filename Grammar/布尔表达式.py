def main():
    a = eval(input("sd [abs]:"))
    #python中只有空字符串""和数字0(不是字符串0)是False
    F = a or "das"
    print(type(F),F)
    
def main2():
    F = "das"and input("sd [abs]") #第一个假就返回第一个，否则返回第二个
    print(F)                        #所以这句会一直返回输入的字符串

main2()


#   x and y     if x is false,return x. otherwise return y

#   x  or y     if x is true,return x.otherwise return y

#   not x       if x is false,return true,otherwise return false
