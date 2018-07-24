#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


result = os.popen('ls /Users/zhaochen/Desktop/mapechart/echatjson/')


d = {}
d["BES"] = "BE"
with open('/Users/zhaochen/Desktop/daima/contry.txt','r') as f:
    lines = f.readlines()
    for l in lines:
        l = l.replace("\n",'')
        if len(l.strip()) == 0:
            pass
        else:
            d[l[-3:]] = l[:2]

for l in result:

    oldname = l[:3]
    try:
        newname = d[l[:3]]
    except Exception as e:
        print e
    os.popen('mv /Users/zhaochen/Desktop/mapechart/echatjson/%s.json /Users/zhaochen/Desktop/mapechart/echatjson/%s.json'%(oldname,newname))
    




