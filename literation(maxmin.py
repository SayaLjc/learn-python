def findMinAndMax(L):
    
#检查数据类型
    if not isinstance(L,list):
    print('数据类型错误')
    return L


#检查是否为空列表
    if len(L) == 0:
    # print('列表为空') 
        return (None,None)


#定义最小值和最大值
    MinValue = L[0]
    MaxValue = L[0]


#若list里只有一个元素，返回初始定义的最大最小数值
    if(len(L) == 1):
        return (MinValue,MaxValue)


#多于一个元素，遍历列表查找最小，最大值
    for value in L:
        if (MinValue > value):
            MinValue = value
        if (MaxValue < value):
            MaxValue = value
    return (MinValue,MaxValue)