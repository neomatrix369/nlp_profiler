import math
import tempfile

import pandas as pd
from joblib import Memory
from nltk.tokenize import word_tokenize
from textblob import Word

from nlp_profiler.constants import \
    DEFAULT_PARALLEL_METHOD
from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.constants import \
    SPELLING_QUALITY_SCORE_COL, SPELLING_QUALITY_COL, SPELLING_QUALITY_SUMMARISED_COL
from nlp_profiler.generate_features import generate_features

memory = Memory(tempfile.gettempdir(), compress=9, verbose=0)


def apply_spelling_check(heading: str,
                         new_dataframe: pd.DataFrame,
                         text_column: dict,
                         parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    spelling_checks_steps = [
        (SPELLING_QUALITY_SCORE_COL, text_column, spelling_quality_score),
        (SPELLING_QUALITY_COL, SPELLING_QUALITY_SCORE_COL, spelling_quality),
        (SPELLING_QUALITY_SUMMARISED_COL, SPELLING_QUALITY_COL, spelling_quality_summarised),
    ]
    generate_features(
        heading, spelling_checks_steps,
        new_dataframe, parallelisation_method
    )


### Spell check
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
spelling_quality_score_to_words_mapping = [
    ["Very good", 99, 100],  # Very good: Certain: 100%: Give or take 0%
    ["Quite good", 97, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Good", 95, 97],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Pretty good", 90, 95],  # Pretty: Good: Probable: 75%: Give or take about 12%
    ["Bad", 60, 90],  # So/so: Chances About Even: 50%: Give or take about 10%
    ["Pretty bad", 12, 60],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    ["Quite bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
    ["Very bad", 0, 2]  # Impossible 0%: Give or take 0%
]


def spelling_quality_summarised(quality: str) -> str:
    if (not quality) or (quality == NOT_APPLICABLE):
        return NOT_APPLICABLE

    if 'good' in quality.lower():
        return 'Good'

    return 'Bad'


def spelling_quality_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    tokenized_text = get_tokenized_text(text)
    misspelt_words = [
        each_word for _, each_word in enumerate(tokenized_text)
        if actual_spell_check(each_word) is not None
    ]
    result = 1 - (len(misspelt_words) / len(tokenized_text))

    return result if result >= 0.0 else 0.0


def get_tokenized_text(text: str) -> list:
    cached_function = memory.cache(word_tokenize)
    return cached_function(text.lower())


@memory.cache
def actual_spell_check(each_word: str) -> str:  # pragma: no cover
    # pragma: no cover => as multiprocess leads to loss of test coverage info
    spellchecked_word = Word(each_word).spellcheck()
    _, score = spellchecked_word[0]
    return each_word if score != 1 else None


def spelling_quality(score: float) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    score = float(score) * 100
    for _, each_slab in enumerate(spelling_quality_score_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]
