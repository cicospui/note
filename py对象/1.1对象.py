# 1. 对象
"""
对应到生活中:
设计表格--设计类
打印表格--创建对象
填写表格--对象属性赋值
"""
# 设计类
class Student1:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
# 创建一个对象
stu_1 = Student1()
# 对象属性赋值
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "China"
stu_1.native_place = "ShanDong"
stu_1.age = 31
# 获取对象中的信息
print(stu_1)

print(stu_1.name,stu_1.gender,stu_1.nationality,stu_1.native_place,stu_1.age)

# 2.类的成员和方法
"""
class 类名称:
    类的属性（定义在类中的成员变量）
    类的行为（写到类中的函数/方法）

对象 = 类名称()     #用来创建一个对象

类中定义方法与外部定义函数有细微差别:
def 方法名(self,形参1,......形参N):
    方法体

self关键字用来表示类对象自身,在方法内部访问类的成员变量必须使用self,调用时传递参数self可以视为不存在
"""
class Student2:
    name = None

    def say_hi(self):
        print(f"i am {self.name},nice to meet u!")

    def say_hi_2(self,msg):
        print(f"hello,i am {self.name},{msg}")      #访问类内的成员要用self

stu_1 = Student2()
stu_1.name = "周杰伦"
stu_1.say_hi()
stu_1.say_hi_2("诶呦不错呦")
stu_2 = Student2()
stu_2.name = "邓紫棋"
stu_2.say_hi()
stu_2.say_hi_2("叽叽叽叽")

# 3.类和对象
"""
现实世界具有事和物两种,对应到代码类中的方法和对象
面向对象编程的核心是设计类、构造对象让其工作
"""
class Clock:
    id = None
    price = None

    def ring(slef):
        import winsound
        winsound.Beep(2000,3000)

clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID为{clock1.id},价格为{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 29.99
print(f"闹钟ID为{clock2.id},价格为{clock2.price}")
clock2.ring()

