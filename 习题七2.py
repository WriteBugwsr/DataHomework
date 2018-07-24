# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:30:41 2018

@author: WSR
"""
#练习题七
#1、使用多选其一，完成天气的提醒，淘宝客户端
#2、一定要多次使用for循环，偶尔使用while循环 在淘宝客户端中
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json #将字符串转为字典
data=json.loads(data)

ls3=[]
i=0
for i in range(0,36):
    print('第{}件商品'.format(i+1))
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    ls3.append(float(data['mods']['itemlist']['data']['auctions'][i]['view_fee']))
    print('')
    if (i+1)%4==0:
         print(str('=')*30)

ls=[]
ls2=[]
b=[0]*36
a=[0]*36
def price(i):
    for i in range(0,36):
        ls.append(float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])) 
        c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        ls2.append(float(c[0:-3]))
price(i)    
b=sorted(ls)
a=sorted(ls2) 
b.reverse()
print('按价格降序排序为'+'\n'+str(b))
print('按销量升序排序为'+'\n'+str(a)+'\n')

for j in range(0,36):
    while ls3[j]==0.0:
        print('第{}商品包邮  '.format(j+1),end='')
        break


