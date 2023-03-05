# 1.字面量：六种字面量的数据类型；py中被双引号包围起来的都是字符串。
666
13.14
"黑马程序员"
print(666)
print(13.14)
print("黑马")
# 被写在代码的固定的值称为字面量，常用整数、浮点数、字符串三种；print可以输出字面量。

# 2.注释：单行以#开头，最好和内容隔开一格；多行注释则以三对双引号包围
"""
注释不影响程序。单行注释一般是解释下一行语句，多行注释一般对整个文件或类注释
"""

# 3.变量：存储计算结果或表示值的抽象概念
"""
语法：变量名称 = 变量的值
"""
money = 50
money = money - 10
print("钱包还有",money,"元")

# 4.数据类型
"""
type()可以查看字面量/变量的数据类型
变量没有类型， type()查看的是变量存储的数据的类型。
"""
print(type("黑马"))
print(type(666))
print(type(13.14))
string_type = type("1")
int_type = type(666) 
print(string_type)
print(int_type)
name = "黑马"
print(type(name))

# 5.数据类型转换
"""
int(x)
float(x)
str(x)
"""
num_str = str(111)
print(num_str)
print(type(num_str))
num = int("11")
print(type(num),num)
int_num = int(114.514)
print(type(int_num),int_num)    #丢失小数部分

# 6.标识符
"""
变量的名字、方法的名字、类的名字等
只允许英文中文数字和下划线，数字不可以用于开头
大小写敏感
不可使用关键字
命名规范：通过_连接不同单词，且全小写。
"""
Heima = "heima"
heima = 666
print(Heima,heima)

# 7.运算符
"""
算术运算符：//取整除结果；%取余；**指数
赋值运算符：=或者包含等于的+=等赋值运算符
//= ; %= ; **= 均和+=类似
"""
print("1 + 1 =",1+1)
print("11 // 3 =", 11 // 3)
print("11 % 3 =", 11 % 3)
print("3 ** 2 =", 3 ** 2)

# 8.字符串的定义
"""
包括三种定义方法，若字符串内本身具有某种符号，用另一种符号的定义法。
或使用转义字符\解除引号的作用，作为字符串的内容。
"""
name1 = 'heima'     #单引号
name2 = "heima"     #双引号
name3 = """heima""" #三引号定义法
print(name1,name2,name3,type(name1),type(name2),type(name3))
name4 = "\"黑马"
print(type(name4),name4)

# 9.字符串的拼接
"""
用+拼接
只能适用于字符串类型
用于字面量和变量或变量和变量之间的拼接。
"""
name = "黑马"
adress = "建材城东路"
# tel = 415555555555555
print("我是:" + name +"，我的地址是："+adress)

# 10.字符串的格式化
"""
问题：变量过多，拼接麻烦；字符串无法拼接其他类型。
通过%的方式拼接，可以拼接数字
"""
# 通过占位%的方式拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num,avg_salary)
# %s中，%表示占位，s表示变量转换为字符串放入。%d转换成整数，%f转换成浮点型
print(message)

# 11.字符串格式化的精度控制
"""
辅助符号m.n控制数据的宽度和精度,小数点计入一点宽度。
若m（很少使用）小于自身，不生效；.n负责控制小数点精度，小数部分四舍五入。
"""
d = 11
f = 11.336
print("数字11限制为宽度5，结果为：%5d" % d)
print("数字11.333宽度限制7，小数限制2，结果为：%7.2f" % f)

# 12.字符串格式化2
"""
快速格式化字符串，语法为：f"内容{变量}";
f表示内部需要快速格式化
快速格式化不做类型和精度控制
"""
name = "传播"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name},我成立于{set_up_year},我今年的股价是{stock_price}")

# 13.表达式的格式化
"""
表达式：一条具有明确执行结果的代码语句
"""
print("1*1的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))
# 小练习
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"{name}公司，股票代码：{stock_code},当前股价：{stock_price}")
print(f"每日增长系数：{stock_price_daily_growth_factor}，经过{growth_days}天的增长后")
print("股价达到：%.2f" % (stock_price*(stock_price_daily_growth_factor**growth_days)))

# 14.数据输入input()
"""
input()从键盘获取输入内容，后使用一变量接收内容。
接收的内容统一视作字符串
"""
# print("你是谁？")
name = input("请告诉我你是谁")
print("你是：%s" % name)
num = input("输入一串数字")
print("你输入的数字类型是：",type(num))
print("转换后的类型为：",type(int(num)))    # 可以自行进行类型转换
