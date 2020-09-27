# NLP Profiler [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A simple NLP library allows profiling datasets with one or more text columns. 

NLP Profiler returns either high-level insights or low-level/granular statistical information about the text when given a dataset and a column name containing text data, in that column. 

In short: Think of it as using the `pandas.describe()` function or running [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) on your data frame, but for datasets containing text columns rather than the usual columnar datasets.

## What do you get from the library?

- Input a Pandas dataframe series as input paramater.
- You get back a new dataframe with various features about the parsed text per row.
  - high-level: sentiment analysis, objectivity/subjectivity analysis, spelling quality check, grammar quality check, etc...
  - low-level/granular: number of characters in the sentence, number of words, number of emojis, number of words, etc...
- From the above numerical data in the resulting dataframe descriptive statistics can be drawn using the `pandas.describe()` on the dataframe.

See screenshots under the [Jupyter](#Jupyter) section and also under [Screenshots](#Screenshots) for further illustrations.

Under the hood it does make use of a number of libraries that are popular in the AI and ML communities, but we can extend it's functionality by replacing or adding other libraries as well.

A simple [notebook](#Notebooks) have been provided to illustrate the usage of the library.

_**Note:** this is a new endeavour and it's may have rough edges i.e. probably NOT capable of doing many things atm. _Many of these gaps are opportunities we can work on and plug, as we go along using it. Please provide constructive feedback to help with the improvement of this library. We just recently achieved this with [scaling with larger datasets](https://github.com/neomatrix369/nlp_profiler/issues/2#issuecomment-696675059)._

## Requirements

- Python 3.6.x or higher.
- Dependencies described in the `requirements.txt`.
- High-level including Grammar checks:
  - faster processor
  - higher RAM capacity
- (Optional)
  - Jupyter Lab (on your local machine).
  - Google Colab account.
  - Kaggle account.
  - Grammar check functionality:
    - Internet access
    - Java 8 or higher
  
## Getting started

### Demo

Look at this short demo of the NLP Profiler library by clicking on the below image: 
[![Demo of the NLP Profiler library](https://user-images.githubusercontent.com/1570917/88474968-8fb48980-cf23-11ea-944d-0a1069174ede.png)](https://youtu.be/sdPOyqMfK7M?t=2274)or you find the rest of the [talk here](https://www.youtube.com/watch?v=sdPOyqMfK7M).

## Installation

From the GitHub repo:

```bash
pip install git+https://github.com/neomatrix369/nlp_profiler.git@master
```

From the source (only for development purposes):

```bash
git clone https://github.com/neomatrix369/nlp_profiler
cd nlp_profiler
```

```
python setup.py install
```
or 

```
pip install -e .
```

or 

```
pip install --prefix .
```

## Usage

```python
import nlp_profiler.core as nlpprof

new_text_column_dataset = nlpprof.apply_text_profiling(dataset, 'text_column')
```

or 

```python
from nlp_profiler.core import apply_text_profiling

new_text_column_dataset = apply_text_profiling(dataset, 'text_column')
```

See [Notebooks](#Notebooks) section for further illustrations.

## Notebooks

_After succesful installation of the library, RESTART Jupyter kernels or Google Colab runtimes for the changes to take effect._

### Jupyter

See [Jupyter Notebook](./notebooks/jupyter/nlp_profiler.ipynb)

![](https://user-images.githubusercontent.com/1570917/88475060-73651c80-cf24-11ea-8c44-21352f7be5bc.png)

### Google Colab

You can open these notebooks directly in [Google Colab](./notebooks/google-colab/nlp_profiler.ipynb)

### Kaggle kernels

**[Notebook/Kernel](https://www.kaggle.com/neomatrix369/nlp-profiler-simple-dataset)** | [Script](https://www.kaggle.com/neomatrix369/nlp-profiler-class) | [Other related links](https://www.kaggle.com/general/166954)

## Screenshots

![Importing the library](https://user-images.githubusercontent.com/1570917/92324238-ccea5c00-f037-11ea-9369-89b0e034ef16.png)

---

![Pandas describe() function](https://user-images.githubusercontent.com/1570917/92324242-cf4cb600-f037-11ea-9c5a-e22806b4be5b.png)

# Credits and supporters

See [CREDITS_AND_SUPPORTERS.md](./CREDITS_AND_SUPPORTERS.md)

# Changes

See [CHANGELOG.md](./CHANGELOG.md)

# License

Refer [licensing](LICENSE.md) (and warranty) policy.

# Contributing

Contributions are Welcome!

Please have a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines.

Please share it with the wider community (and get credited for it)!

---

Go to the [NLP page](https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/natural-language-processing/README.md)</br>
