# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:46:40 2018

@author: WSR
"""
#练习题五
#1、优化代码，用函数的方式写出修改练习四代码，输出每一天的天气（函数）
#2、打印温度折线图，使用函数来优化（必须要有返回值）
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
    print('*'*30)
    return
for i in range(1,6):
    weatherreport(a)
    a=a+8


b=2
print('The line chart is ：')
def temper(b):
    return data['list'][b]['main']['temp']
for i in range(1,6):
    print('-' * int(temper(b)))
    b=b+8 
    
    
    
   
   










