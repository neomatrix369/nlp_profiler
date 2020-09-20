import re

from nlp_profiler.constants import NaN


### Sentences
def gather_sentences(text: str) -> list:
    if not isinstance(text, str):
        return []

    lines = re.findall(r'([^.]*[^.]*)', text)
    for index, each in enumerate(lines):
        if each == '':
            del lines[index]

    return lines


def count_sentences(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_sentences(text))
