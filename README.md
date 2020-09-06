# NLP Profiler [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A simple NLP library allows profiling datasets with one or more text columns. 

When given a dataset and a column name containing text data, NLP Profiler will return either high-level insights or low-level/granular statistical information about the text in that column. 

Think of it as using the `pandas.describe()` function or running [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) on your data frame, but for datasets containing text columns rather than the usual columnar datasets.

Under the hood it does make use of a number of libraries that are popular in the AI and ML communities, but we can extend it's functionality by replacing or adding other libraries as well.

A simple notebook have been provided to illustrate the usage of the library.

**Note:** this is it's inception and so it's not probably capable of doing many things, including running at _scale_. Many of these are opportunities we can work on as we go along using it.

## Requirements

- Python 3.7.x or higher
- Dependencies described in the `requirements.txt`
- (Optional)
  - Jupyter Lab (on your local machine)
  - Google Colab account  
  - Kaggle account

## Get started

### Demo

Take a look at this short demo of the NLP Profiler library by clicking on the below image: 
[![Demo of the NLP Profiler library](https://user-images.githubusercontent.com/1570917/88474968-8fb48980-cf23-11ea-944d-0a1069174ede.png)](https://youtu.be/sdPOyqMfK7M?t=2274)or you find the rest of the [talk here](https://www.youtube.com/watch?v=sdPOyqMfK7M).

### Notebooks

#### Jupyter

See [Jupyter Notebook](./notebooks/jupyter/nlp_profiler.ipynb)

#### Google Colab

You can open these notebooks directly in [Google Colab](./notebooks/google-colab/nlp_profiler.ipynb)

#### Kaggle kernels

**[Notebook/Kernel](https://www.kaggle.com/neomatrix369/nlp-profiler-simple-dataset)** | [Script](https://www.kaggle.com/neomatrix369/nlp-profiler-class) | [Other related links](https://www.kaggle.com/general/166954)

## Installation

Install directly from the GitHub repo:

```bash
pip install git+https://github.com/neomatrix369/nlp_profiler.git@master
```

## Usage

```python
import nlp_profiler.core as nlpprof

new_text_column_dataset = nlpprof.apply_text_profiling(dataset['text_column'])
```

or 

```python
from nlp_profiler.core import apply_text_profiling

new_text_column_dataset = apply_text_profiling(dataset['text_column'])
```

See [Notebooks](#Notebooks) section for further illustrations.

# Contributing

Contributions are very welcome, please share back with the wider community (and get credited for it)!

Please have a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines, also have a read about our [licensing](LICENSE.md) (and warranty) policy.

---

Go to the [NLP page](https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/natural-language-processing/README.md)</br>