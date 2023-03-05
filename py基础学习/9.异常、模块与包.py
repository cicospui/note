# 1.异常的概念
"""
错误 = BUG = 异常
"""
# 打开不存在的文件就是BUG,如下
# f = open('abd.txt','r',encoding = 'UTF-8')

# 2.异常捕获
"""
作用是提前假设可能出现的异常,做好准备,若真的出现异常,则留有后手。
"""
# 基本捕获语法
try:
    f = open('pylearning/不存在的文件.txt','r',encoding='UTF-8')
except:
    print("出现异常,文件不存在,改为w模式打开文件")
    f = open('pylearning/不存在的文件.txt','w',encoding='UTF-8')
# 捕获指定异常
try:        #一种异常
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print("异常为:",e)

try:        # 多种异常的情况
    1 / 0
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义的异常或除以0的异常")
    print("异常为:",e)

try:        # 所有都可能异常-顶级的异常Exception
    1 / 0
    print(name)
except Exception as e:
    print("出现了异常")
    print("异常为:",e)
else:       # 若没有异常,执行
    print("好高兴,没有异常")
finally:    # 无论如何,都要执行
    print("有无异常,我都运行")
    f.close()

# 3.异常的传递
"""
异常会因为函数的互相调用而传递下去.即使本身无异常,若调用含异常的函数则本身也会异常.
由于异常的传递性,允许不进入最底层来捕获异常,在高层就可以try捕获异常.
"""

# 4.模块导入方法
"""
以.py结尾的python代码文件,能定义函数、类、变量,也可以包含可执行代码
语法为:[from 模块名] import [模块/类/变量/函数/*] [as 别名]     
*表示全部功能都要导入,区别在于前者用.调用某个功能,*直接可以用功能名实现功能.
使用时为:模块名.功能名()    通过.可以利用模块里的所有功能.
"""
import time     # 有一个time.py文件
from time import sleep 
print("nihao")
# time.sleep(5)
print("wohao")

from time import *
print("*")
# sleep(10)
print("*")

# 5.自定义模块
"""
只需创建.py文件然后在其他py文件中import即可
当传入不同模块的同名功能时,该功能会优先按后导入的执行

"""
def test(a,b):
    print(a + b)
if __name__ == '__main__':      
    # 在本文件运行时,内置的变量__name__会被赋值为__main__,从而运行if内的语句
    # 若在其他文件中导入该模块,__name__变量不会这样赋值,则不会运行if内的语句
    test(1,2)

# __all__ 变量,在其他文件中使用from xxx import *导入时,会导入该变量
# 如果在模块中定义了 __all__ = ['某函数']时,*不再导入全部函数,而是__all__中的函数/功能,但不影响手动导入函数

# 6.python包
"""
python模块太多会导致混乱,可以通过Py包来管理多个模块文件
物理上看,包是个文件夹,在文件夹下包含了一个__init__.py文件,该文件夹可用于包含多个模块文件.
逻辑上看,包的本质依然是模块.

导入包时通过import 包名.模块名
使用对应目标时则为: 包名.模块名.目标

也有第三方创建的包
"""
# import my_utils.str_util
# my_utils.str_util.func()

# 案例
"""
使用自己创建的包my_utils
"""
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima",0,4))

file_util.append_to_file("pylearning/text.txt","itheima")
file_util.print_file_info("pylearning/text.txt")

file_util.print_file_info("pylearning/unexist.txt")











