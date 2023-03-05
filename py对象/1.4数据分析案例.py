"""
1. 数据封装的类
2. 设计包含文件读取相关功能的抽象类，以子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑运算
5. 通过pyecharts进行图形绘制


"""
import json
# 1.数据封装类
class Record: 
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

# 2.抽象类,指出功能但不具体实现
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件数据,读到的每一条数据都转换为Record对象,封装成list返回"""
        pass

class TextFileReader(FileReader):
    """文本类文件实现"""
    def __init__(self,path):
        self.path = path    # 定义成员变量，记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding = "UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # 消除读取到的每行\n
            data_list = line.split(',')
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self,path):
        self.path = path    # 定义成员变量，记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding = "UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict= json.loads(line)
            record = Record(data_dict["data"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list











