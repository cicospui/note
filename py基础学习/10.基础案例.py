# 1.json数据格式
"""
json是带有特定格式的字符串,是一个在各个编程语言中流通的数据格式,负责数据在不同编程语言的传递与交互
如c语言没有字典格式,则需要json作为中转站
json可以视为python的列表,内部是一个个字典
导入json模块后,准备好符合json格式的python数据
json.dumps(data)可以将python数据转换为json数据
json.loads(data)将json数据转换为python数据

"""
import json
data = [{"name":"zhangdasan","age":11},{"name":"lisi","age":14},{"name":"wangwu","age":15}]
json_str = json.dumps(data)
print(type(json_str))
print(json_str)

s = '[{"name": "zhangdasan", "age": 11}, {"name": "lisi", "age": 14}, {"name": "wangwu", "age": 15}]'
l = json.loads(s)
print(type(l))
print(l)

# 2.数据可视化
"""
使用到pyecharts模块
对生成图也需要进行全局配置set_global_opts和系列配置

"""
from pyecharts.charts import Line
# 得到折线图对象
line = Line()
# 添加x,y轴数据
line.add_xaxis(["china","US","English"])
line.add_yaxis("GDP",[30,20,10])
# 画图
line.render() # 生成html文件,用浏览器打开即可

# 3.数据处理
"""


"""
# 准备地图对象
from pyecharts.charts import Map
map = Map()
# 准备数据
date = [
    ("北京",99),
    ("上海",199),
    ("湖南",299),
    ("台湾",199),
    ("安徽",299),
    ("广东",399),
    ("湖北",599)
] 
# 添加数据
map.add("地图",data,"china")
# 绘图
map.render()









