import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.non_alphanumeric \
    import gather_non_alpha_numeric, count_non_alpha_numeric  # noqa

text_with_a_number = '2833047 people live in this area'
text_with_emojis = "I love ⚽ very much 😁"
text_with_alphanumeric_chars = '2833047 people live in this area'

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_invalid_text_when_parsed_then_return_empty_list(
        text: str, expected_result: str
):
    # given, when
    actual_result = gather_non_alpha_numeric(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


text_to_return_count_mapping = [
    (np.nan, NaN),
    (float('nan'), NaN),
    (None, NaN),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_count_mapping)
def test_given_invalid_text_when_counted_then_return_NaN(
        text: str, expected_result: float
):
    # given, when
    actual_result = count_non_alpha_numeric(text)

    # then
    assert expected_result is actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_non_alphanumeric_chars_when_parsed_then_return_non_alphanumeric_chars():
    # given: a number in a text
    expected_results = [' ', ' ', ' ', ' ', ' ']

    # when
    actual_results = gather_non_alpha_numeric(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected non-alphanumeric chars in the text with a number"

    # given: emojis in text
    expected_results = [' ', ' ', '⚽', ' ', ' ', ' ', '😁']

    # when
    actual_results = gather_non_alpha_numeric(text_with_emojis)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected non-alphanumeric chars in the text with emoji"


def test_given_a_alphanumeric_text_when_counted_then_return_number_of_alphanumeric_chars():
    # given, when
    actual_results = count_non_alpha_numeric(text_with_a_number)

    # then
    assert actual_results == 5, \
        "Didn't find the expected number of non-alphanumeric " \
        "chars in the text with a number"

    # given, when
    actual_results = count_non_alpha_numeric(text_with_emojis)

    # then
    assert actual_results == 7, \
        "Didn't find the expected number of non-alphanumeric " \
        "chars in the text with emojis"
