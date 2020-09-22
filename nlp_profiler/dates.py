import re

from nlp_profiler.constants import NaN


### Dates
def gather_dates(text: str, date_format: str = 'dd/mm/yyyy') -> list:
    if not isinstance(text, str):
        return []

    ddmmyyyy = r'\b(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/([0-9]{4})\b'
    mmddyyyy = r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b'
    regex_list = {
        'dd/mm/yyyy': ddmmyyyy, 'mm/dd/yyyy': mmddyyyy
    }
    return re.findall(regex_list[date_format], text)


def count_dates(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_dates(text))
