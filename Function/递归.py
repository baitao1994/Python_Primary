#递归函数：在函数的定义中使用函数自身
#构造递归函数，需要基例，基例不进行递归，否则递归会一直进行


   #  阶乘
def fact(n):
    if n == 0:#基例
        return 1
    else:
        return n * fact(n - 1)

# 字符串翻转
def reverse(s):
    if s == "":#基例
        return s
    else:
        return reverse(s[1:]) + s[0]#字符串第二个往后翻转 + 第一个

print(fact(100))
