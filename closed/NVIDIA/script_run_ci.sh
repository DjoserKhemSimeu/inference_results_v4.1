#!/bin/bash

# Check if the qc parameter is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <qc>"
    exit 1
fi

qc=$1

# Loop to run the command 10 times
for i in {1..10}; do
    echo "Running iteration $i"

    # Run the make command
    make run_harness RUN_ARGS="--benchmarks=bert --scenarios=singlestream"

    # Rename the output CSV file
    mv /media/nvidia/00640565-37a8-4b58-a27b-fbd90cd43fec/scratch/save_data/consommation_energie_jetson.csv \
       /media/nvidia/00640565-37a8-4b58-a27b-fbd90cd43fec/scratch/save_data/consommation_energie_single_orin_QC_${qc}_${i}_ci.csv

    echo "Finished iteration $i"
done

echo "All iterations completed."
