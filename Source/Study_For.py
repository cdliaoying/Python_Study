#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-21
Name: Study
Description：本节内容为if条件判断的学习
"""

#for循环
"""
sum = 0
for x in range(101):
    sum = sum + x
    print(sum)
"""
#while循环
"""
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
"""


"""
#test
#for 循环
Ls = ['Bart', 'Lisa', 'Adam']
Ls.append('Wayne')
for x in range(4):
    print('Hello,', Ls[x], '!')
#简化版本
print('----------我是分隔符----------')

Ls = ['Bart', 'Lisa', 'Adam']
Ls.append('Wayne')
for x in Ls:
    print('Hello,', x, '!')
print('----------我是分隔符----------')

#while 循环
La = ['Bart', 'Lisa', 'Adam']
La.append('Wayne')
y = 3
while y >= 0:
    print('Hello,', La[y], '!')
    y = y - 1
print('----------我是分隔符-----------')

La = ['Bart', 'Lisa', 'Adam']
#La.append('Wayne')
while y in La:
    print('Hello,',y, '!')
"""

#break用法
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('End')

#continue
n = 0
while n < 10:
    n = n +1
    if n % 2 == 0:
        continue
    print(n)