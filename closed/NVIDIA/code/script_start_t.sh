#!/bin/bash


CSV_FILE="/media/nvidia/00640565-37a8-4b58-a27b-fbd90cd43fec/data/consommation_energie_jetson.csv"


echo "timestamp,gpu_power" > $CSV_FILE


tegrastats --interval 200 --logfile /tmp/out.txt --start &


start_time=$(date +%s.%3N)


while [ ! -s /tmp/out.txt ]; do
    
    continue
done


tail -f /tmp/out.txt | while read line; do
   
    gpu_power=$(echo $line | grep -oP 'VDD_GPU_SOC \K\d+')

   
    current_time=$(date +%s.%3N)
    elapsed_time=$(echo "$current_time - $start_time" | bc)

   
    if [ -n "$gpu_power" ]; then
        echo "$elapsed_time,$gpu_power" >> $CSV_FILE
    fi
done
