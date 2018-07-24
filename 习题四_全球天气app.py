# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:45:29 2018

@author: WSR
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=heyuan,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r #导入联网工具包，命名为r
r.urlopen(url).read().decode('utf-8','ignore')

import json #将字符串转为字典
data=json.loads(data)

####温度   例子
#data字典-->list列表-->o index字典-->main字典-->temp变量
data['list'][0]['main']['temp']


#练习题四
#1、打印每天18点的天气信息，温度，城市，情况，气压，最高温度，最低温度
#2、写出英文版的天气application-天气情况，用户输入英文 （即可以选择语言）
#3、打印温度折线图（字符乘以数字实现）
#4、获取所有温度，并且排序（sorted函数实现 升序）
#5、友情提示，根据温度提示穿衣，打伞，出门（可选）

url='http://api.openweathermap.org/data/2.5/forecast?q=heyuan,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r #导入联网工具包，命名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json #将字符串转为字典
data=json.loads(data)

#第一天

print('temperature:'+str(data['list'][2]['main']['temp']))
print('city:'+data['city']['name'])
print('description:'+data['list'][2]['weather'][0]['description'])
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('*'*30)
 #第二天                     
print('temperature:'+str(data['list'][10]['main']['temp']))
print('city:'+data['city']['name'])
print('description:'+data['list'][10]['weather'][0]['description'])
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('*'*30)
 #第三天
print('temperature:'+str(data['list'][18]['main']['temp']))
print('city:'+data['city']['name'])
print('description:'+data['list'][18]['weather'][0]['description'])
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('*'*30)
 #第四天
print('temperature:'+str(data['list'][26]['main']['temp']))
print('city:'+data['city']['name'])
print('description:'+data['list'][26]['weather'][0]['description'])
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('*'*30)
 #第五天
print('temperature:'+str(data['list'][34]['main']['temp']))
print('city:'+data['city']['name'])
print('description:'+data['list'][34]['weather'][0]['description'])
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('*'*30)
#3、打印温度折线图（字符乘以数字实现）
temper = [data['list'][2]['main']['temp'],
          data['list'][10]['main']['temp'],
          data['list'][18]['main']['temp'],
          data['list'][26]['main']['temp'],
          data['list'][34]['main']['temp']]
print('The line chart is ：')
print('-' * int(temper[0]))
print('-' * int(temper[1]))
print('-' * int(temper[2]))
print('-' * int(temper[3]))
print('-' * int(temper[4]))
#4、获取所有温度，并且排序（sorted函数实现 升序）
print(temper)
print(sorted(temper))



