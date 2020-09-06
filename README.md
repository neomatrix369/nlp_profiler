# NLP Profiler [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This is a simple NLP library allows profiling datasets with one or more text columns. 

When given a dataset and a column name with text data, NLP Profiler will return either high-level insights about the text or low-level/granular statistical information about the same text. 

Think of it as using the pandas.describe() function or running Pandas Profiling on your data frame, but for datasets containing text columns rather than columnar datasets.

Under the hood it does make use of a number of libraries that are popular in the AI and ML communities.

A simple notebook have been provided to illustrate the usage of the library.

## Requirements

- Python 3.7.x or higher
- Dependencies described in the requirements.txt

## Get started

### Notebooks

#### Jupyter

See [Jupyter Notebook](./notebooks/jupyter/nlp_profiler.ipynb)

#### Google Colab

You can open these notebooks directly in [Google Colab](./notebooks/google-colab/nlp_profiler.ipynb)

#### Kaggle kernels

**[Notebook/Kernel](https://www.kaggle.com/neomatrix369/nlp-profiler-simple-dataset)** | [Script](https://www.kaggle.com/neomatrix369/nlp-profiler-class) | [Other related links](https://www.kaggle.com/general/166954)

![](https://user-images.githubusercontent.com/1570917/88474968-8fb48980-cf23-11ea-944d-0a1069174ede.png)

## Installation

```bash
pip install git+https://github.com/neomatrix369/nlp-profiler.git@master
```

## Usage

```python
import nlp_profiler as nlpprof

new_text_column_dataset = nlpprof.apply(dataset['text_column'])
```

See [Notebooks](#Notebooks) section for further illustrations.

# Contributing

Contributions are very welcome, please share back with the wider community (and get credited for it)!

Please have a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines, also have a read about our [licensing](LICENSE.md) (and warranty) policy.

---

Go to the [NLP page](https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/natural-language-processing/README.md)</br>