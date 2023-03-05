"""
演示自定义模块 
"""

def str_reverse(s):
    """
    接受传入字符串,将字符串反转返回
    """
    rev = []
    for i in range(len(s)):
        rev.append(s[-1-i])
    rev = "".join(rev)
    return rev

def substr(s,x,y):
    """
    按照下标x,y对字符串进行切片
    """
    sub = []
    for i in range(x,y):
        sub.append(s[i])
    sub = "".join(sub)
    return sub    




