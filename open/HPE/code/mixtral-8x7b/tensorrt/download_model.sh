#!/bin/bash
# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e

source code/common/file_downloads.sh

# Make sure the script is executed inside the container
if [ -e /work/code/mixtral-8x7b/tensorrt/download_data.sh ]
then
    echo "Inside container, start downloading..."
    echo "The mixtral download is not automatable. Please run git clone https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1 to download the model."
else
    echo "WARNING: Please enter the MLPerf container (make prebuild) before downloading model."
    echo "WARNING: The model is NOT downloaded! Exiting..."
    exit 0
fi
