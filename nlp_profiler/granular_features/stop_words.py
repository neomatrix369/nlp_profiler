import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nlp_profiler.constants import NaN

nltk.download("stopwords")
nltk.download("punkt")
STOP_WORDS = set(stopwords.words("english"))


### Stop words
def gather_stop_words(text: str) -> list:
    if not isinstance(text, str):
        return []

    word_tokens = word_tokenize(text)
    return [word for word in word_tokens if word in STOP_WORDS]


def count_stop_words(text: str) -> int:
    return len(gather_stop_words(text)) if isinstance(text, str) else NaN
