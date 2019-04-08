#TempConcert.py
val = input("请输入待温度表示符号的温度值（例如：32C）：")
if val[-1] in ['C','c']:
    f = 1.8 * eval(val[0:-1]) + 32 # eval()是返回 表达式 的值，表达式可以是值也可以是字符串，可int也可以是float
    print("转换后的温度为：%.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) -32)/1.8 # 将整数或字符串转化为浮点数
    print("转换后的温度为：%.2fC"%c)
else:
    print("输入有误")
