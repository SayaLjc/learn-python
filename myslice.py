# -*- coding: utf-8 -*-
def trim(s):
    if len(s)==0:
        return '字符串为空'
    else:
        l=len(s)
        print('字符串长度为',l)
    f=0
    for i in s:
        if i ==' ':
            f=f+1
        else:
            break
    for n in s[::-1]:            #list[::1]将list反过来
        if n==' ':
            l=l-1
        else:
            break
    print('有效字符串范围为',f,'to',l)
    print('字符串为',s[f:l])

a=input('请输入字符串')
trim(a)


