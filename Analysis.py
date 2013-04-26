#!/usr/bin/env python

print "\n\nEntering Analysis.py\n-----------------------\n"

import os,sys
import shlex,subprocess
from config import *

## ##  Data passed down through a file -- turn into environment variables
## fid = open('setupAnalysis.txt','r')
## mylines = fid.read().splitlines()
## print "Contents of file passed from setupAnalysis:\n",mylines
## for line in mylines:
##     var = line.split('=')[0]
##     val = line.split('=')[1]
##     os.environ[var]=val
##     pass


##  Data in environment variables
print '\n\n** Dump of LSST_ env-vars:'
for var in os.environ:
    if var.startswith('LSST'):
        print var,', ',os.environ[var]
        pass
    pass

print "\n\nLSST_ANALYSIS_SCRIPT_DIR = ",os.environ['LSST_ANALYSIS_SCRIPT_DIR'],'\n\n'
    
simdir = os.environ['LSST_SENSOR_DIR']
(site,sensor)=simdir.split('/')
os.environ['LSST_SITE'] = site
os.environ['LSST_SENSOR'] = sensor
print 'LSST_SITE = ',site
print 'LSST_SENSOR = ',sensor


print 'LSST_INDATA_ROOT = ',os.environ['LSST_INDATA_ROOT']
print 'LSST_OUTDATA_ROOT = ',os.environ['LSST_OUTDATA_ROOT']

## Env-vars especially for analysis scripts
os.environ['SENSOR_ID'] = os.environ['LSST_SENSOR']
os.environ['CCD_VENDOR'] = os.environ['LSST_SENSOR_VENDOR']
os.environ['DB_CREDENTIALS'] = '/nfs/farm/g/lsst/u1/testData/SIMData/pipeline/mysql_db_data_app.par'
os.environ['OUTPUTDIR_ROOT']=os.environ['LSST_OUTDATA_ROOT']+'/Stream-'+os.environ['PIPELINE_STREAMPATH'].split('.')[0]+'/'+os.environ['LSST_SENSOR_DIR']

## Clean up output directory
cmd = "rm -rf "+os.environ['OUTPUTDIR_ROOT']
print cmd
cmdList = shlex.split(cmd)
rc = subprocess.call(cmd,shell=True)
print 'Return code from output dir cleanup = ',rc

## Create output directory, if needed
os.makedirs(os.environ['OUTPUTDIR_ROOT'])


##  Call Analysis Script(s)
print "LSST_ANALYSIS_SCRIPT_DIR = ",os.environ['LSST_ANALYSIS_SCRIPT_DIR']
print "Calling analysis script wrapper....."

cmd = 'bash '+os.environ['CONFIGDIR']+'/analysis_pipeline.sh'
print cmd
sys.stdout.flush()
cmdList = shlex.split(cmd)
rc = subprocess.call(cmd,shell=True)
sys.stdout.flush()
print "Returning from analysis routine, rc = ",rc
sys.stdout.flush()


## Post-analysis steps

## Create pipeline variable containing directory of files to be registered
cmd = 'pipelineSet LSST_OUTPUTDIR_ROOT '+os.environ['OUTPUTDIR_ROOT']
xrc = subprocess.call(cmd,shell=True)

sys.exit(rc)
