# NLP Profiler 

||| [![Gitter](https://badges.gitter.im/nlp_profiler/community.svg)](https://gitter.im/nlp_profiler/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) |||
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub actions](https://github.com/neomatrix369/nlp_profiler/workflows/end-to-end-flow/badge.svg)](https://github.com/neomatrix369/nlp_profiler/actions?workflow=end-to-end-flow)
[![Code coverage](https://codecov.io/gh/neomatrix369/nlp_profiler/branch/master/graph/badge.svg)](https://codecov.io/gh/neomatrix369/nlp_profiler)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai) 
[![Codeac](https://static.codeac.io/badges/2-293235950.svg "Codeac.io")](https://app.codeac.io/github/neomatrix369/nlp_profiler)
[![PyPI version](https://badge.fury.io/py/nlp-profiler.svg)](https://badge.fury.io/py/nlp-profiler) 
[![Python versions](https://img.shields.io/pypi/pyversions/nlp_profiler.svg)](https://pypi.org/project/nlp_profiler/) 
[![PyPi stats](https://img.shields.io/pypi/dm/nlp_profiler.svg?label=pypi%20downloads&logo=PyPI&logoColor=white)](https://pypistats.org/packages/nlp_profiler)
[![Downloads](https://static.pepy.tech/personalized-badge/nlp-profiler?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/nlp-profiler)


A simple NLP library that allows profiling datasets with one or more text columns. 

NLP Profiler returns either high-level insights or low-level/granular statistical information about the text when given a dataset and a column name containing text data, in that column. 

In short: Think of it as using the `pandas.describe()` function or running [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) on your data frame, but for datasets containing text columns rather than the usual columnar datasets.

# Table of contents

- **Community/Chat/Communication:** [![Gitter](https://badges.gitter.im/nlp_profiler/community.svg)](https://gitter.im/nlp_profiler/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
- [What do you get from the library?](#what-do-you-get-from-the-library)
- [Requirements](#requirements)
- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Developer guide](#developer-guide)
  - [Demo and presentations](#Demo-and-presentations)
- [Notebooks](#notebooks)
- [Screenshots](#screenshots)
- [Credits and supporters](#credits-and-supporters)
- [Changes](#changes)
- [License](#license)
- [Contributing](#contributing)

---

## What do you get from the library?

- Input a Pandas dataframe series as an input parameter.
- You get back a new dataframe with various features about the parsed text per row.
  - High-level: sentiment analysis, objectivity/subjectivity analysis, spelling quality check, grammar quality check, ease of readability check, etc...
  - Low-level/granular: number of characters in the sentence, number of words, number of emojis, number of words, etc...
- From the above numerical data in the resulting dataframe descriptive statistics can be drawn using the `pandas.describe()` on the dataframe.

See screenshots under the [Jupyter](#Jupyter) section and also under [Screenshots](#Screenshots) for further illustrations.

Under the hood it does make use of a number of libraries that are popular in the AI and ML communities, but we can extend it's functionality by replacing or adding other libraries as well.

A simple [notebook](#Notebooks) have been provided to illustrate the usage of the library.

**_Please join the [Gitter.im community](https://gitter.im/nlp_profiler/community) and say "hello" to us, share your feedback, have a fun time with us._**

**Note:** _this is a new endeavour and it may have rough edges i.e. NLP_Profiler in its current version is probably NOT capable of doing many things. Many of these gaps are opportunities we can work on and plug, as we go along using it. Please provide constructive feedback to help with the improvement of this library. We just recently achieved this with [scaling with larger datasets](https://github.com/neomatrix369/nlp_profiler/issues/2#issuecomment-696675059)._

## Requirements

- Python 3.6.x or higher.
- Dependencies described in the `requirements.txt`.
- High-level including Grammar checks:
  - faster processor
  - higher RAM capacity
  - working disk-space of 1 to 3 GBytes (depending on the dataset size)
- (Optional)
  - Jupyter Lab (on your local machine).
  - Google Colab account.
  - Kaggle account.
  - Grammar check functionality:
    - Internet access
    - Java 8 or higher
  
## Getting started

### Installation

**For Conda/Miniconda environments:**

```bash
conda config --set pip_interop_enabled True
pip install "spacy >= 2.3.0,<3.0.0"         # in case spacy is not present
python -m spacy download en_core_web_sm

### now perform any of the below pathways/options
```

**For Kaggle environments:**

```
pip uninstall typing      # this can cause issues on Kaggle hence removing it helps
```

_Follow any of the remaining installation steps but "avoid" using `-U` with `pip install` -- again this can cause issues on Kaggle hence not using it helps_.

**From PyPi:**

```bash
pip install -U nlp_profiler
```

**From the GitHub repo:**

```bash
pip install -U git+https://github.com/neomatrix369/nlp_profiler.git@master
```

**From the source:**

For library development purposes, see [Developer guide](#developer-guide)

### Usage

```python
import nlp_profiler.core as nlpprof

new_text_column_dataset = nlpprof.apply_text_profiling(dataset, 'text_column')
```

or 

```python
from nlp_profiler.core import apply_text_profiling

new_text_column_dataset = apply_text_profiling(dataset, 'text_column')
```

See [Notebooks](./notebooks/README.md) section for further illustrations.

### Developer guide

See [Developer guide](developer-guide.md) to know how to build, test, and contribute to the library.

### Demo and presentations

Look at a short demo of the NLP Profiler library at one of these:

<table>
  <tr>
    <td align="center"><a href="https://youtu.be/sdPOyqMfK7M?t=2274"><img alt="Demo of the NLP Profiler library (Abhishek talks #6)" src=https://user-images.githubusercontent.com/1570917/88474968-8fb48980-cf23-11ea-944d-0a1069174ede.png></a> or you find the rest of the <a href=https://www.youtube.com/watch?v=sdPOyqMfK7M>talk here</a> or here for <a href="https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/presentations/awesome-ai-ml-dl/02-abhishektalks-2020/README.md">slides</a></td>
<td>
  <td align="center"><a href="https://youtu.be/wHIcQWeOugI?t=808"><img alt="Demo of the NLP Profiler library (NLP Zurich talk)" src=https://secure.meetupstatic.com/photos/event/5/7/3/highres_492541395.jpeg></a> or you find the rest of the <a href=https://www.youtube.com/watch?v=wHIcQWeOugI>talk here</a> or here for <a href="https://github.com/neomatrix369/nlp_profiler/blob/master/presentations/01-nlp-zurich-2020/README.md">slides</a></td>
  
  </tr>
</table>

## Notebooks

After successful installation of the library, RESTART Jupyter kernels or Google Colab runtimes for the changes to take effect.

See [Notebooks](./notebooks/README.md) for usage and further details.

## Screenshots

See [Screenshots](./notebooks/README.md#screenshots)

## Credits and supporters

See [CREDITS_AND_SUPPORTERS.md](./CREDITS_AND_SUPPORTERS.md)

## Changes

See [CHANGELOG.md](./CHANGELOG.md)

## License

Refer [licensing](LICENSE.md) (and warranty) policy.

## Contributing

Contributions are Welcome!

Please have a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines.

Please share it with the wider community (and get credited for it)!

---

Go to the [NLP page](https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/natural-language-processing/README.md)</br>
