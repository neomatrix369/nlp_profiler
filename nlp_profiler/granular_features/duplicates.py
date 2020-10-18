from itertools import groupby

from nltk.tokenize import word_tokenize

from nlp_profiler.constants import NaN


### Number of characters without spaces
def gather_duplicates(text: str) -> dict:
    if not isinstance(text, str):
        return []

    tokenized_text = word_tokenize(text.lower())
    sorted_tokenized_text = sorted(tokenized_text)
    duplicates = {}
    for _, (value, group) in enumerate(groupby(sorted_tokenized_text)):
        frequency = len(list(group))
        if frequency > 1:
            duplicates.update({value: frequency})

    return duplicates


### Duplicates
def count_duplicates(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_duplicates(text))
