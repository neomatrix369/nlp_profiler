import re

from nlp_profiler.constants import NaN


### Punctuations
def gather_punctuations(text: str) -> list:
    if not isinstance(text, str):
        return []

    line = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string = "".join(line)
    return list(string)


def count_punctuations(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_punctuations(text))
