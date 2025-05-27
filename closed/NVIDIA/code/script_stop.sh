#!/bin/bash
PID=$(cat /tmp/jtop_pid.txt)
kill $PID
