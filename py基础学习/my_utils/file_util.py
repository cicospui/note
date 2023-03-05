

def print_file_info(file_name):
    """
    接收传入文件的路径,打印文件的全部内容,如文件不存在则捕获异常,输出提示信息,通过finally关闭文件对象
    """      
    try:        #一种异常
        f = open(file_name,'r',encoding = 'UTF-8') 
    except Exception as e:
        print("打开文件操作出现了异常")
        print("异常为:",e)
    else:
        print(f"打印文件的全部内容为\n{f.read()}")
    finally:
        print("关闭文件")
        f.close()
    
def append_to_file(file_name,data):
    """
    接收文件路径与传入数据,将数据追加到写入文件中
    """
    f = open(file_name,'a',encoding = 'UTF-8')
    f.write(data)
    f.flush()
    f.close()








