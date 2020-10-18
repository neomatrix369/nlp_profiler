import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.duplicates import gather_duplicates, count_duplicates  # noqa

text_with_a_number = '2833047 people live in this area'
text_with_duplicates = 'Everyone here is so hardworking. hardworking people. ' \
                       'I think hardworking people are a good trait in our company'

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
    actual_result = gather_duplicates(text)

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
    actual_result = count_duplicates(text)

    # then
    assert expected_result is actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_no_duplicates_when_parsed_then_return_empty():
    # given
    expected_results = {}

    # when
    actual_results = gather_duplicates(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Should have NOT found duplicates in the text"


def test_given_a_text_with_duplicates_when_parsed_then_return_the_duplicates():
    # given
    expected_results = {'.': 2, 'hardworking': 3, 'people': 2}

    # when
    actual_results = gather_duplicates(text_with_duplicates)

    # then
    assert expected_results == actual_results, \
        "Should have found multiple duplicates in the text"


def test_given_a_text_with_duplicates_when_counted_then_return_the_duplicates_count():
    # given,  when
    actual_results = count_duplicates(text_with_a_number)

    # then
    assert actual_results == 0, \
        "Should have NOT found duplicates in the text"

    # given,  when
    actual_results = count_duplicates(text_with_duplicates)

    # then
    assert actual_results == 3, \
        "Should have found a few duplicates in the text"
