#!/bin/bash

# Tuer tegrastats
if [ -f /tmp/tegrastats_pid.txt ]; then
    TEGRASTATS_PID=$(cat /tmp/tegrastats_pid.txt)
    kill $TEGRASTATS_PID 2>/dev/null
    sleep 1
    [ -n "$TEGRASTATS_PID" ] && ps -p $TEGRASTATS_PID && kill -9 $TEGRASTATS_PID
    rm /tmp/tegrastats_pid.txt
fi

# Tuer la boucle tail | while
if [ -f /tmp/loop_pid.txt ]; then
    LOOP_PID=$(cat /tmp/loop_pid.txt)
    kill $LOOP_PID 2>/dev/null
    sleep 1
    [ -n "$LOOP_PID" ] && ps -p $LOOP_PID && kill -9 $LOOP_PID
    rm /tmp/loop_pid.txt
fi

# Nettoyer le log
rm -f /tmp/outxx.txt

