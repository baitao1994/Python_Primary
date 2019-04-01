# month.py
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = input('请输入月份数（1-12）：')
#变量 = input（）。输入的东西以字符串的形式储存在变量中
pos = (int(n)-1) * 3
monthAbbrev = months[pos:pos+3]#提取字符串的其中几位，[]中必须是整型
print('月份简称为：'+monthAbbrev+'.')

'''week = '一二三四五六七'
a = input('请输入数字（1-7）：')
b = int(a) - 1
print('对应为星期'+week[b])'''
