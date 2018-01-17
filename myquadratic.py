# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(int)):
            raise TypeError('bad operand type')
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b-math.sqrt(delta))/2*a
        x2=(-b+math.sqrt(delta))/2*a
        print('方程有两个解，分别为',x1,x2)
    elif delta==0:
        x1=(-b)/2*a
        print('方程有一个解，解为',x1)
    else:
        print('方程无解')





A=int(input('请输入整型参数a：'))
B=int(input('请输入整型参数b：'))
C=int(input('请输入整型参数c：'))
quadratic(A,B,C)
