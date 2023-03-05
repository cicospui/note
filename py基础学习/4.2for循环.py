# 1.for基础语法
"""
for循环是"轮询"机制，对一批内容进行"逐个处理"
for 临时变量 in 待处理数据集:
    循环内的操作
数据集不可能无限大，Python的for不允许无限循环;
临时变量不建议在外部生效
"""
name = "itheima"
count = 0
for x in name:
    if x == 'i':
        count += 1
print(count)        

# 2.range语句
"""
for循环内的“待处理数据集”实际为“序列类型”
序列类型：内容可以一个个依次取出的类型，包括字符串、列表、元组等
range语法:
1.range(num)从0开始到num-1结束
2.range(num1,num2)从num1开始到num2-1结束
3.range(num1,num2,step)从num1开始每次按步长step取,即num1+N*step
"""
for x in range(5,10,2):
    print(x,end = ' ')

# 3.变量作用域
"""
for内的临时变量最好不要拿出来用,想当成全局变量则在外部就定义它.
"""

# 4.for循环嵌套
"""
for x in range1:
    do something1
    for y in range2:
        do something2
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end = '\t')
    print("\n")

# 5.循环中断break&continue
"""
continue:中断本次循环，跳过本次循环的后边部分，直接进行下一次循环；
break:直接结束循环，跳过后边部分；
均且只能影响一层循环，在嵌套循环中对外层的循环不影响
"""
for i in range(1,6):
    print(1)
    for j in range(1,6):
        print(2)
        continue
        print(3)
    print(4)

# 发工资案例
import random
count = 10000
for i in range(1,21):
    if count == 0:
        print("工资发完，下月领取")
        break
    jixiao = random.randint(1,10)
    if jixiao < 5:
        print(f"员工{i},绩效分{jixiao},低于5,不发工资,下一位")
        continue
    count -= 1000
    print(f"员工{i},绩效分{jixiao},发1000元,公司还剩{count}元，下一位")





