#猴子吃桃问题。猴子第一天摘下若干桃子，当即吃掉一半，还不过瘾，又多吃了一个；
#第二天又将剩下的吃了一半，又多吃了一个。以后每天都吃前一天剩下的一半多一个
#第五天吃完后正好剩一个
#问：猴子第一天摘了多少桃子
n = 1
for i in range(5,0,-1): #意思是从列表的下标为5的元素开始，倒序取到下标为0的元素（但是不包括下标为0元素），步长为-1
#range(start, end, step) ，都取不到 end 上的数值
    n = (n+1)<<1 #<<符号是按位左移的意思，就是把对象转为2进制，有效数字往左移动。
    '''
    << 1就是按位左移1个单位。比如2<<1意思就是2按位左移1个单位，2的二进制就是00000010，左移一位就是00000100，转为十进制就是4。
    那么按位左移多少个单位的操作，可以理解为乘以2的多少次方
    '''
print(n)
