# 1.字典的定义
"""
1) 提供一种对应关系,通过key找到value
2) 同集合,使用{}定义,存储元素为键值对
3) 字典的key不可重复,新的覆盖旧的
4) 不可使用下标索引,只可通过key值索引:字典[key] == value
# 定义字典字面量
{key:value, key:value, ······key,value}
# 定义字典变量
变量名称 = {key:value, key:value, ······key,value}
# 定义空字典
变量名 = {}
变量名 = dict()
"""
my_dict = {"san":99,"si":88,"wu":77}
empty_dict = dict()
print(f"{my_dict},type is {type(my_dict)}")
print(f"san's value is {my_dict['san']}")

# 2.字典的嵌套
"""
字典的key和value可以是任意数据类型(key不能是字典)因此是可嵌套的
"""
# 学生成绩
stu_score_dict = {
    "wanglihong":{
        "yuwen":77,
        "shuxue":66,
        "yingyu":33
    },
    "zhoujielun":{
        "yuwen":88,
        "shuxue":66,
        "yingyu":98
    },
    "linjunjie":{
        "yuwen":78,
        "shuxue":57,
        "yingyu":87
    }
}
print(stu_score_dict["zhoujielun"]["yuwen"])    # 嵌套的字典需要双重索引

# 3.字典操作
"""
新增元素    字典[key] = value
更新元素    字典[key] = value   针对已存在的key值
删除元素    字典.pop(Key)       获得并删除指定key的value
清空元素    字典.clear()
获取全部的key       字典.keys()     得到字典中全部的key,用作字典的遍历
统计数量    len(字典)
"""
stu_score_dict["zhangxinzhe"] = {"yuwen":55,"shuxue":66,"yingyu":77}
print(stu_score_dict)
stu_score_dict["zhoujielun"]["yuwen"] = 55
print(stu_score_dict)
zhou = stu_score_dict.pop("zhoujielun")
print(stu_score_dict,zhou)
my_keys = stu_score_dict.keys()
print(my_keys)
# stu_score_dict.clear()
# print(stu_score_dict)

# 4.字典的遍历
"""
一种根据取出所有key来遍历
一种直接在字典内遍历
不可用while循环
"""
for key in my_keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{stu_score_dict[key]}")

for key in stu_score_dict:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{stu_score_dict[key]}")

print(f"the num is {len(stu_score_dict)}")

# 案例练习
yuangongtable = {
    "王力宏":[ "科技部",3000,1],
    "周杰伦":[ "市场部",5000,2],
    "林俊杰":[ "市场部",7000,3],
    "张学友":[ "科技部",4000,1],
    "刘德华":[ "市场部",6000,2]
    }
def levelup(dict):
    for name in yuangongtable:
        if yuangongtable[name][2] == 1:
            yuangongtable[name][2] += 1
            yuangongtable[name][1] += 1000

print(f"原工资为:{yuangongtable}")
levelup(yuangongtable)
print(f"涨工资后:{yuangongtable}")