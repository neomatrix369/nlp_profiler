import re

from nlp_profiler.constants import NaN


### Numbers
def gather_whole_numbers(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall(r'[0-9]+', text)


def count_whole_numbers(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_whole_numbers(text))
