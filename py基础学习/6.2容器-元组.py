# 1.元组
"""
元组可放任意类型的元素
列表可修改，而元组不可修改。可以视为只读的列表。
定义:
# 定义元组字面量
(元素1,元素2,元素3,······)
# 定义元组变量
变量名称 = (元素1,元素2,元素3,······)
# 定义空元组
1) 变量名称 = ()
2) 变量名称 = tuple()
"""

t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(t1,t2,t3)

# 元组若只含一个元素，必须在定义中,后放一个空格，否则会变为原类型！！！
t4 = ("hello")
t5 = ("hello", )
t6 = (12345)
print(type(t4),type(t5),type(t6))

# 元组的嵌套
t7 = ((1,2,3),(4,5,6))
print(t7,type(t7))

# 由下标索引出内容
print(t7[1][2])

# 2.元组相关操作
"""
由于是特殊的列表,操作相较列表比较有限
index()     查找某个数据,返回对应下标
count()     统计某个元素在当前数组出现的次数
len(元组)   统计元组内元素个数
"""

t1 = ("112","223","334")
index = t1.index("223")
num = t1.count("223")
print(index,num,len(t1))

# 3.元组的遍历
"""
# while框架
index = 0
while index < len(tuple):
    do something
    index += 1
#for框架
for element in tuple:
    do something
"""

# 4.修改元组
"""
元组的内容不可修改,会报错
元组内若包含有列表,列表内容可修改
"""
t1 = (1,2,["heima","itcast"])
t1[2][1] = "best"
print(t1)

# 案例
test_tuple = ("Jay",11,["football","music"])
print(f"年龄下标的位置为：{test_tuple.index(11)}")
print(f"学生姓名为:{test_tuple[0]}")
del test_tuple[2][0]
test_tuple[2].append("coding")
print(f"the final result:{test_tuple}")




