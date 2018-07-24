#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile

result = os.popen('ls').read()

for l in result:
    file0 = []
    file1 = []
    file2 = []
    file3 = []
    file4 = []
    l = l[:-1]
    if zipfile.is_zipfile(l):
        zf = zipfile.ZipFile(l,'r')
        zf.extractall(l[:-4])
        for name in zf.namelist():
            if name[-5] == '0':
                file0.append(name)
            if name[-5] == '1':
                file1.append(name)
            if name[-5] == '2':
                file2.append(name)
            if name[-5] == '3':
                file3.append(name)
            if name[-5] == '4':
                file4.append(name)

        if len(file0) != 0:
            os.system('mkdir '+file0[0][7:-6])
        elif len(file1) != 0:
            os.system('mkdir '+file1[0][7:-6])
        elif len(file2) != 0:
            os.system('mkdir '+file2[0][7:-6])
        elif len(file3) != 0:
            os.system('mkdir '+file3[0][7:-6])
        elif len(file4) != 0:
            os.system('mkdir '+file4[0][7:-6])
            
        
        if len(file0) != 0:
            zf = zipfile.ZipFile(file0[0][:-4]+'.zip','w')
            for name in file0:
                zf.write(l[:-4]+'/'+name)
            zf.close()
            os.system('shp2json '+file0[0][:-4]+'.zip'+' '+file0[0][7:-6]+'/'+file0[0][:-4]+'.json')
            os.system('rm '+file0[0][:-4]+'.zip')
        if len(file1) != 0:
            zf = zipfile.ZipFile(file1[0][:-4]+'.zip','w')
            for name in file1:
                zf.write(l[:-4]+'/'+name)
            zf.close()
            os.system('shp2json '+file1[0][:-4]+'.zip'+' '+file1[0][7:-6]+'/'+file1[0][:-4]+'.json')
            os.system('rm '+file1[0][:-4]+'.zip')
        if len(file2) != 0:
            zf = zipfile.ZipFile(file2[0][:-4]+'.zip','w')
            for name in file2:
                zf.write(l[:-4]+'/'+name)
            zf.close()
            os.system('shp2json '+file2[0][:-4]+'.zip'+' '+file2[0][7:-6]+'/'+file2[0][:-4]+'.json')
            os.system('rm '+file2[0][:-4]+'.zip')
        
        if len(file3) != 0:
            zf = zipfile.ZipFile(file3[0][:-4]+'.zip','w')
            for name in file3:
                zf.write(l[:-4]+'/'+name)
            zf.close()
            os.system('shp2json '+file3[0][:-4]+'.zip'+' '+file3[0][7:-6]+'/'+file3[0][:-4]+'.json')
            os.system('rm '+file3[0][:-4]+'.zip')

        if len(file4) != 0:
            zf = zipfile.ZipFile(file4[0][:-4]+'.zip','w')
            for name in file4:
                zf.write(l[:-4]+'/'+name)
            zf.close()
            os.system('shp2json '+file4[0][:-4]+'.zip'+' '+file4[0][7:-6]+'/'+file4[0][:-4]+'.json')
            os.system('rm '+file4[0][:-4]+'.zip')

        os.system('rm -rf '+l[:-4])


