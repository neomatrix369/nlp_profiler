import math

import numpy as np
import pytest

from nlp_profiler.core import NOT_APPLICABLE, sentiment_polarity_score, \
    sentiment_polarity_summarised, sentiment_polarity  # noqa

positive_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
negative_text = "2833047 people live in this area. It is not a good area."
neutral_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."

text_to_return_value_mapping = [
    (np.nan, NOT_APPLICABLE),
    (float('nan'), NOT_APPLICABLE),
    (None, NOT_APPLICABLE),
    ("", NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_an_invalid_text_when_sentiment_analysis_is_applied_then_no_sentiment_analysis_info_is_returned(
        text: str, expected_result: str
):
    # given, when: text is not defined
    actual_results = sentiment_polarity_score(text)

    # then
    assert actual_results == expected_result, \
        f"Sentiment polarity score should NOT " \
        f"have been returned, expected {expected_result}"

    # given, when
    actual_results = sentiment_polarity(expected_result)

    # then
    assert actual_results == expected_result, \
        f"Sentiment polarity should NOT " \
        f"have been returned, expected {expected_result}"


def test_given_a_text_when_sentiment_analysis_is_applied_then_sentiment_analysis_info_is_returned():
    assert_text_polarity(positive_text, 0.375000, 'Pretty positive', 'Positive')
    assert_text_polarity(negative_text, -0.10681818181818181, 'Pretty negative', 'Negative')
    assert_text_polarity(neutral_text, 0.0, 'Neutral', 'Neutral')
    assert_text_polarity(None, NOT_APPLICABLE, NOT_APPLICABLE, NOT_APPLICABLE)


def assert_text_polarity(text,
                         expected_polarity_score,
                         expected_polarity,
                         expected_polarity_summarised):
    # given, when
    actual_results = sentiment_polarity_score(text)
    # then
    if expected_polarity_score == NOT_APPLICABLE:
        assert actual_results == expected_polarity_score
    else:
        assert math.isclose(expected_polarity_score, actual_results,
                            rel_tol=1e-09, abs_tol=0.0), \
            "Sentiment polarity score didn't match for the text"

    # given, when
    actual_results = sentiment_polarity(actual_results)
    # then
    assert expected_polarity == actual_results, \
        "Sentiment polarity didn't match for the text"

    # given, when
    actual_results = sentiment_polarity_summarised(actual_results)
    # then
    assert expected_polarity_summarised == actual_results, \
        "Summarised Sentiment polarity didn't match for the text"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
sentiment_polarity_score_to_words_mapping = [
    (1, 0.99555, "Very positive"),  # ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    (0.99, 0.99555, "Very positive"),  # ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite positive"),  # ["Quite positive", 87, 99],  # Almost Certain: 93%: Give or take 6%
    (0.60, 0.60, "Pretty positive"),  # ["Pretty positive", 51, 87],  # Probable: 75%: Give or take about 12%
    (0.0, 0.50, "Neutral"),  # ["Neutral", 49, 51],  # Chances About Even: 50%: Give or take about 10%
    (-0.60, 0.30, "Pretty negative"),  # ["Pretty negative", 12, 49],  # Probably Not: 30%: Give or take about 10%
    (-0.95, 0.08, "Quite negative"),  # ["Quite negative", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    (-0.99, 0.01, "Very negative"),  # ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
    (-1, 0.01, "Very negative"),  # ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_sentiment_in_words",
                         sentiment_polarity_score_to_words_mapping)
def test_given_sentiment_polarity_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_sentiment_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_sentiment_in_words:", expected_sentiment_in_words)
    actual_result = sentiment_polarity(original_score)

    # then
    assert expected_sentiment_in_words == actual_result
