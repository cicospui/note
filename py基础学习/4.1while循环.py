# 1.while循环
"""
while 条件:
    do something1,2,3,
"""
i = 1
sum = 0
while i<=100:
    sum += i
    i += 1
print(sum)

# while猜数字
import random
num = random.randint(1,10)
guess = int(input("请输入你要猜的值:"))
i = 1
flag = 1
while flag:
    if guess == num:
        print(f"congratulations! u have used {i} times!")
        flag = 0
    elif guess > num:
        print("bigger!")
        guess = int(input("try again!the number is:"))
    else:
        print("smaller!")
        guess = int(input("try again!the number is:"))
    i += 1
     
# 2.while嵌套循环
"""
while tiaojian1:
    do something
    while tiaojian2:
        do something
"""
i = 1
j = i
while i <= 100:
    print(f"today is {i} days")
    j=1
    while j<=10:
        print(f"give {j} flowers to XiaoMei")
        j += 1
    print("i love u")
    i += 1
print("success!")

# 9*9乘法表
"""
print("hello",end = ' ')可以实现输出不换行
输出对齐：\t用制表符
print("hello \tworld")
print("itheima \tbest")
"""
i = 1
j = 1
while i < 10:
    while j <= i:
        print(f"{i}*{j}={i*j}\t",end = ' ')
        j += 1
    j = 1
    print("\n")
    i += 1    



