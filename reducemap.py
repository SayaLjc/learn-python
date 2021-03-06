# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    left, right = s.split('.')
    integral = reduce(lambda x, y=0: x*10+y, map(lambda c: DIGITS[c], left))
    decimal = reduce(lambda x, y=0: x/10+y, map(lambda c: DIGITS[c], right[::-1])) / 10
    return integral + decimal
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')