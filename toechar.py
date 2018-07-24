#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os


def toechart(fi):
    with open(fi) as f:
        dicgeo = json.load(f)
        li = dicgeo['features']
        for i in range(0,len(li)):
            if dicgeo['features'][i]['properties'].has_key('NAME_1'):
                name1 = dicgeo['features'][i]['properties'].get('NAME_1')
                del dicgeo['features'][i]['properties']
                dicgeo['features'][i]['properties'] = {"name":name1}
            elif dicgeo['features'][i]['properties'].has_key('NAME_0'):
                name = dicgeo['features'][i]['properties'].get('NAME_0')
                del dicgeo['features'][i]['properties']
                dicgeo['features'][i]['properties'] = {"name":name}

        with open("/Users/zhaochen/Desktop/mapechart/"+fi[-10:-7]+'.json','w') as f:
            json.dump(dicgeo,f)

        
li = os.popen('find ~/Desktop/mapsok/ -name "*1*"')
#for fi in li:
#    fi = fi.replace('\n','')
#    toechart(fi)
print "start"
for fi in li:
    fi = fi.replace('\n','')
    print "start toechart"
    toechart(fi)
    print fi[-10:-7]
