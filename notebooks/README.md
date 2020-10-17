# Notebooks

# Table of contents

- [Requirements](#requirements)
- [How to update the notebooks?](#how-to-update-the-notebooks)
- [Jupyter](#jupyter)
- [Google Colab](#google-colab)
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

## How to update the notebooks?

In order to change the notebooks:

- First run `jupyter` by doing the following:

```
$ cd jupyter
```

```
$ jupyter labs .

or

$ jupyter notebook .
```

- Regenerate the notebooks by running all the cells. 
- Once you are happy, then commit your changes.
- Push commits to remote branch
- Create pull request

## Jupyter

See [Jupyter Notebook](./jupyter/nlp_profiler.ipynb)

![](https://user-images.githubusercontent.com/1570917/88475060-73651c80-cf24-11ea-8c44-21352f7be5bc.png)

## Google Colab

You can open these notebooks directly in [Google Colab](./google-colab/nlp_profiler.ipynb)

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
