# 1.布尔类型与比较运算符
"""
布尔类型表示真假，比较运算符判断真假。
True、False
比较预算符
== , != , < , > , <= , >=六个
"""
result = 10 > 5
bool_1 = True
bool_2 = False
print(f"10 > 5的结果为{result},bool_1的内容是{bool_1},其类型是{type(bool_1)}")
num1 = 10
num2 = 15
print(f"num1 == num2的结果为{num1 == num2},num1 > num2的结果为{num1 > num2},num1 <= num2的结果为{num1 <= num2}")

# 2.if的基本格式
"""
if 要判断的条件:
    条件成立时的事情
"""
print("欢迎来到游乐场，儿童免费，成人收费")
age = int(input("请输入您的年龄"))
tickt = 10
if age >= 18:
    print(f"今年{age}，您已成年，需补票{tickt}元")
else:
    print(f"今年{age},未成年")
print("have a good time")

# 3.if else语句

# 4.if elif else语句组合使用
"""
if 条件1：
    条件1的事情
elif 条件N：
    条件N的事情
else:
    其他事情
最后的else其实也是可以删除的
"""
height = int(input("请输入您的身高(cm):"))
vip_level = int(input("请输入您的VIP等级(1--5):"))
day = 1

if height < 120:
    print("身高低于120，免费进入")
elif vip_level > 3:
    print("高级会员，免费进入")
elif day == 1:
    print("免费日，请进入")
else:
    print("请付费")

# 5.判断语句的嵌套
"""
if 条件1:
    do something 1
    if 条件2:
        do something 2
"""
print("Welecome LOL!")
if int(input("请输入你的身高：")) > 120:
    if int(input("请输入VIP级别:")) > 3:
        print("尊贵的VIP用户，可以免费")
    print("身高不够，无法进入")
print("小朋友免费进入")

# 6.实战案例-猜数字游戏
import random
num = random.randint(1,10)
guess_num = int(input("你有三次机会，第1次猜："))
if guess_num == num:
    print("congratulation!u just use 1 time")
elif guess_num > num:
    print("bigger!")
else:
    print("smaller!")
guess_num = int(input("你有三次机会，第2次猜："))
if guess_num == num:
    print("congratulation!u have used 2 times")
elif guess_num > num:
    print("bigger!")
else:
    print("smaller!")
guess_num = int(input("你有三次机会，第3次猜："))
if guess_num == num:
    print("congratulation!u have used 3 times")
else:
    print(f"run out,it's {num}!")

