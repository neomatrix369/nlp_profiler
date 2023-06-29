#!/bin/bash

set -e
set -u
set -o pipefail

MOUNT_VOLUME="${PWD}/../"
TARGET_FOLDER="/nlp_profiler"
DOCKER_IMAGE_NAME="nlp_profiler"
PYTHON_VERSION="3.8"

echo "~~~ Running nlp_profiler in a docker container"
echo "Docker image name: " ${DOCKER_IMAGE_NAME}}
echo "Mounted volume: ${MOUNT_VOLUME}"
echo "Target folder: " ${TARGET_FOLDER}
echo "Python version: ${PYTHON_VERSION}"

docker build -t ${DOCKER_IMAGE_NAME} --build-arg python_version=${PYTHON_VERSION} ../

docker run -it                                       \
           --volume ${MOUNT_VOLUME}:${TARGET_FOLDER} \
           --workdir ${TARGET_FOLDER}                \
           ${DOCKER_IMAGE_NAME}                      \
           /bin/bash