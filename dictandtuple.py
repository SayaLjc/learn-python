#1，2为key，a，b指向的tuple为value
a=('1','2','3')
b=('1',['2','3'])
d={'1':a,'2':b}
print(d['1'])
print(d['2'])
input()



z={'a':1,'b':2}
print(z['a'])
print(z['b'])
input()

n={'(1,2,3)':23,'(1,[2,3])':24}
print(n['(1,2,3)'])
print(n['(1,[2,3])'])
input()

'''
m={'('1','2','3')':1,'('1',['2','3'])':2}
print(m['('1','2','3')'])
print(m['('1',['2','3'])'])                    #语法错误
input()
'''


v={'6':(1,2,3),'7':(1,[2,3])}
print(v['6'])
print(v['7'])
input()


#a放入set
x=set(a)
print(x)
input()

#tuple放入set
c=set((1,2,3))
print(c)
input()


'''
#内含list的tuple放入set
c=set((1, [2, 3]))
print(c)
input()




v=set([a,b])
print(v)
input()



c=set(b)
print(c)
input()         #均报错unhashable type：‘list’


'''