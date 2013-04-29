## This file contains configuration data and expects to be import'ed

import os,sys

print '\n***************************************\n    config.py\n*******************************\n'

## Name of file containing list of sensors to be processed
sensorListF = os.environ['CONFIGDIR']+'/sensorList.txt'

##os.environ['LSST_ANALYSIS_CODE_VERSION'] = '0.0.0.2'  ## 2/22/2013
##os.environ['LSST_ANALYSIS_CODE_VERSION'] = '0.0.0.3'  ## 3/4/2013
os.environ['LSST_ANALYSIS_CODE_VERSION'] = '0.0.0.4'  ## 4/18/2013
os.environ['LSST_ANALYSIS_SCRIPT_DIR'] = '/afs/slac/g/lsst/software/redhat6-x86_64-64bit-gcc44/lsstCameraSensor/test_scripts/'+os.environ['LSST_ANALYSIS_CODE_VERSION']+'/'

#################  DEBUG 4/26/2013 to test new test_script interface  ##################
os.environ['LSST_ANALYSIS_SCRIPT_DIR'] = '/nfs/farm/g/lsst/u1/Pipeline-tasks/LSST_Sensor_Analysis/test_scripts-20130422'

os.environ['LSST_INDATA_ROOT']='/nfs/farm/g/lsst/u1/testData/'   ## original (Harvard)
##os.environ['LSST_INDATA_ROOT']='/nfs/farm/g/lsst/u1/sensorTestData/'  ## new & improved test data (BNL)
os.environ['LSST_OUTDATA_ROOT']=os.environ['TASKROOT']+'/data'

os.environ['LSST_SENSOR_VENDOR'] = 'e2v'


## This bit of confusion is so that Pipeline jython scriptlets can
## hava a peek at selected task configuration objects.  In this case,
## the mapping of analysis script with needed input, and a list of
## desired analysis scripts to run.
analysisConfigFile = os.environ['CONFIGDIR']+'/analysisDict.jy'
execfile(analysisConfigFile)

## Done.
print 'leaving config.py .......'
