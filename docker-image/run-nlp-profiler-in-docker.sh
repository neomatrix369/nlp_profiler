#!/bin/bash

set -e
set -u
set -o pipefail

MOUNT_VOLUME="${PWD}/../"
TARGET_FOLDER="/nlp_profiler"
DOCKER_IMAGE_NAME="nlp_profiler"

echo "~~~ Running nlp_profiler in a docker container"
echo "Mounted volume: ${MOUNT_VOLUME}"

docker build -t ${DOCKER_IMAGE_NAME} .

docker run -it                                       \
           --volume ${MOUNT_VOLUME}:${TARGET_FOLDER} \
           --workdir ${TARGET_FOLDER}                \
           ${DOCKER_IMAGE_NAME}                      \
           /bin/bash