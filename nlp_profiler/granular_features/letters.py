import re

from nlp_profiler.constants import NaN


### Alphanumeric
def gather_repeated_letters(text: str) -> list:
    return re.findall("(([a-zA-Z])\\2{2,})", text) if isinstance(text, str) else []


def count_repeated_letters(text: str) -> int:
    return len(gather_repeated_letters(text)) if isinstance(text, str) else NaN
