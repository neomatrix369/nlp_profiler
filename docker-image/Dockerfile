ARG python_version

FROM python:$python_version

RUN apt-get update 

RUN apt-get install -y cmake

RUN pip install --upgrade pip

WORKDIR /nlp_profiler

COPY . .

RUN pip install -r requirements-dev.txt

RUN pip install -r requirements.txt

RUN pip install -r requirements-nix-dev.txt