

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

echo "Synchronising local repo with master"
git pull --rebase origin master
git push origin master

echo ""
echo "Creating the distribution artifacts"
echo "  -- removing older version of build and nlp_profiler.egg-info"
rm -fr build nlp_profiler.egg-info
echo "  -- running python setup.py"
python setup.py sdist bdist_wheel

echo ""
echo "Uploading package using twine"
twine upload --skip-existing dist/*
echo ""

PACKAGE_VERSION=$(grep  "__version__ = " nlp_profiler/__init__.py | awk '{print $3}' | tr -d '"' || true)
echo "~~~ Finished uploading nlp_profiler ${PACKAGE_VERSION} to pypy ~~~"
echo "~~~ Goto https://pypi.org/project/nlp-profiler/{PACKAGE_VERSION}/ to see latest version ~~~"
echo ""