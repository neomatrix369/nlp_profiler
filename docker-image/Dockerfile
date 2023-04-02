FROM python:3.7

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/neomatrix369/nlp_profiler.git

WORKDIR nlp_profiler

ADD app.py . 

RUN pip install -r requirements-dev.txt

RUN pip install -r requirements.txt

RUN pip install -r requirements-nix-dev.txt