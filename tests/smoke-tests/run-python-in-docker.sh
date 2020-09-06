#!/bin/bash
set -eou pipefail

MOUNT_VOLUME="${PWD}/../../"
TARGET_FOLDER="/nlp_profiler"
echo "~~~ Running Python 3.7 in a docker container"
echo "Mounted volume: ${MOUNT_VOLUME}"
echo "Manual smoke test steps: "
echo "   $ pip install pandas"
echo "   $ python"
echo "   >>> import nlp_profiler.core as nlpprof"
echo "   ( Use the steps in the Jupyter notebook: notebooks/jupyter/nlp_profiler.ipynb )"
echo "   ( inside the Python REPL to test out the nlp_profiler library                 )"
echo "   ( creating dataset, importing library, using apply_text_profiling, etc...     )"
echo ""
docker run -it                                       \
           --rm                                      \
           --volume ${MOUNT_VOLUME}:${TARGET_FOLDER} \
           --workdir ${TARGET_FOLDER}                \
           python:3.7                                \
           /bin/bash
echo "~~~ Exited docker container."