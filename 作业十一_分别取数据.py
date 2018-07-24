# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:57:55 2018

@author: WSR
"""
######################取校名##########################################3
f=open('学校和数字1.txt',encoding='gbk').readlines()
schools=[]

for line in f:
    schools.append(line.split(',')[0][1:])
a=open('校名.txt','a',encoding='gbk')
a.write(str(schools))
a.close()
######################取人数####################################3
z=open('学校和数字1.txt',encoding='gbk').readlines()
schools2=[]

for line in z:
    schools2.append(line.split(',')[1][0:-2])
b=open('人数.txt','a',encoding='utf-8')
b.write(str(schools2))
b.close()