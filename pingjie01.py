#/usr/bin/env python
# -*- coding: utf-8 -*-
import json

#with open('gadm36_CHN_0.json','r') as f:
with open('gadm36_CHN_1.json','r') as f:
    dic0 = json.load(f)

#with open('gadm36_CHN_1.json','r') as f:
with open('gadm36_TWN_0.json','r') as f:
    dic1 = json.load(f)
    print type(dic0['features'])
    print type(dic1['features'])
    dic1['features'] += dic0['features']

with open('pj.json','w') as f:
    json.dump(dic1,f)
    
