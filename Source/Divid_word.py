#!/usr/bin/python3
# coding=utf-8

'''
Environment: Python 3.6
Creat: Wayne
Date: 2018-01-23
Name: Study
Description：本节为网络抄录的结巴分词器sample
'''

import jieba

"""
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))
"""

sentence = ("新都区新都镇工业大道10号")
Words = jieba.lcut(sentence)
print(Words)