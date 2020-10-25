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

PACKAGE_VERSION=$(grep  "__version__ = " nlp_profiler/__init__.py | awk '{print $3}' | tr -d '"' || true)
TARGET_REPO="neomatrix369/nlp_profiler"

if [[ -z "${PACKAGE_VERSION:-}" ]]; then
  echo "ERROR: Cannot find the version number in 'nlp_profiler/__init__.py', cannot proceed. Exiting..."
  exit -1
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "GITHUB_TOKEN cannot be found in the current environment, please populate to proceed."
  echo "For e.g."
  echo "     $ GITHUB_TOKEN=<your token> ./release-to-github.sh"
  echo ""

  exit -1
fi

echo "Synchronising local repo with master"
git pull --rebase origin master
git push origin master

TAG_NAME="v${PACKAGE_VERSION}"
TRIMMED_PACKAGE_VERSION=$(echo ${PACKAGE_VERSION} | tr -d ".")
POST_DATA=$(printf '{
  "tag_name": "%s",
  "target_commitish": "master",
  "name": "%s",
  "body": "Release %s: changelog available at https://github.com/neomatrix369/nlp_profiler/blob/master/CHANGELOG.md#%s",
  "draft": false,
  "prerelease": false
}' ${TAG_NAME} ${TAG_NAME} ${TAG_NAME} ${TRIMMED_PACKAGE_VERSION})
echo "Creating release ${PACKAGE_VERSION}: $POST_DATA"
curl \
    -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Content-Type: application/json" \
    -H "Accept: application/vnd.github.v3+json" \
    -X POST -d "${POST_DATA}" "https://api.github.com/repos/${TARGET_REPO}/releases"

TMP_FOLDER=release-artifacts
mkdir -p "${TMP_FOLDER}"
CURL_OUTPUT="./${TMP_FOLDER}/github-release.listing"
echo "Getting Github ReleaseId"
curl \
    -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    -X GET "https://api.github.com/repos/${TARGET_REPO}/releases/tags/${TAG_NAME}" |
    tee ${CURL_OUTPUT}
RELEASE_VERSION=$(cat "${CURL_OUTPUT}" | grep id | head -n 1 | tr -d " " | tr "," ":" | cut -d ":" -f 2)

echo ""
echo "GitHub RELEASE_VERSION: ${RELEASE_VERSION}"
echo "PACKAGE_VERSION: ${PACKAGE_VERSION}. TAG_NAME: ${TAG_NAME}."
echo "See change logs at https://github.com/neomatrix369/nlp_profiler/blob/master/CHANGELOG.md#${TRIMMED_PACKAGE_VERSION}"
echo "~~~ Finished creating tag and release on GitHub ~~~"
echo ""
echo ""
echo "Fetching the tags to local machine."
git fetch --all
echo "Finished fetching the tags to local machine."
