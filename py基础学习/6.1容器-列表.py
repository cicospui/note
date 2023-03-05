# 1.数据容器
"""
数据容器可以容纳多份数据。
是一种可以容纳多份数据的数据类型，每1份数据称为1个元素
每一个元素可以是任意类型的数据：字符串、数字、布尔
共有5类数据容器：列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)
"""

# 2.list的定义
"""
# 字面量
[元素1、元素2、元素3、······]
内部可以是任意数据类型
# list变量
变量名 = [元素1、元素2、元素3、······]

# 定义空list
变量名 = []
变量名 = list()
"""
name_list = ['itheima',666,True]
print(name_list)
print(type(name_list))

# 嵌套列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))

# 3.list索引
"""
列表的下标索引可以取出特定位置的元素，自0始
也可以反向索引：最后一个为-1，向前逐个减一。
嵌套列表的索引：如列表[1][0]
"""
test_list = ["Tom","Lily","Rose",["bro1","bro2"]]
print(test_list[0])
print(test_list[-1])
print(test_list[-1][1])

# 4.list常见操作
"""
查询下标:       列表.index(元素)            返回其下标
插入:           列表.insert(下标,元素)      在指定下标位置插入元素
追加单个元素:   列表.append(元素)            将指定元素添加到最后位置
追加多个元素:   列表.extend(其他数据容器)     将其他数据容器的内容取出，依次追加到列表尾部。
删除:           1.del 列表[下标]            仅删除
                2.列表.pop(下标)            返回值为删除的元素
                3.列表.remove(元素)         删除元素在列表中的第一个匹配项
                4.列表.clear()              清空整个列表
修改：          列表[下标] = 新值
统计元素个数:   列表.count(元素)             返回该元素个数
统计:           len(列表)                   统计列表内的元素个数

普通函数是封装的代码块
若函数是类(class)的成员，则函数称为：方法
"""
print(test_list.index("Rose"))
test_list.insert(1,"best")
print(test_list)
test_list.append("append_word")
print(test_list)
test_list.extend(my_list)
print(test_list)
del test_list[-1]
print(test_list)
r = test_list.pop(1)
print(test_list,r)
test_list.remove("Rose")
print(test_list)
test_list.clear()
print(test_list)

my_list = [1,2,3,4,3,2,2]
print(my_list.count(2))
print(len(my_list))

# 5.list的遍历
"""
while遍历框架:
    index = 0
    while index < len(列表):
        元素 = 列表[index]
        元素处理操作
        index += 1

for遍历框架:
    for 临时变量 in 数据容器:
        元素处理操作

对比:
for更简单,while更灵活
for用于容器内依次取出元素,while适用于任何循环    
"""
def list_while_func():
    my_list = ["111","222","333"]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

list_while_func()

def list_for_func():
    my_list = ["111","222","333"]
    for element in my_list:
        print(element)

list_for_func()

# 练习
test_list = [1,2,3,4,5,6,7,8,9,10]
def while_func(list):
    i = 0
    res = []
    while i < len(list):
        if list[i] % 2 == 0:
            res.append(list[i])
        i += 1
    print(f"this is result by while func:{res}")

def for_func(list):
    res = []
    for i in list:
        if i % 2 == 0:
            res.append(i)
    print(f"this is result by for func:{res}")

while_func(test_list)
for_func(test_list)

