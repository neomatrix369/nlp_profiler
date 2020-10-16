# Changelog

Changelog for nlp_profiler.

## 0.0.1
### GitHub branch `test-python-3.6-compatibility` enable support for Python 3.6

Based on the issue raised on github [#1](https://github.com/neomatrix369/nlp_profiler/issues/1)

[b2a002a](https://github.com/neomatrix369/nlp_profiler/commit/b2a002a) - [4f117a6](https://github.com/neomatrix369/nlp_profiler/commit/4f117a6) [@neomatrix369](https://github.com/neomatrix369) _Wed Sep 16 17:15:29 2020 +0100_

---

### GitHub branch `create-test-cases` write tests to verify implementation and for test coverage

[6bdc799](https://github.com/neomatrix369/nlp_profiler/commit/6bdc799) - [4c49ae5](https://github.com/neomatrix369/nlp_profiler/commit/4c49ae5) [@neomatrix369](https://github.com/neomatrix369) _Thu Sep 17 17:27:14 2020 +0100_

---

### GitHub branch `add-progress-bars` add progress bars to the various levels of transformation for better UX/UI experience

Based on the issue raised on github [#3](https://github.com/neomatrix369/nlp_profiler/issues/3) - although only implements progress bars at the first and second levels of iterations, pending level 3 iteration (row/record level)

![image](https://user-images.githubusercontent.com/1570917/93523649-42ed9d80-f92b-11ea-9c08-c45914ca0c20.png)

[a83bc23](https://github.com/neomatrix369/nlp_profiler/commit/a83bc23) - [7c72b0e](https://github.com/neomatrix369/nlp_profiler/commit/7c72b0e) [@neomatrix369](https://github.com/neomatrix369) _Thu Sep 17 19:50:30 2020 +0100_

---

### GitHub branch `add-progress-bars` add progress bars to the various levels of transformation for better UX/UI experience

Continuing with the above changes, third-level progress-bar is in place (row-level progress)

[7c72b0e](https://github.com/neomatrix369/nlp_profiler/commit/a83bc23) - [c3ada30](https://github.com/neomatrix369/nlp_profiler/commit/c3ada30) [@neomatrix369](https://github.com/neomatrix369) _Fri Sep 18 13:44:48 2020 +0100_

---

### GitHub pull request https://github.com/neomatrix369/nlp_profiler/pull/9  improve performance of the library when used on larger datasets

Branch `scale-when-applied-to-larger-datasets`

Added parallelisation and some caching to improve the initial slow-down in the performance.

Verification and tests have been performed, although this is a continuous process.

For performance metrics before and after changes see this [comment](https://github.com/neomatrix369/nlp_profiler/issues/2#issuecomment-696675059) on github issue [#2](https://github.com/neomatrix369/nlp_profiler/issues/2).

[00a68e2](https://github.com/neomatrix369/nlp_profiler/commit/00a68e2) - [1ff5082](https://github.com/neomatrix369/nlp_profiler/commit/1ff5082) [@neomatrix369](https://github.com/neomatrix369) _Fri Sep 18 14:09:12 2020 +0100_

---

## 0.0.1-dev

### GitHub branch `create-update-release` releasing NLP Profiler on GitHub and PyPi

Just releasing to GitHub under the Releases tab and on PyPi

[d5d0bc1](https://github.com/neomatrix369/nlp_profiler/commit/d5d0bc1) - [6510131](https://github.com/neomatrix369/nlp_profiler/commit/6510131) [@neomatrix369](https://github.com/neomatrix369) _Sun Sep 27 11:56:48 2020 +0100
_

---

### GitHub branch `scale-when-applied-to-larger-datasets` Improving performance of Grammar check on large datasets

Tweaking the Grammar check function to perform better than the previous version

[81d055f](https://github.com/neomatrix369/nlp_profiler/commit/81d055f) - [2e311f7](https://github.com/neomatrix369/nlp_profiler/commit/2e311f7) [@neomatrix369](https://github.com/neomatrix369) _Sat Oct 3 07:57:39 2020 +0100_


---

### GitHub branch `ci-cd-github-action` Automate CI/CD process on GitHub

Enable running tests with coverage when a new PR is created or commits are pushed to the repo, across Linux and Windows instances.

Producing the Code coverage report with each commit. And uploading the artifacts to GitHub.

[a806716](https://github.com/neomatrix369/nlp_profiler/commit/a806716bdc0312509ee55d7dfb5e26769493a46b) - [7e4ca87](https://github.com/neomatrix369/nlp_profiler/commit/7e4ca8756bfd73d0b7f805d3c19e536bf0d7e266) [@neomatrix369](https://github.com/neomatrix369) _Thu Oct 15 16:50:59 2020 +0100_

---

Return to [README.md](README.md)