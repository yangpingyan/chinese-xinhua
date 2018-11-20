#!/usr/bin/env python 
# coding: utf-8
# @Time : 2018/11/20 17:00 
# @Author : yangpingyan@gmail.com

import json
import pandas as pd

print("Mission Start")

with open("./data/idiom.json", 'r', encoding='utf-8') as f:
    idiom = json.load(f)

df = pd.DataFrame(idiom)
df['yingbiao_wei'] = df['pinyin'].map(lambda x: x[-1])
df['pinyin_wei'] = df['pinyin'].map(lambda x: x.split(' ')[-1])
df = df[df['yingbiao_wei'] == 'ì']
df.sort_index(axis=1, ascending=False, inplace=True)
df.sort_values(by='pinyin_wei', axis=0, inplace=True)

print("Mission Complete")

# In[1]
