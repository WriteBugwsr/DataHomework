# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:21:41 2018

@author: WSR
"""
#作业十
#1、获取2300所学校的编号
#2、获取31所城市的编号
#3、获取142600数据  每个组获取3个城市，最后合并
#4、将142600数据使用Spark统计



#获取2300所学校
ls=open('school_id.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line)

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/48.0.2564.82',
       'X-Requested-With':'XMLHttpRequest' }
    
f=open('陕西3.txt','a',encoding='utf-8')
for schoolid in schoolls[0:]:
        req=r.Request(url,data='id={}&type=2&city=61&state=1'.format(schoolid).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()
    
    
f1=open('异常的学校.txt','a',encoding='utf-8')

for schoolid in [971]:
    req=r.Request(url,data='id={}&type=1&city=61&state=1'.format(schoolid).encode(),headers=headers)
    f1.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
f1.close()
    
    
    
    
    
    
    
    
    
    