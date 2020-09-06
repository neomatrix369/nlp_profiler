#!/bin/python

from setuptools import setup
from setuptools import find_packages

import nlp_profiler

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

with open("requirements.txt", encoding='utf8') as requirements_txt:
    install_requirements = requirements_txt.read().split(",")

setup(
    name="nlp_profiler",
    version=nlp_profiler.__version__,
    description='A simple NLP library allows profiling datasets with one or more text columns.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author='Mani Sarkar',
    url='https://github.com/neomatrix369/nlp_profiler',
    license = "Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    keywords="nlpprofiler, nlpprof, nlp_profiler, nlp-profiler",
    install_requires=install_requirements,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0 License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)