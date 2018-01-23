#!/usr/bin/python3
# coding=utf-8

'''
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-21
Name: Study
Description：本节内容为if条件判断的学习
'''

H = input('请输入身高：')
W = input('请输入体重：')
Height = float(H)
Weight = float(W)
BMI = round(Weight/(Height*Height), 2)
if BMI < 18.5:
    Result = '过轻'
elif 18.5 <= BMI < 25:
    Result = '正常'
elif 25 <= BMI < 28:
    Result = '过重'
elif 28 <= BMI < 32:
    Result = '肥胖'
else:
    Result = '严重肥胖'
print('您的身高为: ', Height, 'm')
print('您的体重为: ', Weight, 'kg')
print('您的BMI指数为：', BMI, '检查结果为: ', Result)
