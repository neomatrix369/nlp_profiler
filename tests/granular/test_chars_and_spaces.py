from nlp_profiler.constants import NOT_APPLICABLE
from nlp_profiler.core \
    import count_chars, count_spaces, count_characters_excluding_spaces  # noqa
import numpy as np
import pytest

text_with_a_number = '2833047 people live in this area'

text_to_return_value_mapping = [
    (np.nan, NOT_APPLICABLE),
    (float('nan'), NOT_APPLICABLE),
    (None, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_invalid_text_when_parsed_then_return_empty_list(
        text: str, expected_result: list
):
    # given, when
    actual_result = count_chars(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"

    # given, when
    actual_result = count_spaces(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"

    # given, when
    actual_result = count_characters_excluding_spaces(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_when_counted_for_length_then_return_that_count():
    # given, when
    actual_results = count_chars(text_with_a_number)

    # then
    assert actual_results == 32, \
        "Didn't find the expected number of chars in the text"


def test_given_a_text_with_spaces_when_counted_for_spaces_then_return_that_count():
    # given, when
    actual_results = count_spaces(text_with_a_number)

    # then
    assert actual_results == 5, \
        "Didn't find the expected number of spaces in the text"


def test_given_a_text_with_spaces_when_counted_for_chars_then_return_that_count():
    # given, when
    actual_results = count_characters_excluding_spaces(text_with_a_number)

    # then
    assert actual_results == 27, \
        "Didn't find the expected number of chars without spaces in the text"
