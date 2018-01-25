#!/usr/bin/python2
# coding=utf-8

'''
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-19
Name: Study
'''

# 定义字符转换
'''
print('Wayne'.encode('ascii')) #encode函数将 str 型转为 bytes
print('中文'.encode('utf-8'))
print(chr(66))
print(len(chr(25991)))
print(b'ABC'.decode('ascii')) #将 bytes 转换为 str
'''

# if函数判断
'''
word = input("请输入您的年龄...\n")
if word >= "18": print("已成年")
else: print("未成年")
'''

# 测试%字符
# %格式化字符串，%s 表示用字符串替换，%d表示用整数替换， 有几个 %？占位符，后面就跟几个变量或值，%s 可以将任何类型数据转为字符串
'''
print('hello,%s' % 'world')
print('hi,%s,you have $%d.' % ('Wayne', 10000))
print('%d.%02d' % (3,1))
print('%.2f' % 3.14159226) #控制浮点数小数位数
print('hello,{0},成绩提升了 {1:.2f}%'.format('Wayne',20.8745)) #format()函数
'''
# test
s2016 = 72
s2017 = 85
r = (s2017 - s2016) / s2016
print('(字符串方法)小明成绩较上年提升了 %.1f%%' % r)
print('(format方法)小明成绩较上年提升了 {0:.1f}%'.format(r))

import re

sen = '成都市锦江区工业大道109号'
rule = [r'附.+号', r'.+号']
x = rule[0]
print(x)
re1 = re.findall(x, sen)  # 查找规则1包含字符，如包含len>0。具有规则楼栋，需要重新做正则式规则
print(re1)
