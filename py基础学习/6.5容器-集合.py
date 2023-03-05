# 1.集合定义
"""
已有:
列表可修改、支持重复元素且有序
元组、字符串不可修改,支持重复元素且有序
若需要去重操作会有局限性,因此需要集合set定义

# 定义集合字面量
{1,2,3······}
# 定义集合变量
变量名 = {1,2,3······}
# 定义空集合
变量名 = set()
"""
my_set = {"chuanzhi","heima","itheima","chuanzhi","heima","itheima","chuanzhi","heima","itheima"}
empty_set = set()
print(my_set,empty_set) # 自动将集合中的去重且不保证集合顺序

# 2.常用操作
"""
集合无序,因此不支持下标索引访问
添加元素    集合.add(新元素)
移除元素    集合.remove(元素)
随机取出    集合.pop()          返回元素结果,且集合本身被修改,元素被移除
清空集合    集合.clear()
集合差集    集合1.different(集合2)  取出集合1有而集合2没有的
消除相同    集合1.difference_update(集合2)  在集合1内删除与集合2相同的元素
合并集合    集合1.union(集合2)  得到集合1和2组成新集合,但集合1和2不变
统计数量    len(集合)
"""
my_set.add("python")
print(my_set)
my_set.remove("heima")
print(my_set)
res = my_set.pop()
print(res,my_set)
my_set.clear()
print(my_set)
set1 = {1,2,3}
set2 = {1,5,6}
print(set1.difference(set2))
set1.difference_update(set2)
print(set1)
set3 = set1.union(set2)
print(set3,len(set3))

# 3.集合的遍历
"""
集合不支持下标,因此不可以用while遍历,只能用for循环
"""
set1 = {1,2,3,4,5}
for i in set1:
    print(i)

# 案例
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
def list2set(list):
    res = set()
    for i in list:
        res.add(i)
    return res

print(list2set(my_list))

