import re

from nlp_profiler.constants import NaN


### Numbers
def gather_whole_numbers(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall(r"[0-9]+", text)


def count_whole_numbers(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_whole_numbers(text))


def gather_digits(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall("[0-9]", text)


def count_digits(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_digits(text))


def gather_repeated_digits(text: str) -> list:
    if not isinstance(text, str):
        return []

    ### Gather 2 or more repeated digits
    return re.findall("(([0-9])\\2{1,})", text)


def count_repeated_digits(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_repeated_digits(text))
