import re

from nlp_profiler.constants import NaN


### Count words
def gather_words(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall(r'\b[^\d\W]+\b', text)


def count_words(text: str) -> int:
    if not isinstance(text, str):
        return NaN
    return len(gather_words(text))
