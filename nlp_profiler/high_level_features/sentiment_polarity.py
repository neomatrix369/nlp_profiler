import math
from textblob import TextBlob

from nlp_profiler.constants import NOT_APPLICABLE, NaN


### Sentiment analysis

def sentiment_polarity_summarised(polarity: str) -> str:
    if (not polarity) or (polarity == NOT_APPLICABLE):
        return NOT_APPLICABLE

    if 'negative' in polarity.lower():
        return 'Negative'
    if 'positive' in polarity.lower():
        return 'Positive'

    return polarity


# Docs: https://textblob.readthedocs.io/en/dev/quickstart.html
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
sentiment_polarity_to_words_mapping = [
    ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    ["Quite positive", 87, 99],  # Almost Certain: 93%: Give or take 6%
    ["Pretty positive", 51, 87],  # Probable: 75%: Give or take about 12%
    ["Neutral", 49, 51],  # Chances About Even: 50%: Give or take about 10%
    ["Pretty negative", 12, 49],  # Probably Not: 30%: Give or take about 10%
    ["Quite negative", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
]


def sentiment_polarity(score: float) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    score = float(score)
    score = (score + 1) / 2  # see https://stats.stackexchange.com/questions/70801/how-to-normalize-data-to-0-1-range
    score *= 100
    for _, each_slab in enumerate(sentiment_polarity_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_polarity_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    return TextBlob(text).sentiment.polarity
