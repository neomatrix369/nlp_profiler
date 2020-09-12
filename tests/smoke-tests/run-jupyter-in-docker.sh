#!/bin/bash
set -eou pipefail

MOUNT_LIB_VOLUME="${PWD}/../../"
MOUNT_NOTEBOOK_VOLUME="${PWD}/../../notebooks/jupyter"
TARGET_LIB_FOLDER="/nlp_profiler"
TARGET_NOTEBOOK_FOLDER="/home/jovyan/work"
echo "~~~ Running Jupyter Lab/Python in a docker container"
echo "Mounted library volume: ${MOUNT_LIB_VOLUME}"
echo "Manual smoke test steps: "
echo "   open the browser on port 8888"
echo "   see console messages for further instructions"
echo "   go to the nlp_profiler.ipynb notebook"
echo "   install the nlp_profiler library using steps in the README.md"
echo "   run all the cells in the notebook"
echo ""
docker run --rm -it                  \
           -p 8888:8888              \
           -p 4040:4040              \
           -e JUPYTER_ENABLE_LAB=yes \
           --volume ${MOUNT_LIB_VOLUME}:${TARGET_LIB_FOLDER}           \
           --volume ${MOUNT_NOTEBOOK_VOLUME}:${TARGET_NOTEBOOK_FOLDER} \
           --workdir ${TARGET_LIB_FOLDER}                              \
           jupyter/all-spark-notebook
echo "~~~ Exited docker container."