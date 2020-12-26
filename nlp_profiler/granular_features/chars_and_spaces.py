import re

from nlp_profiler.constants import NaN


### Number of spaces
def count_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    spaces = re.findall(r' ', text)
    return len(spaces)


def count_characters_excluding_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(text) - count_spaces(text)


def count_chars(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(text)


def gather_repeated_spaces(text: str) -> list:
    if not isinstance(text, str):
        return NaN

    return re.findall('(([ ])\\2{1,})', text)


def count_repeated_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_repeated_spaces(text))
