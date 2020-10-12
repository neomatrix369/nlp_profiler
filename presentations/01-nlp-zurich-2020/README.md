## Profiling Text Data

### Slides

See [slides (PDF)](NLP_Profiler_Profiling_textual_datasets.pdf)

### Video

See [on YouTube](https://www.youtube.com/watch?v=wHIcQWeOugI)

### Speaker

- [Mani Sarkar](http://github.com/neomatrix369) | [About me](https://neomatrix369.wordpress.com/about)

### Abstract

Natural language processing (NLP) is a widespread field with many new innovations and advancements. Despite that, at a very basic level, there are no comprehensive tools to analyze tabular text data. So, we all end up building our own little solutions to analyze text datasets. Each one of us might do it differently and get a different response.

While preparing for a talk sometime back, I wrote a utility called NLP Profiler. When given a dataset and a column name with text data, NLP Profiler will return either high-level insights about the text or low-level/granular statistical information about the same text. Think of it as using the pandas.describe() function or running Pandas Profiling on your data frame, but for datasets containing text columns rather than columnar datasets.

In this talk, we can see what profiling means to us, it is important and how it can be applied to datasets to get some interesting information i.e. High-level information that would include things like sentiment analysis, subjectivity/objectivity analysis, grammar or spelling quality check, etc. Low-level details could include the number of words in the sentence, the number of emojis in the text, etc.

NLP Profiler can do this analysis using a single line of code. Above all, it can be extended and shared openly with others.