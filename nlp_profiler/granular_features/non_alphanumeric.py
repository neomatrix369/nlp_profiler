import re

from nlp_profiler.constants import NaN


### Non-alphanumeric
def gather_non_alpha_numeric(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall('[^A-Za-z0-9]', text)


def count_non_alpha_numeric(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_non_alpha_numeric(text))
