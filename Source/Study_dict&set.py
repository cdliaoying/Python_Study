#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-21
Name: Study
Description：本节内容为if条件判断的学习
dict -dictionary,在其他语言中也称为map，使用建-值（key-value）方式存储
set - 一组key的集合，但不存储value，由于key不能重复，所以在set中，没有重复的key
"""

d = {'Wayne': 100, 'Karen': 99, 'Tracy': 85}
print(d['Karen'])
print(d.get('Adam', -1))
print('Adam' in d)
d['Adam'] = '60'
print(d)
d.pop('Tracy')
print(d)
s = set([1, 2, 3])
print(s)

b=3
print(b*2)