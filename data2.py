# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv

data=open('.\Documents\Event.csv','r')
writ=open('doreen.txt','w')

data2=csv.reader(data)
for line in data2:
    print(line[3]+'  \t  '+line[5]+'\n')
    writ.write('\n'+line[3]+'   \t   '+line[5]+'\n' )
data.close()
writ.close()