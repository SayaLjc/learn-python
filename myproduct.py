# -*- coding: utf-8 -*
def product(*args):
    if len(args) == 0:
        raise TypeError('input is empty')
#检查输入是否是数字    
    for i in args:
        if not isinstance(i,(int,float)):
            raise TypeError(i,'bad oprand type')
    sum=1
    for i in args:
        sum=sum*i
    return sum
