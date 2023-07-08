ARG BASE_IMAGE=python:${PYTHON_VERSION}

FROM ${BASE_IMAGE} as base

RUN apt-get update \ 
    && apt-get install --no-install-recommends -y cmake \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /nlp_profiler

COPY . .

RUN pip install --no-cache-dir -r requirements-dev.txt \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r requirements-nix-dev.txt