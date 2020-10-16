To be able to merge a pull request, there are a few checks:

TL;DR

[ ] clear title and description to the Pull Request has been provided
[ ] you have read the [Contributing doc](https://github.com/neomatrix369/nlp_profiler/blob/master/CONTRIBUTING.md) and [Developer Guide](https://github.com/neomatrix369/nlp_profiler/blob/master/developer-guide.md)
[ ] the pull request should pass the tests (`./test-coverage "tests slow-tests"``) - this will be visible via the Code coverage report and CI/CD task on the Pull Request
[ ] you have performed some kind of smoke test by running your changes in an isolated environment i.e. Docker container, Google Colab, Kaggle, etc...
[ ] the notebooks are updated (see `notebooks` folder)    
[ ] `CHANGELOG.md` has been updated (please follow the existing format)


## Goal or purpose of the PR

{ Short description outlining what the Pull Request does, and reference the related GitHub issue(s):
  - describe the impact of the change in this PR to the _user_ of this repository (e.g. end user, contributor, developer).
  - describe the new behaviour in _present tense_, and the old behaviour and how it's been changed in _past tense_.

## Changes implemented in the PR

{ Please explain what you implemented, why your changes are the best way to achieve the goal(s) above. Also please describe a high-level flow of the implementation and if necessary add some code-level details. If possible provide examples, screen-shots or references to other resources.

This would allow the reviewer to understand your intentions in the code much better.}