import re

from nlp_profiler.constants import NaN


### Alphanumeric
def gather_alpha_numeric(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall('[A-Za-z0-9]', text)


def count_alpha_numeric(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_alpha_numeric(text))
