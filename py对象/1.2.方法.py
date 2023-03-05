# 4.构造方法
"""
更高效方式对对象属性赋值,像传参一样给类赋值,称为构造方法
python中的__init__方法,是为构造方法,其在创建类对象时,会自动执行,也会将传入参数自动传递给__init__方法使用

"""
class student:
    name = None
    age = None
    tel = None
    # 如果写了__init__,上边的成员定义可以省略.
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建了一个对象")

stu = student("老六",66,16666666666)

# 案例
class test:
    def __init__(self,sort,name,age,address):
        self.sort = sort
        self.name = name
        self.age = age
        self.address = address
        print(f"第{sort}位学生信息录入完成,信息为：【学生姓名:{name},年龄:{age},地址:{address}】")

def creat_stu(num):
    for i in range(num):
        print(f"当前录入第{i+1}位同学信息,共需录入{num}位")
        res = test(i+1,input("请输入学生姓名:"),input("请输入学生年龄:"),input("请输入学生地址:"))
        stu.append(res)

stu = []
num = int(input("你想创建几个学生档案？"))
creat_stu(num)

# 5.魔术方法
"""
__init__等方法是Python类内置的方法之一
内置的方法各自有特殊的功能,称为魔术方法,以下是五个常见的
__init__构造方法
__str__字符串方法
__lt__小于、大于符号比较
__le__小于等于、大于等于符号比较
__eq__==符号比较
如果不加入魔术方法,进行比较等行为的时候则是对两个对象object进行的,无法得到正确结果
"""
stu = student("Jay",11,18888888888)
print(stu)
print(str(stu))
# 加入魔术方法后
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("student类创建了一个对象")
    
    # 用来返回时打印正常字符串而非对象的
    def __str__(self):
        return f"student类对象,name:{self.name},age:{self.age}"

    # 用来类对象比较大小时使用,可以设定为任意成员变量的比较，但不适用于小于等于
    def __lt__(self,other):     # other为另一个类对象
        return self.age < other.age

    # 用于小于等于和大于等于时的魔术方法
    def __le__(self,other):
        return self.age <= other.age

    # 用于判断 ==
    def __eq__(self,other):
        return self.age == other.age

jay = student("zhoujielun",31)
lin = student("linjunjie",29)
deng = student("dengziqi",31)
print(lin)
print(str(lin))
print(jay < lin)
print(jay >= lin)
print(jay == deng)




