#!/usr/bin/python3
# coding=utf-8

'''
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-21
Name: Study
Description：本节内容为数组的学习
'''

'''
Classmate = ['wayne','karen','Mashall']
print(Classmate)
print(Classmate[0])
print(Classmate[-2])
Classmate.append('Adam') #在list中最后位置增加字符串
Classmate.insert(3,'Mike') #向list中指定位置添加字符串
print(Classmate)
print(Classmate[0])
print(Classmate[-2])
Classmate.pop(2) #pop()删除list中指定位置的字符串
print(Classmate)

t = [] 定义的是可变的数组，
t = () 定义的是不变的元组
在定义单个元素元组时，为消除歧义，应当定义为 t = (1,) 用，消除歧义，避免程序定义为数学符号
但在tuple 元组中可以包含一个可变的list
'''


#练习题
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]

S = ['Java','Python','Ruby','PHP']
x = 5
while x >= 0:
    s = input('请输入姓名...')
    if s in S:
        print(s)
        exit()
    else:
        print('您输入的姓名不存在！')
        x = x - 1
else:
    print('您已经超过输入次数')
