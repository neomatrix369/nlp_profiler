import re

# https://www.journaldev.com/23788/python-string-module
import string as string_module

from nlp_profiler.constants import NaN


def count_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    spaces = re.findall(r" ", text)
    return len(spaces)


# ' \t\n\r\x0b\x0c'
def count_whitespaces(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    spaces = re.findall(f"(([{string_module.whitespace}" + "]){1})", text)
    return len(spaces)


def count_characters_excluding_spaces(text: str) -> int:
    return len(text) - count_spaces(text) if isinstance(text, str) else NaN


def count_characters_excluding_whitespaces(text: str) -> int:
    return len(text) - count_whitespaces(text) if isinstance(text, str) else NaN


def count_chars(text: str) -> int:
    return len(text) if isinstance(text, str) else NaN


def gather_repeated_spaces(text: str) -> list:
    return re.findall("(([ ])\\2{1,})", text) if isinstance(text, str) else NaN


def count_repeated_spaces(text: str) -> int:
    return len(gather_repeated_spaces(text)) if isinstance(text, str) else NaN


# ' \t\n\r\x0b\x0c'
def gather_repeated_whitespaces(text: str) -> list:
    return (
        re.findall(f"(([{string_module.whitespace}" + "])\\2{1,})", text)
        if isinstance(text, str)
        else NaN
    )


def count_repeated_whitespaces(text: str) -> int:
    return len(gather_repeated_whitespaces(text)) if isinstance(text, str) else NaN
