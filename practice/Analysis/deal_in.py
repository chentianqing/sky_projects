# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-01-21 16:08
# @Author  :    TianQing Chen
# @File    :    deal_in.py
# function :    count words
"""
    整体思路：
    1，对文档进行初始化处理，变成可处理对象
    2，统计
    3，排序
    4，输出
"""

import re

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]',' ',text)

    # 转换小写
    text = text.lower()

    #生成单词列表
    word_list = text.split(' ')
    # print(word_list)
    #去除空白单词
    word_list = filter(None,word_list)

    # 生成单词和词频到字典
    word_cnt = {}
    for word in word_list:
        if word not  in word_cnt:
            word_cnt[word] = 0
        else:
            word_cnt[word] += 1

    # 排序
    sorted_world_list = sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)

    return sorted_world_list


with open('in.txt','r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt','w') as fout:
    for word,freq in word_and_freq:
        fout.write('{} {}\n'.format(word,freq))