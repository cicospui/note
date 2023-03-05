# 1.文件编码
"""
计算机使用编码技术(密码本)将文本内容翻译成01序列存入计算机
编码技术就是翻译规则:UTF-8、GBK、Big5等,不同密码翻译的结果可能不同
目前通用规则使用UTF-8
"""

# 2.文件的读取
"""
操作系统以文件为单位管理磁盘中的数据
文件操作包括:打开、关闭、读、写
1) 打开:   open(name,mode,encoding)
name    打开的目标文件名的字符串(也可包含文件所在的具体路径)
mode    打开文件的模式:只读-r(默认模式)、写入-w、追加-a等
encoding确定编码编码格式,事实上这个不是第三个位置,需要利用关键字传参
"""
f = open('pylearning/text.txt','r',encoding = 'UTF-8')
print(f,type(f))
"""
2) 读取:    
read()方法      文件对象.read(num)  num表示从文件中读取的字节长度,未传入num时则读取所有文件中的数据
readlines()方法 按照行方式读取整个文件中的内容,返回一个列表,每个元素对应一个文件中的行
readline()方法  一次读取一行内容
for循环读取     
"""
# print(f"读取10个字节的结果为:{f.read(10)}")
# print(f"读取全部内容为:{f.read()}")     
# 读取操作在同一代码中重复出现，会接着之前的读取相当于有个小指针指着读到哪里了

# lines = f.readlines()
# print(f"lines type is {type(lines)},content is {lines}")

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"line1 = {line1}line2 = {line2}line3 = {line3}")

for line in f:
    print(f"every line is {line}")

"""
3) 关闭文件
close() 关闭文件对象,不关闭的话文件会一直被python程序占用
停止占用一是close二是停止程序
with open方法   自动对文件的close
"""
with open('pylearning/text.txt','r',encoding = 'UTF-8') as f:
    for line in f:
        print(f"防止忘记关闭文件 {line}")

# 小练习
with open('pylearning/word.txt','r',encoding = 'UTF-8') as txt:
    count = 0
    for line in txt:
        print(f"{line}type is {type(line)}")
        res = line.split(' ')
        print(res)
        for i in res:
            if i == 'itheima':
                count += 1
    print(f"itheima 出现次数为{count}")

# 3.文件的写入
"""
打开文件--文件写入--内容刷新
write()调用时,内容未被真正写入文件,而是积攒在内存中的缓冲区
待到内容刷新时才会写入,关闭时也会写入,因为close内置了flush功能
"""
f = open('pylearning/一个不存在的文件.txt','w',encoding = 'UTF-8')
f.write("hello world!")
f.flush()
f.close()
f = open('pylearning/一个不存在的文件.txt','w',encoding = 'UTF-8')
f.write("itheima")
f.flush()
f.close()
# 只要关闭了文件，再打开写入则会覆盖原文件，但如果中途没有关闭文件，则写入操作会持续的进行

# 4.追加写入操作
"""
a模式下文件不存在则创建文件,存在则在最后追加写入
"""
f = open('pylearning/二个不存在的文件.txt','a',encoding = 'UTF-8')
f.write("hello world!")
f.flush()
f.close()
f = open('pylearning/二个不存在的文件.txt','a',encoding = 'UTF-8')
f.write("itheima")
f.flush()
f.close()

