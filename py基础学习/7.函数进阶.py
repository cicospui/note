# 1.函数的多返回值
"""
若写两个return,函数只会执行第一个return语句.
若返回多个返回值,则为:
return 1,2,3,
"""
def test_return():
    return 1,2,3

x,y,z = test_return()
print(x,y,z)

# 2.函数参数形式
"""
1)  位置参数    根据参数前后位置传入参数,一般的传参方法
2)  关键字参数  通过"键 = 值"形式传参,也可以和位置参数混用,但此时位置参数要放最前
3)  缺省参数    在函数定义时会定义默认值,若不传参数则使用默认参数
4)  不定长参数  位置传递 *args               作为元组存在,接受的参数是不受限的
                关键字传递 **kwargs         作为字典存在,按照key = value的形式传入
"""

def user_info(name,age,gender = '男'):
    print(f"name is {name},age is {age},gender is {gender}")
user_info("小明",20,'男')       # 1)
user_info(age = 11,name = '小王',gender = '女')     # 2)
user_info('ming',10)    # 3)

def user_info(*args):   # 4.1)数量随意,元组存在
    print(f"args have the type of {type(args)},the content is {args}")

user_info(1,2,3,'ming','qiang')

def user_info(**kwargs):    # 4.2)字典形式存在
    print(f"kwargs have the type of {type(kwargs)},the content is {kwargs}")

user_info(name = 'wang',age = 11,addr = 'beijing')

# 3.函数作为参数传递
"""
之前一直是传入数据作为参数处理的,但实际也可以传入参数来处理
目的是计算逻辑的传递,而非数据的传递
"""
def test_func(compute):
    result = compute(1,2)
    print(result,type(compute))     # 传入的是函数类型

def compute(x,y):
    return x + y

test_func(compute)

# 4.lambda匿名函数
"""
def关键字定义带有名称的函数,基于名称可重复使用
lambda关键字定义匿名函数,只临时使用1次
语法:
lambda 传入参数:函数体(一行代码)
"""
# 同3中功能相同的匿名函数
test_func(lambda x,y:x+y)




