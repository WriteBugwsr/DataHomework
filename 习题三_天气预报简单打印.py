# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:41:19 2018

@author: WSR
"""
#练习题三
#通过复制联网天气代码，获取老家的天气
#打印温度temp,天气情况description 天气气压pressure

import urllib.request as r  #导入联网工具包， 打开网址，读取内容转换为str
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=heyuan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json #导入字符串转字典工具包
data=json.loads(data)

print('温度：'+str(data['main']['temp']))
print('天气：'+data['weather'][0]['description'])
print('气压：'+str(data['main']['pressure']))