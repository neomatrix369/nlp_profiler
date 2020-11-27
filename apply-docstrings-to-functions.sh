#!/bin/bash

#
# Copyright 2020 Mani Sarkar
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
#

set -e
set -u
set -o pipefail

echo "~~~ Attempting to apply docstrings to functions in source files in nlp_profiler (using docly)"
for file in $(ls nlp_profiler/**/*.py)
do 
   echo "~~~~ Attempting to apply docstrings to $file"
   exit_code=0
   docly-gen $file || true && exit_code=$?

   if [[ ${exit_code} != 0 ]]; then
      echo "~~~~ Failed to apply docstrings to $file, due to the above error(s)"
   else
      echo "~~~~ Finished applying docstrings to $file"
   fi
   
   echo ""
done;
echo "~~~ Finished applying docstrings to functions in source files in nlp_profiler (using docly)"