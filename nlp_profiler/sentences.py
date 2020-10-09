from nltk import sent_tokenize

from nlp_profiler.constants import NaN


### Sentences
def gather_sentences(text: str) -> list:
    if not isinstance(text, str):
        return []

    return sent_tokenize(text)


def count_sentences(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_sentences(text))
