import re

from nlp_profiler.constants import NaN


### Numbers
def gather_whole_numbers(text: str) -> list:
    return re.findall(r"[0-9]+", text) if isinstance(text, str) else []


def count_whole_numbers(text: str) -> int:
    return len(gather_whole_numbers(text)) if isinstance(text, str) else NaN


def gather_digits(text: str) -> list:
    return re.findall("[0-9]", text) if isinstance(text, str) else []


def count_digits(text: str) -> int:
    return len(gather_digits(text)) if isinstance(text, str) else NaN


def gather_repeated_digits(text: str) -> list:
    return re.findall("(([0-9])\\2{1,})", text) if isinstance(text, str) else []


def count_repeated_digits(text: str) -> int:
    return len(gather_repeated_digits(text)) if isinstance(text, str) else NaN
