import math

import numpy as np
import pytest

from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.high_level_features.sentiment_subjectivity import sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity  # noqa

objective_subjective_text = '2833047 and 1111 people live in this area.'
objective_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
subjective_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."

text_to_return_value_mapping = [
    (None, NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (np.nan, NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (float('nan'), NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (objective_subjective_text, 0.50, 'Objective/subjective', 'Objective/subjective'),
    (subjective_text, 0.75, 'Pretty subjective', 'Subjective'),
    (objective_text, 0.0, 'Very objective', 'Objective'),
]


@pytest.mark.parametrize("text,"
                         "expected_score,"
                         "expected_subjectivity,"
                         "expected_subjectivity_summarised",
                         text_to_return_value_mapping)
def test_given_a_text_when_sentiment_subjectivity_analysis_is_applied_then_subjective_analysis_info_is_returned(
        text: str,
        expected_score: float,
        expected_subjectivity: str,
        expected_subjectivity_summarised: str
):
    # given, when
    actual_score = sentiment_subjectivity_score(text)
    # then
    if math.isnan(expected_score):
        assert actual_score is expected_score
    else:
        assert math.isclose(expected_score, actual_score,
                            rel_tol=1e-09, abs_tol=0.0), \
            "Subjectivity/objectivity score didn't match for the text"
    # given, when
    actual_subjectivity = sentiment_subjectivity(actual_score)
    # then
    assert expected_subjectivity == actual_subjectivity, \
        "Sentiment subjectivity didn't match for the text"
    # given,  when
    actual_subjectivity_summarised = sentiment_subjectivity_summarised(actual_subjectivity)
    # then
    assert expected_subjectivity_summarised == actual_subjectivity_summarised, \
        "Summarised Sentiment subjectivity didn't match for the text"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
sentiment_subjectivity_score_to_words_mapping = [
    (1, 1.0, "Very subjective"),  # ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    (0.99555, 0.99555, "Very subjective"),  # ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite subjective"),  # ["Quite subjective", 87, 99],  # Almost Certain: 93%: Give or take 6%
    (0.65, 0.65, "Pretty subjective"),  # ["Pretty subjective", 63, 87],  # Probable: 75%: Give or take about 12%
    (0.50, 0.50, "Objective/subjective"),
    # ["Objective/subjective", 40, 63],  # Chances About Even: 50%: Give or take about 10%
    (0.35, 0.35, "Pretty objective"),  # ["Pretty objective", 12, 40],  # Probably Not: 30%: Give or take about 10%
    (0.08, 0.08, "Quite objective"),  # ["Quite objective", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    (0.01, 0.01, "Very objective"),  # ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
    (0.0, 0.00, "Very objective"),  # ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_subjectivity_in_words",
                         sentiment_subjectivity_score_to_words_mapping)
def test_given_sentiment_subjectivity_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_subjectivity_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_subjectivity_in_words:", expected_subjectivity_in_words)
    actual_result = sentiment_subjectivity(original_score)

    # then
    assert expected_subjectivity_in_words == actual_result
