def main():
    for n in range(2,10):# n 在[2，10）遍历，for循环是遍历，而while循环是条件
        for x in range(2,n):
            if n % x == 0:
                print(n,'equals',x,'*',n//x)# //是商的取证，向下取整
                break    #break是结束整个循环
        else:#else后面的表达式在for循环列表遍历完毕后或while条件语句不满足时执行
        # loop fell through without finding a factor 
            print(n,'is a prime number.')

'''
for i in range(2,3):
    print('in  range')
print('not in range')#所以结果为：in  range 和 not in range

'''
def main2():
    for num in range(2,10):
        if num % 2 == 0:
            print("Found an even number",num)
            continue    #continue是结束本次循环之后
        print("Found a number",num)

def main3():
    sum = 0
    num = 0
    while num <= 20:
        num += 1
        sum += num
        if sum > 100:
            break    #我就想知道停止的哪个循环
    print("The number is",num)
    print("The sum is",sum)

main()
'''for / while  else 类似于 try except else
等for/try 执行完毕后，在执行else
'''
