#!/bin/bash

set -e
set -u
set -o pipefail

PYTHON_VERSION=${1:-"3.8"}

MOUNT_VOLUME="${PWD}/../"
TARGET_FOLDER="/nlp_profiler"
DOCKER_IMAGE_NAME="nlp_profiler"

echo "~~~ Running nlp_profiler in a docker container"
echo "Docker image name: ${DOCKER_IMAGE_NAME}"
echo "Mounted volume: ${MOUNT_VOLUME}"
echo "Target folder:  ${TARGET_FOLDER}"

echo "~~~ Building docker image ${DOCKER_IMAGE_NAME} with Python version ${PYTHON_VERSION}."
docker build -t ${DOCKER_IMAGE_NAME} --build-arg python_version="${PYTHON_VERSION}" ../

echo "~~~ Running docker container ${DOCKER_IMAGE_NAME}."
docker run -it                                       \
           --volume "${MOUNT_VOLUME}":${TARGET_FOLDER} \
           --workdir ${TARGET_FOLDER}                \
           ${DOCKER_IMAGE_NAME}                      \
           /bin/bash

echo "~~~ Exited docker container."