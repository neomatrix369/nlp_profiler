import numpy as np
import pytest

from nlp_profiler.granular_features.numbers import \
    NaN, gather_whole_numbers, count_whole_numbers  # noqa

text_with_a_number = '2833047 people live in this area'

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
    actual_result = gather_whole_numbers(text)

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
    actual_result = count_whole_numbers(text)

    # then
    assert expected_result is actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_numbers_when_parsed_then_return_only_the_numbers():
    # given
    expected_results = ['2833047']

    # when
    actual_results = gather_whole_numbers(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the number '2833047' in the text"


def test_given_a_text_with_a_number_when_counted_then_return_count_of_numbers_found():
    # given, when
    actual_results = count_whole_numbers(text_with_a_number)

    # then
    assert actual_results == 1, \
        "Didn't find the expected single number in the text"
