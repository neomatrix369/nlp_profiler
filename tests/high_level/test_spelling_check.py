import math

import numpy as np
import pytest

from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.spelling_quality_check import spelling_quality_score, \
    spelling_quality, spelling_quality_summarised  # noqa

good_spelling_text = 'People live in this area. It is not a good area. People live in this area. It is not a good area. 2833047 people live in this area. It is not a good area.'
bad_spelling_text = "2833047 people live in this arae. It is not a good area. swa peeeple live in this area."
very_bad_spelling_text = "I am asdasd asdasd good asdasd."

text_to_return_value_mapping = [
    (np.nan, NaN, NOT_APPLICABLE),
    (float('nan'), NaN, NOT_APPLICABLE),
    (None, NaN, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_score,expected_quality",
                         text_to_return_value_mapping)
def test_given_an_invalid_text_when_spelling_check_is_applied_then_no_analysis_info_is_returned(
        text: str, expected_score: float, expected_quality: str
):
    # given, when: text is not defined
    actual_score = spelling_quality_score(text)

    # then
    assert actual_score is expected_score, \
        f"Spelling quality score should NOT " \
        f"have been returned, expected {expected_score}"

    # given, when
    actual_quality = spelling_quality(expected_score)

    # then
    assert actual_quality == expected_quality, \
        f"Spelling quality should NOT " \
        f"have been returned, expected {expected_quality}"


def test_given_a_text_when_spell_check_is_applied_then_spell_check_analysis_info_is_returned():
    verify_spelling_check(good_spelling_text, 1.0, 'Very good', 'Good')
    verify_spelling_check(bad_spelling_text, 0.6190476190476191, 'Bad', 'Bad')
    verify_spelling_check(very_bad_spelling_text, 0.14285714285714285, 'Pretty bad', 'Bad')
    verify_spelling_check(None, NaN, NOT_APPLICABLE, NOT_APPLICABLE)


def verify_spelling_check(text,
                          expected_spelling_check_score,
                          expected_spelling_check,
                          expected_summarised_spelling_check):
    # given, when
    actual_score = spelling_quality_score(text)
    # then
    if expected_spelling_check_score is NaN:
        assert actual_score is expected_spelling_check_score
    else:
        assert math.isclose(expected_spelling_check_score, actual_score,
                            rel_tol=1e-09, abs_tol=0.0), \
            "Spell check score didn't match for the text"

    # given, when
    actual_score = spelling_quality(actual_score)
    # then
    assert expected_spelling_check == actual_score, \
        "Spelling quality check didn't match for the text"

    # given, when
    actual_score = spelling_quality_summarised(actual_score)
    # then
    assert expected_summarised_spelling_check == actual_score, \
        f"Summarised spelling quality check didn't match for the text '{text}'. " \
        f"Expected: {expected_summarised_spelling_check}, Actual: {actual_result}"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
spelling_check_score_to_words_mapping = [
    (0.99555, 0.99555, "Very good"),  # ["Very good", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite good"),  # ["Quite good", 90, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.88, 0.88, "Good"),  # ["Good", 87, 90],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.70, 0.70, "Pretty good"),  # ["Bad", 63, 87],  # Pretty: Good: Probable: 75%: Give or take about 12%
    (0.50, 0.50, "Bad"),  # ["Pretty bad", 40, 63],  # So/so: Chances About Even: 50%: Give or take about 10%
    (0.30, 0.30, "Pretty bad"),  # ["Quite bad", 12, 40],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    (0.08, 0.08, "Quite bad"),  # ["Very bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
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
