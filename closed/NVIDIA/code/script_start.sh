#!/bin/bash
cd /media/nvidia/00640565-37a8-4b58-a27b-fbd90cd43fec/inference_results_v4.1/closed/NVIDIA/code
nohup python3 -c 'from jtop_measure import JtopMeasure; measure = JtopMeasure(); measure.start()' > /tmp/jtop.log 2>&1 &
echo $! > /tmp/jtop_pid.txt
