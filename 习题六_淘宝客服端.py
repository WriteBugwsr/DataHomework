# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 08:55:39 2018

@author: WSR
"""
#在网址后面加 &ajax=true  可获取网址信息

#练习六
#1、每一行显示四个商品，打印分割线，只要第一页36个商品信息
#2、列出36个商品
#3、获取所有商品的商品价格，并且排序，从高到低排序
#4、按照销量排序
#5、商品过滤，只要15天退款或包邮的商品信息，显示
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
    if ls3[j]==0.0:
        print('第{}商品包邮  '.format(j+1),end='')


