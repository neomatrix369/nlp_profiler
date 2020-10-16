---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**

<!--
A clear and concise description of what the bug is.
If the description consists of multiple non-related bugs, you are encouraged to create separate issues.

Try to ellaborate wth examples with text, code-snippets, visuals or links to resources.

Note: In case the issue is small enough that a few lines of code (or small changes to the code-base) would fix the issue then please just raise a Pull Request with your changes. We can discuss the issue there.
-->

**To Reproduce**

<!--
We would need to reproduce your scenario before being able to resolve it. 

_Data:_
Please share your dataframe. 
If the data is confidential, for example when it contains company-sensitive information, provide us with a synthetic or open dataset that produces the same error. 
You should provide the DataFrame structure, for example by reporting the output of `df.info()`. 
You can anonymize the column names if necessary.

_Code:_ Preferably, use this code format:
```python
"""
Test for issue XXX:
https://github.com/neomatrix369/nlp_profiler/issues/XXX
"""
from nlp_profiler.core import apply_text_profiling


def test_issueXXX():
    df = pd.read_csv(r'<file>')

    # Minimal reproducible code
```
--> 

**Version information:**

<!--
Version information is essential in reproducing and resolving bugs. Please report:

* _Python version_: Your exact Python version.
* _Environment_: Where do you run the code? Command line, IDE (PyCharm, Spyder, IDLE etc.), Jupyter Notebook (Colab or local)
* _`pip`_: If you are using `pip`, run `pip freeze` in your environment and report the results. The list of packages can be rather long, you can use the snippet below to collapse the output.

<details><summary>Click to expand <strong><em>Version information</em></strong></summary>
<p>

```
<<< Put your version information here >>>
```

</p>
</details>
-->

**Additional context**

<!--
Add any other context about the problem here. Usually logs or screen output captured in the form of screenshots or just a copy-paste of the text helps. Sharing a link to where you are using the library (i.e. Google colab or Kaggle kernel or some other location).
-->