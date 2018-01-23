#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-21
Name: Study
Description：本节内容为函数学习
"""

#n1 = 255
#n2 = 1000
#print('n1=%s' % hex(n1))
#print('n2=%s' % hex(n2))

"""
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x


s = input()
print(my_abs(s))
"""

import math
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('Bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('Bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('Bad operand type')
    n = b*2-4ac
    if n > 0:



