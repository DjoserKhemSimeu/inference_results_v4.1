#!/bin/bash

export DATA_DIR=/data
export MODEL_DIR=/model
export number_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`
export NUM_SOCKETS=`grep physical.id /proc/cpuinfo | sort -u | wc -l`
export CPUS_PER_SOCKET=$((number_cores/NUM_SOCKETS))

export CPUS_PER_PROCESS=${CPUS_PER_SOCKET}  # which determine how much processes will be used
export CPUS_PER_INSTANCE=2
export CPUS_FOR_LOADGEN=1
export BATCH_SIZE=200

if [ $CPUS_PER_SOCKET == 128 ]; then
    if [ $1 == "server" ]; then
        export CPUS_PER_INSTANCE=2
        export BATCH_SIZE=100
    fi
fi

export DNNL_MAX_CPU_ISA=AVX512_CORE_AMX

export KMP_BLOCKTIME=1
export OMP_NUM_THREADS=$CPUS_PER_INSTANCE
export KMP_AFFINITY="granularity=fine,compact,1,0"
export DNNL_PRIMITIVE_CACHE_CAPACITY=20971520
export LD_PRELOAD="${CONDA_PREFIX}/lib/libtcmalloc.so:${CONDA_PREFIX}/lib/libiomp5.so"
export DLRM_DIR=$PWD/python/model
export TCMALLOC_LARGE_ALLOC_REPORT_THRESHOLD=30469645312

dtype="fp32"
batch_size=$(($BATCH_SIZE + 0))
if [ $# -ge 2 ]; then
    if [[ $2 == "accuracy" ]]; then
        test_type="accuracy"
    fi
    if [[ $2 == "bf16" ]] || [[ $3 == "bf16" ]]; then
        dtype="bf16"
    elif [[ $2 == "int8" ]] || [[ $3 == "int8" ]]; then
        dtype="int8"
	int8_cfg="--int8-configure-dir=int8_configure.json"
    fi
else
    test_type="performance"
fi

mode="Offline"
extra_option="--samples-per-query-offline=204800"
if [ $1 == "server" ]; then
    mode="Server"
    extra_option=""
fi

sudo ./run_clean.sh
echo "Running $mode bs=$batch_size $dtype $test_type $DNNL_MAX_CPU_ISA"
export TMP_DIR=${TMP_DIR}
LOG_DIR=${TMP_DIR} bash run_local.sh pytorch dlrm multihot-criteo cpu $dtype $test_type \
        --int8-model-dir=${MODEL_DIR} \
        --int8-model=dlrm_int8.pt \
        --scenario $mode \
        --max-ind-range=40000000 \
        --samples-to-aggregate-quantile-file=${PWD}/tools/dist_quantile.txt \
        --max-batchsize=$batch_size \
        $extra_option ${int8_cfg}
