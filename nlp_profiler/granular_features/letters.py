import re

from nlp_profiler.constants import NaN


### Alphanumeric
def gather_repeated_letters(text: str) -> list:
    if not isinstance(text, str):
        return []

    ### Gather 3 or more repeated letters
    return re.findall("(([a-zA-Z])\\2{2,})", text)


def count_repeated_letters(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_repeated_letters(text))
