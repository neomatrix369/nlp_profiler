# Changelog

Changelog for nlp_profiler.

## 0.0.1

### GitHub branch `test-python-3.6-compatibility` enable support for Python 3.6

Based on the issue raised on GitHub [#1](https://github.com/neomatrix369/nlp_profiler/issues/1)

[b2a002a](https://github.com/neomatrix369/nlp_profiler/commit/b2a002a) - [4f117a6](https://github.com/neomatrix369/nlp_profiler/commit/4f117a6) [@neomatrix369](https://github.com/neomatrix369) _Wed Sep 16 17:15:29 2020 +0100_

---

### GitHub branch `create-test-cases` write tests to verify implementation and for test coverage

[6bdc799](https://github.com/neomatrix369/nlp_profiler/commit/6bdc799) - [4c49ae5](https://github.com/neomatrix369/nlp_profiler/commit/4c49ae5) [@neomatrix369](https://github.com/neomatrix369) _Thu Sep 17 17:27:14 2020 +0100_

---

### GitHub branch `add-progress-bars` add progress bars to the various levels of transformation for better UX/UI experience

Based on the issue raised on GitHub [#3](https://github.com/neomatrix369/nlp_profiler/issues/3) - although only implements progress bars at the first and second levels of iterations, pending level 3 iteration (row/record level)

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

For performance metrics before and after changes see this [comment](https://github.com/neomatrix369/nlp_profiler/issues/2#issuecomment-696675059) on GitHub issue [#2](https://github.com/neomatrix369/nlp_profiler/issues/2).

[00a68e2](https://github.com/neomatrix369/nlp_profiler/commit/00a68e2) - [1ff5082](https://github.com/neomatrix369/nlp_profiler/commit/1ff5082) [@neomatrix369](https://github.com/neomatrix369) _Fri Sep 18 14:09:12 2020 +0100_

---

## 0.0.1-dev

### GitHub branch `create-update-release` releasing NLP Profiler on GitHub and PyPi

Just releasing to GitHub under the Releases tab and on PyPi

[d5d0bc1](https://github.com/neomatrix369/nlp_profiler/commit/d5d0bc1) - [6510131](https://github.com/neomatrix369/nlp_profiler/commit/6510131) [@neomatrix369](https://github.com/neomatrix369) _Sun Sep 27 11:56:48 2020 +0100
_

---

## 0.0.2

### GitHub branch `scale-when-applied-to-larger-datasets` Improving performance of Grammar check on large datasets

Tweaking the Grammar check function to perform better than the previous version

[81d055f](https://github.com/neomatrix369/nlp_profiler/commit/81d055f) - [2e311f7](https://github.com/neomatrix369/nlp_profiler/commit/2e311f7) [@neomatrix369](https://github.com/neomatrix369) _Sat Oct 3 07:57:39 2020 +0100_


---

### GitHub branch `ci-cd-github-action` Automate CI/CD process on GitHub

Enable running tests with coverage when a new PR is created or commits are pushed to the repo, across Linux and Windows instances.

Producing the Code coverage report with each commit. And uploading the artifacts to GitHub.

[a806716](https://github.com/neomatrix369/nlp_profiler/commit/a806716bdc0312509ee55d7dfb5e26769493a46b) - [7e4ca87](https://github.com/neomatrix369/nlp_profiler/commit/7e4ca8756bfd73d0b7f805d3c19e536bf0d7e266) [@neomatrix369](https://github.com/neomatrix369) _Thu Oct 15 16:50:59 2020 +0100_

---

## 0.0.3

### GitHub branch `add-docs-for-developers` and `add-github-templates` Update docs for Developers and Add Github templates for issues and pull request

To improve communication with developers and also to create a streamlined process for the same, docs and templates have been added and updated to the repo. These do not change the functionality of the library in any form or shape.

[6d40570](https://github.com/neomatrix369/nlp_profiler/commit/6d4057057c00dd9b359429e40941d0fee15313ee) - [6d40570](https://github.com/neomatrix369/nlp_profiler/commit/6d4057057c00dd9b359429e40941d0fee15313ee) [@neomatrix369](https://github.com/neomatrix369) _Sat Oct 17 19:24:30 2020 +0100_

---


### GitHub branch `addNounPhraseCount` Add noun phrase count in text data

Count the number of noun phrases in the text data and return it as part of granular features.

Thanks, @ritikjain51 for your contribution originally via PR #13, which was fixed and refactored via PR #47.

[f8a22ba](https://github.com/neomatrix369/nlp_profiler/commit/f8a22baf24c39e58f2c8f7cb3faecdb6b87f8462) - [fcd706b](https://github.com/neomatrix369/nlp_profiler/commit/fcd706b39bc426532ad0ccc72d434bda6668bd72) [@neomatrix369](https://github.com/neomatrix369) _Wed Oct 21 13:40:20 2020 +0100_

---

### GitHub branch `ci-cd-github-action` Fix GitHub to run on Windows instances

Now the build and test action runs on Windows instances as well. Fixes issue reported via #21.

[5e7f999](https://github.com/neomatrix369/nlp_profiler/commit/5e7f99910da27a65237abcae9c409e1b3d462db9) [@neomatrix369](https://github.com/neomatrix369) _Sat Oct 24 16:43:49 2020 +0100_

---

### GitHub branch `add-spacy-version-dependency-for-conda` Add spacy related docs info for Conda users

Conda user(s) could not install the library using the `pip install` this is now possible following the docs on the [README](./README.md) page. 
Fixes issue #57 via PR https://github.com/neomatrix369/nlp_profiler/pull/58

[ae91f5c](https://github.com/neomatrix369/nlp_profiler/commit/ae91f5c) [@neomatrix369](https://github.com/neomatrix369) _Sun Dec 13 10:17:17 2020 +0000_

---

### GitHub branch `indicate-ease-of-reading-of-text` High-level feature: Indicate ease of reading of text

Just like spelling check and grammar checks, adding a high-level feature to indicate if a block of text is easy to read or not, based on the library textstat's flesch_reading_ease().

It returns values between 0 and 100 (I have seen values go past 0 and 100 depending on how bad or good the text is).

[4919a51](https://github.com/neomatrix369/nlp_profiler/commit/4919a51) [@neomatrix369](https://github.com/neomatrix369) _Sun Dec 13 18:36:42 2020 +0000_

---

### GitHub branch `add-granular-features` Granular features: Add granular features: count letters, digits, spaces, whitespaces, and punctuations 

Implemented functionality via PR [#60](https://github.com/neomatrix369/nlp_profiler/pull/60) - details described in the body of the PR.
In short, counting repeated letters, digits, spaces, whitespaces, and punctuations in the text. Counting English and 
non-English language characters in the text.  Also, amending existing functionality of punctuations count, digits count 
and fixing a bug in ease of reading scoring.
Housekeeping: removing duplicates, removing cached folders before running tests.


[68bee76](https://github.com/neomatrix369/nlp_profiler/commit/68bee76) [@neomatrix369](https://github.com/neomatrix369) _Sun Dec 27 12:45:59 2020 +0000_

---

### GitHub branch `add-syllables-count` Add granular feature: syllables count applied to text 

Implemented functionality via PR [#61](https://github.com/neomatrix369/nlp_profiler/pull/61) - details described in the body of the PR.

Added new feature(s) to the granular features groups: count syllables extracted from the text provided.

Credits: Gunes Evitan (https://www.kaggle.com/gunesevitan) -- inspired by the discussion on https://www.kaggle.com/c/commonlitreadabilityprize/discussion/238375

[498338e](https://github.com/neomatrix369/nlp_profiler/commit/498338e) [@neomatrix369](https://github.com/neomatrix369) _Sat May 15 00:50:01 2021 +0100_

---

### GitHub branch `moving-notebooks-to-github-release` Moving notebooks to github releases

Implemented functionality via PR [#62](https://github.com/neomatrix369/nlp_profiler/pull/62) - details described in the body of the PR.

Moving notebooks to github releases from the `notebooks` folder to prevent Github from misclassifying the repo/library.

[5ba447e](https://github.com/neomatrix369/nlp_profiler/commit/5ba447ee0ea94c01133f6b9f5923a536720e225a) [@neomatrix369](https://github.com/neomatrix369) _Sat Nov 13 21:02:21 2021 +0000_

---

### GitHub branch `fix-failing-high-level-tests` Make the acceptance tests pass, fixing dependency versions

Implemented functionality via PR [#63](https://github.com/neomatrix369/nlp_profiler/pull/63) - details described in the body of the PR.

Fixing dependency issues leading to tests to fail as API changes in the respective libraries i.e. `language_tool_python` and `pandas`.


[5b87b03](https://github.com/neomatrix369/nlp_profiler/commit/5b87b032a213224f2734e5a6f8b1188772ec38f0) [@neomatrix369](https://github.com/neomatrix369) _Sat Nov 13 23:35:38 2021 +0000_

---

### GitHub branch `correct-spelling-of-column-to-noun-phrase` Granular features: corrected the name of the new feature column to noun phrase

Implemented functionality via PR [#64](https://github.com/neomatrix369/nlp_profiler/pull/64) - details described in the body of the PR.

Correct the misspelt term "noun phrase" or "noun phrases" across the codebase

[a9d1e1a](https://github.com/neomatrix369/nlp_profiler/commit/a9d1e1a5560c4dcd82922470b4933ea75de77dad) [@neomatrix369](https://github.com/neomatrix369) _Sat Nov 13 21:41:56 2021 +0000_

---

### GitHub branch `enabled-nightly-builds` Github actions: enabled nightly run of build and test

Implemented functionality via PR [#65](https://github.com/neomatrix369/nlp_profiler/pull/65) - details described in the body of the PR.

Enabled nightly run of build and test via Github actions

[dde3172](https://github.com/neomatrix369/nlp_profiler/commit/dde31723b7cb1c1105b9df828bf7429094113de4) [@neomatrix369](https://github.com/neomatrix369) _Sun Nov 14 09:12:33 2021 +0000_

---
### GitHub branch `grammar_check` Grammar_quality_check: language tool replaced with Gingerit

Implemented functionality via PR [#69](https://github.com/neomatrix369/nlp_profiler/pull/69) - details described in the body of the PR.

Replaced language tool with Gingerit for faster calculations

[b5a5dda](https://github.com/neomatrix369/nlp_profiler/pull/69/commits/b5a5ddaad01f07230cf232712671d43dd9db9862) [@bitanb1999](https://github.com/bitanb1999) _Sun March 13 00:31:31 2023 +0000_

---

### GitHub branch `revert-76-sourcery/revert-71-spelling_check` Granular features: reverted change made to spell checks

Implemented functionality via PR [#75](https://github.com/neomatrix369/nlp_profiler/pull/75) - details described in the body of the PR.

Reverting spell check functionality as it is not tested and tests change/break with new implementation.

[2cddf51](https://github.com/neomatrix369/nlp_profiler/commit/2cddf51a605b434d12604d2dba9457c415808bfe) [@neomatrix369](https://github.com/neomatrix369) _Mon Mar 13 02:56:40 2023 +0000_

---

### GitHub branch `reformating-code-and-minor-fixes` Reformatting code, refactoring as per Sourcery, minor fixes and test fixes

Implemented functionality via PR [#73](https://github.com/neomatrix369/nlp_profiler/pull/73) - details described in the body of the PR.

Reformatting code, refactoring as per Sourcery, minor fixes and test fixes. Bringing back the build system in order. Fixes old regressed tests.

[7caeb47](https://github.com/neomatrix369/nlp_profiler/commit/7caeb47e3795a22c1884731320a02d4b0c39ca0c) [@neomatrix369](https://github.com/neomatrix369) _Mon Mar 13 11:23:49 2023 +0000_

---

Return to [README.md](README.md)
