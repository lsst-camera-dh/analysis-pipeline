#!/usr/bin/env python
## Read sensorList.txt and pass data to next job step.jy
##
## Open sensor list file, read in each line, define pipeline variables
## for each sensor

import os,sys
from config import *
import subprocess

## Read in file containing directories of sensor data.

filename = sensorListF

try:
    fileObj = open(filename,'r')
except:
    print '%Error: attempting to open file: ',filename
    sys.exit(1)
    pass

sensorList = fileObj.read().splitlines()

numLines = len(sensorList)

print 'numLines = ',numLines

for sensor in sensorList:
    print "sensor  ",sensor
    pass



##  Create pipeline variables for each sensor


num = 0


for sensor in sensorList:
    if len(sensor)==0 or sensor.startswith("#"): continue
    cmd = "pipelineSet LSST_SENSOR_"+str(num)+" "+sensor
    rc = subprocess.call(cmd,shell=True)
    num += 1
    pass

print "Number of sensors to process = ",num
cmd = "pipelineSet LSST_NUM_SENSORS "+str(num)
rc = subprocess.call(cmd,shell=True)

sys.exit(0)
