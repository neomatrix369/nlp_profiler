import re

from nlp_profiler.constants import NaN


### Non-alphanumeric
def gather_non_alpha_numeric(text: str) -> list:
    return re.findall("[^A-Za-z0-9]", text) if isinstance(text, str) else []


def count_non_alpha_numeric(text: str) -> int:
    return len(gather_non_alpha_numeric(text)) if isinstance(text, str) else NaN
