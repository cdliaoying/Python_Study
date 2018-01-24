#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creator: Wayne
Date: 2018-01-23
Name: Study
Description：本文档为验证地址识别和核验的业务逻辑编写
"""

'''
对地址进行分段，地址分为宏观部分和微观部分。
宏观部分：决定房屋的GIS坐标，故最小粒度可能为：街道名称/门牌号/小区名称/街道符号
微观部分：决定房屋在小区内部的位置，基本格式为：*栋*单元*楼层*房号
本次测试案例暂以成都区域登记地址为对象，暂不考虑简阳地址。
'''

# Step1:将地址拆分为宏观和微观部分。
# 拆分规则（待确定）：1）字段中包含：a。附*号，b. *号

import re
import jieba
jieba.load_userdict('/Applications/jieba-0.39/User_Define.txt') # 引用本地词库

# 定义检查函数，检查地址中是否包含既定规则的字符，如果包含，拆分字符，如果不包含，提示检查地址
def Address_First_Cut(sen):
    global sen1, sen2
    rule1 = r'附.+号'   # 设定规则1：包含符号的规则
    rule2 = r'.+号'    # 设定规则2：地址中包含"号"的规则
    re1 = re.findall(rule1, sen)  # 查找规则1包含字符，如包含len>0
    re2 = re.findall(rule2, sen)  # 查找规则2包含字符，如包含len>0。规则漏洞：若地址中非街道部分包含本关键字,可能导致结果错误
    if len(re1) > 0:
        sentence = sen.split(re1[0], 1)
        sen1 = '成功'
        sen2 = '%s%s' % (sentence[0], re1[0]) # %s效率较 +效率更高
        sen3 = sentence[1]
    elif len(re2) > 0:
        sentence = sen.split(re2[0], 1)
        sen1 = '成功'
        sen2 = '%s%s' % (sentence[0], re2[0])
        sen3 = sentence[1]
    else:
        sen1 = '失败'
        sen2 = '请检查您输入的地址：'+sen
        sen3 = ''
    return sen1, sen2, sen3


x = input('请输入测试地址...\n')
y = Address_First_Cut(x)
if y[0] == '成功':
    w1 = jieba.lcut(y[1])
    w2 = jieba.lcut(y[2])
    print(w1)
    print(w2)
else:
    print(y[1])

