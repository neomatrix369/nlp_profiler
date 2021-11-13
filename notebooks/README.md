# Notebooks

# Table of contents

- [Requirements](#requirements)
- [Download the notebooks](#download-the-notebooks)
- [How to run the notebooks?](#how-to-run-the-notebooks)
- [How to update the notebooks?](#how-to-update-the-notebooks)
- [Jupyter and Google Colab](#jupyter-and-google-colab)
- [Kaggle kernels](#kaggle-kernels)
- [Screenshots](#screenshots)
- [Developer guide](#developer-guide)
- [Contributing](#contributing)

---

## Requirements

The below are required in order to be able to amend the notebooks and update the repo:

- jupyter (notebook or labs)
- `nbdime` plugin for jupyter (notebook or labs): helps with comparing and viewing `git` related changes
- install `pre-commit` in the root of the project folder: `pip install pre-commit`
- enable `pre-commit` in the root of the project folder: `pre-commit install`

You can also run `pre-commit` manually by doing the below:

```
pre-commit run --all
```

(This is automatically run in the CI/CD when commits are pushed and/or pull request is created on the repo).

## Download the notebooks

Go to https://github.com/neomatrix369/nlp_profiler/releases and select the latest release for e.g. https://github.com/neomatrix369/nlp_profiler/releases/tag/v0.0.3 and then download the [notebooks archive (v0.0.3)](https://github.com/neomatrix369/nlp_profiler/releases/download/v0.0.3/nlp_profiler_notebooks.zip) attached to the release.

The archive should contain `.ipynb` files. 

## How to run the notebooks?

In order to run the notebooks:

- Unzip the archive in the current folder
- Then run `jupyter` by doing the following:

```
$ jupyter labs .

or

$ jupyter notebook .
```

## How to update the notebooks?

- In case you wish to add new changes to the notebook, feel free to do so but do note the release/package version for which you are making these changes
- Zip them up and create pull request with the changes in the zipped archive
- Ensure you have done all the testing and checking
- Please maintain the same formatting as in the original notebooks

Why this method? We are not adding `.ipynb` files to this repo as it makes GitHub think the repo is a Jupyter notebook repo and not a `python` language repo.

## Jupyter and Google Colab

The notebooks can be opened in both Jupyter and Google Colab, here is a sample view of what one of the notebook looks like:

![](https://user-images.githubusercontent.com/1570917/88475060-73651c80-cf24-11ea-8c44-21352f7be5bc.png)

## Kaggle kernels

**[Notebook/Kernel](https://www.kaggle.com/neomatrix369/nlp-profiler-simple-dataset)** | [Script](https://www.kaggle.com/neomatrix369/nlp-profiler-class) | [Other related links](https://www.kaggle.com/general/166954)

## Screenshots

![Importing the library](https://user-images.githubusercontent.com/1570917/92324238-ccea5c00-f037-11ea-9369-89b0e034ef16.png)

---

![Pandas describe() function](https://user-images.githubusercontent.com/1570917/92324242-cf4cb600-f037-11ea-9c5a-e22806b4be5b.png)

## Developer guide

See [Developer guide](../developer-guide.md) to know how to build, test, and contribute to the library.

## Contributing

Contributions are Welcome!

Please have a look at the [CONTRIBUTING](../CONTRIBUTING.md) guidelines.

Please share it with the wider community (and get credited for it)!

---

Go to the [Main page](../README.md)
