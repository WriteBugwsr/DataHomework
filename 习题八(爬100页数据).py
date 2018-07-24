# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:00:27 2018

@author: WSR
"""

#练习题八  保存淘宝数据 小组项目
#1、每个组员爬取某个url的100页数据 每个组员爬取不同的城市（组间不重复）
#2、保存淘宝商品信息
#3、每组组长合并各组员的数据
import urllib.request as r
import json 

page=0
for i in range(0,100):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E5%B9%BF%E8%A5%BF&bcoffset=4&p4ppushleft=1%2C48&s={}&ntoffset=4&ajax=true'
    try:
        data=r.urlopen(url.format(page)).read().decode('utf-8','ignore')
        data=json.loads(data)
    except Exception as err:
        print('发生错误了')
    print('成功爬取第{}页数据'.format(int(page/44+1)),end=' ')
    f=open('temp.txt','a',encoding='UTF-8') #write  防止乱码有UTF-8和gbk
    f.write(str(data))
    f.write('\n')
    f.close()#关闭程序
    page=page+44