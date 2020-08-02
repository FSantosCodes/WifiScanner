### LIBRARIES ###

import os
import datetime
import time
import sys
import csv
import math

### INPUTS ###
run=240 #minutes to scan (240 -> 4 hours; 180 -> 3 hours)
freq=5 #seconds after next scan 
out='/home/pi/DATA/miercoles28/0test' #output folder name

### PROCESSING ###

#sudo date -s 'Tue Aug  27 23:00:00 UTC 2019'

#calculate number of iterations
looperCPU = run * 60
looperCPU = math.floor(looperCPU / freq)
#index to iteration
indexloop = 0
while(looperCPU != 0):
    indexloop = indexloop + 1
    #frequency
    time.sleep(freq)
    #system time
    scantime = datetime.datetime.now()
    scantime = scantime.strftime('%Y-%m-%d %H:%M:%S')
    #command call
    cmd = "iwlist wlan0 scan | egrep 'SSID|Adress|Signal'"
    ret = os.popen(cmd).read().split()
    #extract lecture
    EESID = [s for s in ret if "ESSID" in s]
    EESID = [w.replace('ESSID:', '') for w in EESID]
    Signal = [s for s in ret if "level" in s]
    Signal = [w.replace('level=', '') for w in Signal]
    Quality = [s for s in ret if "Quality" in s]
    Quality = [w.replace('Quality=', '') for w in Quality]
    #save
    lecture = [scantime,EESID,Signal,Quality]
    myFile = open(out + '/dataChunk_'+ str(indexloop) + '.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lecture)
        print(lecture)
        #complete cycle
        looperCPU -= 1
