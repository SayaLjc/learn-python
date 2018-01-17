# -*- coding:utf-8 -*-
# __author__ = 'Leee'
import turtle
t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(90)
#教训：保存文件不得与导入模块重名，且后续需要删除相关pyc文件