import numpy as np
import pytest

from nlp_profiler.granular_features.numbers import \
    NaN, gather_whole_numbers, count_whole_numbers, gather_digits, count_digits  # noqa

text_with_a_number = '2833047 people live in this area'

text_to_whole_numbers_mapping = [
    (np.nan, [], NaN),
    (float('nan'), [], NaN),
    (None, [], NaN),
    (text_with_a_number, ['2833047'], 1),
]


@pytest.mark.parametrize("text,expected_result,expected_count",
                         text_to_whole_numbers_mapping)
def test_given_text_when_counted_for_whole_numbers_then_return_the_respective_values(
        text: str, expected_result: str, expected_count: int
):
    # given, when
    actual_result = gather_whole_numbers(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected number(s) in the text" \
        f"Expected: {expected_result}, Actual: {actual_result}"

    # given, when
    actual_result = count_whole_numbers(text)

    # then
    assert expected_count is actual_result, \
        "Didn't find the expected number of whole numbers in the text" \
        f"Expected: {expected_count}, Actual: {actual_result}"


text_to_digits_result_mapping = [
    (np.nan, [], NaN),
    (float('nan'), [], NaN),
    (None, [], NaN),
    (text_with_a_number, ['2', '8', '3', '3', '0', '4', '7'], 7),
    ('0123456789', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10),
]


@pytest.mark.parametrize("text,expected_result,expected_count",
                         text_to_digits_result_mapping)
def test_given_text_when_counted_for_digits_then_return_the_respective_values(
        text: str, expected_result: float, expected_count: int
):
    # given, when
    actual_result = gather_digits(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected digit(s) in the text" \
        f"Expected: {expected_result}, Actual: {actual_result}"

    # given, when
    actual_result = count_digits(text)

    # then
    assert expected_count is actual_result, \
        "Didn't find the expected number of digits in the text" \
        f"Expected: {expected_count}, Actual: {actual_result}"
