import re

from nlp_profiler.constants import NaN


### Count words
def gather_words(text: str) -> list:
    return re.findall(r"\b[^\d\W]+\b", text) if isinstance(text, str) else []


def count_words(text: str) -> int:
    return len(gather_words(text)) if isinstance(text, str) else NaN
