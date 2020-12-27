import numpy as np
import pytest

from nlp_profiler.granular_features.numbers import \
    NaN, gather_whole_numbers, count_whole_numbers  # noqa

text_with_a_number = '2833047 people live in this area'

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
    (text_with_a_number, ['2833047']),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_text_when_counted_for_whole_numbers_then_return_an_empty_or_valid_list(
        text: str, expected_result: str
):
    # given, when
    actual_result = gather_whole_numbers(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected number(s) in the text" \
        f"Expected: {expected_result}, Actual: {actual_result}"


text_to_return_count_mapping = [
    (np.nan, NaN),
    (float('nan'), NaN),
    (None, NaN),
    (text_with_a_number, 1),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_count_mapping)
def test_given_text_when_counted_for_whole_numbers_then_return_NaN_or_a_count(
        text: str, expected_result: float
):
    # given, when
    actual_result = count_whole_numbers(text)

    # then
    assert expected_result is actual_result, \
        "Didn't find the expected number(s) in the text" \
        f"Expected: {expected_result}, Actual: {actual_result}"
