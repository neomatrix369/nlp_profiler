from nlp_profiler.core import gather_alpha_numeric, count_alpha_numeric  # noqa
import numpy as np
import pytest

text_with_alphanumeric_chars = '2833047 people live in this area'


text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
]
@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_invalid_text_when_parsed_then_return_empty_list(
        text: str, expected_result: list
):
    # given, when
    actual_result = gather_alpha_numeric(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result} "


def test_given_a_alphanumeric_text_when_parsed_then_return_alphanumeric_chars():
    # given
    expected_results = list(text_with_alphanumeric_chars.replace(' ', ''))

    # when
    actual_results = gather_alpha_numeric(text_with_alphanumeric_chars)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected alpha numeric chars in the text"


def test_given_a_alphanumeric_text_when_counted_then_return_number_of_alphanumeric_chars():
    # given
    expected_results = len(list(text_with_alphanumeric_chars.replace(' ', '')))

    # when
    actual_results = count_alpha_numeric(text_with_alphanumeric_chars)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected number of alpha numeric chars in the text"
