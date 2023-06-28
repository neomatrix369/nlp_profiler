ARG python_version

FROM python:$python_version

RUN apt-get update 

RUN apt-get install -y cmake

RUN apt-get install -y git

RUN git clone https://github.com/neomatrix369/nlp_profiler.git

WORKDIR nlp_profiler

RUN pip install -r requirements-dev.txt

RUN pip install -r requirements.txt

RUN pip install -r requirements-nix-dev.txt