# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import datetime
import pyinotify
import logging

exp1 = "export HISTORY_FILE=/var/log/jldata.log"
exp2 = 'export PROMPT_COMMAND='
exp3 = r'{ date "+%Y-%m-%d %T ##### $(who am i |awk "{print \$1\" \"\$2\" \"\$5}")  #### $(pwd) #### $(history 1 | { read x cmd; echo "$cmd"; })"; } >> $HISTORY_FILE'
exp3 = "\'"+exp3+"\'"
exp3 = exp2+exp3

with open("/etc/bash.bashrc",'a+') as f:
    f.write(exp1+'\n')
    f.write(exp3+'\n')

os.system(". /etc/bash.bashrc")
os.system("touch /var/log/jldata.log")


pos = 0
 
def printlog():
    global pos
    try:
            fd = open(r'/var/log/jldata.log')
            if pos != 0:
                fd.seek(pos,0)
            while True:
                line = fd.readline()
                if line.strip():
                    print line.strip()
                pos = pos + len(line)
                if not line.strip():
                    break
            fd.close()
    except Exception,e:
        print str(e)
class MyEventHandler(pyinotify.ProcessEvent):
     
    #当文件被修改时调用函数
    def process_IN_MODIFY(self, event):
        try:
            printlog()
        except Exception,e:
            print str(e)
 
def main():
    #输出前面的log
    printlog()
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/var/log/jldata.log', pyinotify.ALL_EVENTS, rec=True)
    eh = MyEventHandler()
 
    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()
 
if __name__ == '__main__':
    main()
