#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-23
Name: Study
Description：本章为地址识别拆分
"""

# Step 1: 输入地址，并根据词库进行地址拆分
import jieba
jieba.load_userdict('/Applications/jieba-0.39/User_Define.txt')  # 加载自定义词库
# sentence = input("请输入要拆分的地址...\n")
# words = [list(jieba.cut(doc)) for doc in sentence]
# print(words)
sentence = ("成都市锦江区工业大道109号")
Words = jieba.lcut(sentence)
# Regoin = dict(JJ='锦江区', XD='新都区', GX='高新区')
# Street = dict(GY='工业大道', TFDD='天府大道')
Regoin = ['锦江区', '新都区', '高新区']
Street = ['工业大道', '天府大道', '剑南大道']
print(Street)
x = len(Words)
while x > 0:
    x = x - 1
    if Words[x] in Regoin:
        V1 = 'R1'
        x = 0
    else:
        V1 = 'R0'
y = len(Words)
while y > 0:
    y = y - 1
    if Words[y] in Street:
        V2 = 'S1'
        y = 0
    else:
        V2 = 'S0'
print(Words)
print('地址代码为：', V1, '-', V2)

x = input('请输入测试地址...\n')


