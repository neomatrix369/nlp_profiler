from textblob import TextBlob

from nlp_profiler.constants import NOT_APPLICABLE, NaN
import math


### Sentiment Subjectivity

def sentiment_subjectivity_summarised(subjectivity: str) -> str:
    if (not subjectivity) or (subjectivity == NOT_APPLICABLE):
        return NOT_APPLICABLE

    if '/' in subjectivity:
        return subjectivity
    elif 'subjective' in subjectivity.lower():
        return 'Subjective'

    return 'Objective'


### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
sentiment_subjectivity_to_words_mapping = [
    ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    ["Quite subjective", 87, 99],  # Almost Certain: 93%: Give or take 6%
    ["Pretty subjective", 63, 87],  # Probable: 75%: Give or take about 12%
    ["Objective/subjective", 40, 63],  # Chances About Even: 50%: Give or take about 10%
    ["Pretty objective", 12, 40],  # Probably Not: 30%: Give or take about 10%
    ["Quite objective", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
]


def sentiment_subjectivity(score: float) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    score = float(score) * 100

    for _, each_slab in enumerate(sentiment_subjectivity_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_subjectivity_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    return TextBlob(text).sentiment.subjectivity
