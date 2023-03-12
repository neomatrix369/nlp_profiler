import re

# https://www.journaldev.com/23788/python-string-module
import string as string_module

from nlp_profiler.constants import NaN

ADDITIONAL_SYMBOLS = "£€±§"


### Punctuations
def gather_punctuations(text: str) -> list:
    if not isinstance(text, str):
        return []

    line = re.findall("[" + string_module.punctuation + ADDITIONAL_SYMBOLS + "]*", text)
    string = "".join(line)
    return list(string)


def count_punctuations(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_punctuations(text))


def gather_repeated_punctuations(text: str) -> list:
    if not isinstance(text, str):
        return []

    ### Gather 2 or more repeated punctuations
    return re.findall(r"(([\\" + string_module.punctuation + ADDITIONAL_SYMBOLS + "])\\2{1,})", text)


def count_repeated_punctuations(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_repeated_punctuations(text))
