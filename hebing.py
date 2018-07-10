#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


#chn = json.loads('CHN/gadm36_CHN_1.json')
#li = chn.get('features')

with open('TWN/gadm36_TWN_0.json') as f:
    twn = json.load(f)
    li1 = twn.get('features')
with open('CHN/gadm36_CHN_1.json') as f:
    chn = json.load(f)
    li2 = twn.get('features')
    li = li1+li2
    chn['features'] = li

with open("china",'w+') as f:
    json.dump(chn,f)
    print "写入完成"


