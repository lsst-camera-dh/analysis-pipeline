#!/bin/sh

echo ""
echo ""
echo "Entering read_noise.sh wrapper..."
date
echo "------------------------"

# Two functions from the pipeline_wrapper script (are these really needed?)
#function pipelineSet { echo "Pipeline.$1: $2" >> ${PIPELINE_SUMMARY}; }
#function pipelineCreateStream { echo "PipelineCreateStream.$1.$2: $3" >> ${PIPELINE_SUMMARY}; }
#export -f pipelineSet 
#export -f pipelineCreateStream


echo "Prepare DM environment..."
export SHELL=/bin/bash

## EUPS_USERDATA is where a .eups directory is created (else defaults to $HOME)
export EUPS_USERDATA=$PWD
## Not certain why this is needed, but the default is $HOME and that does not work...
export PYTHON_EGG_CACHE=$PWD

## official DM setup script
source /afs/slac/g/lsst/software/redhat6-x86_64-64bit-gcc44/DMstack/Winter2013Beta/loadLSST.sh
setup -t v6_1 pipe_tasks
setup -t v6_1 afw
setup -t v6_1 mysqlpython

echo "Defining env-vars needed by analysis script..."
export PYTHONPATH=${CONFIGDIR}/debug:${LSST_ANALYSIS_SCRIPT_DIR}:${LSST_ANALYSIS_SCRIPT_DIR}/pipeline:${PYTHONPATH}
echo 'LSST_ANALYSIS_SCRIPT_DIR:  '${LSST_ANALYSIS_SCRIPT_DIR}
echo 'PYTHONPATH:  '$PYTHONPATH

echo ""
echo ""
echo "   BEGIN PIPELINE"
echo "   --------------"
echo ""
echo "============================================================================================="

echo "Calling fe55_gain analysis script..."
##python2.7 ${CONFIGDIR}/debug/read_noise_task.py             ### for DEBUGGING only
export OUTPUTDIR=${OUTPUTDIR_ROOT}/fe55_gain
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/fe55_gain_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="


echo ""
echo ""
echo "Calling read_noise analysis script..."
export OUTPUTDIR=${OUTPUTDIR_ROOT}/read_noise
##python2.7 ${CONFIGDIR}/debug/read_noise_task.py             ### for DEBUGGING only
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/read_noise_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="


echo ""
echo ""
echo "Calling ptc analysis script..."
export OUTPUTDIR=${OUTPUTDIR_ROOT}/ptc
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/ptc_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="


echo ""
echo ""
echo "Calling linearity analysis script..."
export OUTPUTDIR=${OUTPUTDIR_ROOT}/linearity
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/linearity_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="


echo ""
echo ""
echo "Calling dark_current analysis script..."
export OUTPUTDIR=${OUTPUTDIR_ROOT}/dark_current
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/dark_current_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="


echo ""
echo ""
echo "Calling bright_pixels analysis script..."
export OUTPUTDIR=${OUTPUTDIR_ROOT}/bright_pixels
python2.7 ${LSST_ANALYSIS_SCRIPT_DIR}/pipeline/bright_pixels_task.py
rc=$?
echo "Return from analysis script = " $rc 
echo "============================================================================================="
echo ""
echo ""
exit $rc