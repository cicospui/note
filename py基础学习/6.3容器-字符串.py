# 1.字符串的定义
"""
字符串是字符的容器,每个字符串可以放任意数量的字符
允许正、逆向地索引
同元组,是一种无法修改的容器,修改、移除、追加字符都无法完成。
但可以通过创建新的字符串完成
"""
# 字符串允许正逆向地索引
my_str = "itheima and itcast"
print(f"i want find H by anti method {my_str[-16]} & normal method {my_str[2]}")
# my_str[2] = 'H'   会异常
value = my_str.index("and")
print(value)

# 2.字符串的替换
"""
字符串.replace(字符串1,字符串2)
将字符串的全部字符串1替换为字符串2;但不是修改,而是得到了新的字符串！
"""
new_str = my_str.replace("it","程序")
print(f"修改之后原字符串为:{my_str},类型为{type(my_str)}\n新字符串为:{new_str},类型为{type(new_str)}")

# 3.字符串的分割
"""
字符串.split(分隔符字符串)
按照指定的分隔符来分割字符串,将字符串划分为了多个字符串,并存入了列表对象中.
字符串本身不变,得到了新的列表对象
"""
my_str = "hello python itheima itcast"
res = my_str.split(" ")
print(f"分割the result is {res},the type is {type(res)}")

# 4.字符串的规整
"""
1) 去前后空格:          字符串.strip()      去掉空格换行符分隔符等,以形式统一
2) 去前后指定字符串:    字符串.strip(字符串)    实际是按单个字符去除字符串内的字符

"""
my_str = "  itheima and itcast  "
res_4_1 = my_str.strip()
print(f"result is {res_4_1},the type is {type(res_4_1)}")
my_str = "12 itheima and itcast 21"
res_4_2 = my_str.strip("12")
print(f"result is {res_4_2},the type is {type(res_4_2)}")

# 5.字符串相关操作
"""
统计某字符串出现的次数:     count()
统计长度:                  len()
"""
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"it in {my_str} have {count} times")
print("my_str length is",len(my_str))

# 6.字符串的遍历(for & whlie)略

# 练习案例
test_str = "itheima itcast boxuegu"
count = test_str.count("it")
print(f"str it have appeared {count} times")
replace = test_str.replace(" ","|")
print(f"after replace, new str is {replace}")
split = replace.split('|')
print(f"after split, result is {split}")
