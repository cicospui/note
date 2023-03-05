# 1.py函数介绍
"""
是组织好的，可重复使用的，实现特定功能的代码块
提升程序复用性，提升了效率。
"""
name = "itheima"
length = len(name)
print(length)
str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1
print(f"str1 length is {count}")
count = 0
for i in str2:
    count += 1
print(f"str2 length is {count}")
count = 0
for i in str3:
    count += 1
print(f"str3 length is {count}")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"{data}长度为{count}")

my_len(str1)
my_len(str2)
my_len(str3)    

# 2.函数定义
"""
def 函数名(传入参数):
    函数体
    return 返回值
函数定义后，需要调用函数才有用。
函数名(传入参数)
参数和返回值若不需要均可以省略
"""
def say_hi():
    print("hello!")

say_hi()

# 3.函数的参数
"""
传入参数：函数计算时接受外部提供的数据。
不同参数用,分割
形式参数：函数声明将要使用2个参数
实际参数：函数执行时真正使用的参数值
函数可以没有参数、也可以有N个参数
"""
def add(x,y):
    result = x + y
    print(f"{x}+{y}={result}")
    
add(4,5)

def temptest(temp):
    print(f"ur temp is {temp}")
    if temp >37.5:
        print("需要隔离")
    else:
        print("正常，请进")
print("welecome to heima, pls test ur tamp:")
temp = float(input())
temptest(temp)

# 4.函数返回值
"""
将函数中的结果返回给函数调用者：变量 = 函数（参数）
若无return,也是有返回值的,等价于return None
函数的返回值是None,即返回了无意义的值。
if判断中,None等同于False.
"""
r = say_hi()
print(f"r的值为{r},类型是{type(r)}")

# 5.函数说明文档
"""
def func():
    注释说明
    函数体...
"""
def func():
    """
    这是测试用的函数说明文档
    鼠标悬停在函数时会显示该文档
    """
    return 0

m = func()

# 6.函数的嵌套调用
"""
一个函数里调用了另一个函数
"""
def fun_b():
    print("2")

def fun_a():
    print("1")
    fun_b()
    print("3")

fun_a()    

# 7.变量作用域
"""
变量的作用范围:全局变量和局部变量
局部变量:在函数体内部，临时保存数据，调用完成后销毁。
全局变量:全局都可以用
在函数内部对全局变量的修改不带出函数外，相当于在函数内又建立了一个全局变量的分身
若要实现函数内部将全局变量更改，则需要在变量前加global
"""
num1 = 200
num2 = 300
def text():
    global num2
    num1 = 500
    num2 = 600
    print(f"text:num1={num1},num2={num2}")
text()
print(f"extra:num1={num1},num2={num2}")

# 8.综合案例
#黑马ATM
money = 5000000
name = "jay"
def check_count():
    print(f"count:{money }")

def input_money(num):
    global money
    money += num
    check_count()

def output_money(num):
    global money
    money -= num
    check_count()






