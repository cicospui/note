import random

# 6.封装
"""
将现实世界的事物封装到程序中的类和对象
但也有私有的、不公开的变量/方法:私有成员变量/方法,以__开头
私有成员/变量无法被类对象使用,但可以被类中的其他的成员变量使用
可以理解为是类内部处理时使用的东西
"""

class Phone:

    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足以使用5g通话,已切换至单核运行")
phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)    均会报错,因为类对象无法使用私有成员
phone.call_by_5g()

# 案例
class Phone:
    __is_5g_enable = True
    IMEI = None     #序列号
    producer = "HM" #厂商
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g turn on")
        else:
            print("5g turn off,4g turn on")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

test = Phone()
test.call_by_5g()

# 7.继承基础
"""
基于旧的类修修改改实现新的功能,继承类里只需要写新的东西
语法为:
单继承
class 类名(父类名):
    类内容体
多继承
class 类名(父类1,父类2,......父类N):
    类内容体

"""
class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g_2022(self):
        print("2022新功能")

p = Phone2022()
print(p.producer)
p.call_by_5g_2022()

class NFCreader:
    nfc_type = "第五代"
    producer = "NFC厂商"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteCantrol:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")

class MyPhone(Phone2022,NFCreader,RemoteCantrol):   # 多继承时,遇到同名的变量/方法，按先继承的使用
    pass # 无实际用处,只是由于其他类的功能完善,子类不需要添加东西但需要写点什么就写pass

iphone = MyPhone()
iphone.call_by_5g_2022()
iphone.read_card()
iphone.control()
print(iphone.producer)

# 8.复写和调用父类成员
"""
复写
子类继承父类的成员属性与方法后,若要修改,可以对其进行复写
复写过程只需在子类中对其重新定义即可
调用
若复写后需要在类中调用父类成员/方法时,可以:
    1.父类名.成员变量/成员方法(self)
    或者2.super()成员变量/成员方法()

"""
class MyPhone1(MyPhone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式,确保通话省电")
        print("使用5g通话")
        print("关闭CPU单核模式,确保性能")

p1 = MyPhone1()
p1.call_by_5g()
print(p1.producer)      # 复写成功

# 9.变量的类型注解
"""
用来变量类型的注解与函数(方法)形参列表和返回值的类型注解
语法为:     变量:类型
特殊的,也允许在注释中进行类型注解
"""
# 变量注解
var_1 : int = 10
var_2 : float = 3.1415926

# 类对象注解
class Student:
    pass
stu : Student = Student()

# 容器注解，可以简易注解与详细注解
my_list : list[int] = [1,2,3]
my_tuple : tuple[str,int,bool] = ("itheima",666,True)
my_set : set[int] = {1,2,3}
my_dict : dict[str,int] = {"itheima":666}

var_3 = random.randint(1,10)    # type : int

# 函数注解:参数和返回值注解 
def add(x:int,y:int):
    return x + y

def func(data:list)->list:
    return data

# 10.union
"""
当需要注解不同类型时,则需要通过union类型
不仅可以用来注解变量,也可以注解函数等
需要先导入Union
语法为:Union[类型,类型......类型]
"""
from typing import Union

my_list: list[Union[int,str]] = [1,2,"itheima","itcast"]

def func(data: list[Union[int,str]]) -> Union[int,str]:
    pass

func(6)

# 11.多态
"""
指多种状态。完成某个行为时使用不同的对象从而得到不同的状态
实现为:
以父类做定义声明,以子类做实际工作,获得同一行为的不同状态

父类和父类中的方法是空实现,父类决定有哪些方法,子类自行实现具体如何实现
抽象方法:方法体是空实现(pass)的方法
抽象类:含有抽象方法的类称为抽象类
"""
class Animal:       # 抽象类,一般由子类实现功能.
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)






