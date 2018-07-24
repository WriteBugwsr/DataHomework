# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:37:17 2018

@author: WSR
"""

#练习题七
#1、使用多选其一，完成天气的提醒，淘宝客户端
#2、一定要多次使用for循环，偶尔使用while循环 在淘宝客户端中
#3、
city=input('Please enter the name of city you want to enquire')
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r #导入联网工具包，命名为r
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')

import json #将字符串转为字典
data=json.loads(data)

a=2
def weatherreport(a):
  
    print('temperature:'+str(data['list'][a]['main']['temp']))
    print('city:'+data['city']['name'])
    print('description:'+data['list'][a]['weather'][0]['description'])
    print('pressure:'+str(data['list'][a]['main']['pressure']))
    print('temp_max:'+str(data['list'][a]['main']['temp_max']))
    print('temp_min:'+str(data['list'][a]['main']['temp_min']))
    
    z=data['list'][a]['weather'][0]['description']
    if data['list'][a]['main']['temp']>30:
        print('温馨提示：气温较高，注意防暑')
    
    if z=='小雨':
        print('温馨提示：记得带伞哦')
    elif z=='多云':
        print('温馨提示：多云天气可以外出游玩')
    else:
        print('温馨提示：记得涂防晒霜呀')

    print('*'*30)
    return

for i in range(1,6):
    weatherreport(a)
    a=a+8



