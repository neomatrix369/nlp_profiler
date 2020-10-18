import math

import numpy as np
import pytest

from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.high_level_features.spelling_quality_check import spelling_quality_score, \
    spelling_quality, spelling_quality_summarised  # noqa

very_good_spelling_text = 'People live in this area. It is not a good area. People live in this area. It is not a good area. 2833047 people live in this area. It is not a good area.'
quite_good_spelling_text = 'People live in this area. It is not a good area. People live in this area. It is not a good area. 2833047 people live in this area. It is not a good arae.'
good_spelling_text = 'People live in this area. It is not a good area. People live in this area. It is not a good area. 2833047 people live in this arae. It is not a good arae.'
pretty_good_spelling_text = 'People live in this arae. It is not a good area. People live in this area. It is not a good area. 2833047 people live in this arae. It is not a good arae.'
bad_spelling_text = "2833047 people live in this arae. It is not a good arae. swa arae live in this arae."
pretty_bad_spelling_text = "I arae arae arae arae arae."

text_to_return_value_mapping = [
    (np.nan, NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (float('nan'), NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (None, NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE, NOT_APPLICABLE),
    (very_good_spelling_text, 1.0, 'Very good', 'Good'),
    (quite_good_spelling_text, 0.975, 'Quite good', 'Good'),
    (good_spelling_text, 0.95, 'Good', 'Good'),
    (pretty_good_spelling_text, 0.925, 'Pretty good', 'Good'),
    (bad_spelling_text, 0.7619047619047619, 'Bad', 'Bad'),
    (pretty_bad_spelling_text, 0.2857142857142857, 'Pretty bad', 'Bad')
]


@pytest.mark.parametrize("text,"
                         "expected_spelling_check_score,"
                         "expected_spelling_quality,"
                         "expected_spelling_check_summarised",
                         text_to_return_value_mapping)
def test_given_a_text_when_spell_check_is_applied_then_spell_check_analysis_info_is_returned(
        text: str,
        expected_spelling_check_score: float,
        expected_spelling_quality: str,
        expected_spelling_check_summarised: str
):
    # given, when
    actual_score = spelling_quality_score(text)
    # then
    if math.isnan(expected_spelling_check_score):
        assert actual_score is expected_spelling_check_score
    else:
        assert math.isclose(expected_spelling_check_score, actual_score,
                            rel_tol=1e-09, abs_tol=0.0), \
            "Spell check score didn't match for the text"

    # given, when
    actual_spelling_check = spelling_quality(actual_score)
    # then
    assert expected_spelling_quality == actual_spelling_check, \
        "Spelling quality check didn't match for the text"

    # given, when
    actual_summarised_spelling = spelling_quality_summarised(actual_spelling_check)
    # then
    assert expected_spelling_check_summarised == actual_summarised_spelling, \
        f"Summarised spelling quality check didn't match for the text '{text}'. " \
        f"Expected: {expected_spelling_check_summarised}, Actual: {actual_summarised_spelling}"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
spelling_check_score_to_words_mapping = [
    (0.99555, 0.99555, "Very good"),  # ["Very good", 99, 100],  # Certain: 100%: Give or take 0%
    (0.975, 0.975, "Quite good"),  # ["Quite good", 90, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.955, 0.955, "Good"),  # ["Good", 87, 90],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.925, 0.925, "Pretty good"),  # ["Bad", 63, 87],  # Pretty: Good: Probable: 75%: Give or take about 12%
    (0.65, 0.65, "Bad"),  # ["Pretty bad", 40, 63],  # So/so: Chances About Even: 50%: Give or take about 10%
    (0.50, 0.50, "Pretty bad"),  # ["Quite bad", 12, 40],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    (0.10, 0.10, "Quite bad"),  # ["Very bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
    (0.01, 0.01, "Very bad"),  # ["Very bad", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_spelling_quality_in_words",
                         spelling_check_score_to_words_mapping)
def test_given_spelling_check_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_spelling_quality_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_spelling_quality_in_words:", expected_spelling_quality_in_words)
    actual_result = spelling_quality(original_score)

    # then
    assert expected_spelling_quality_in_words == actual_result, \
        f"Expected: {expected_spelling_quality_in_words}, Actual: {actual_result}" \
        f"original_score: {original_score}, normalised_score: {normalised_score}"
