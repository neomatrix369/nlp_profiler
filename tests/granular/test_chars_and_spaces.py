import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.chars_and_spaces \
    import count_chars, count_spaces, count_characters_excluding_spaces  # noqa

text_with_a_number = '2833047 people live in this area'

text_to_return_value_mapping = [
    (np.nan, NaN, NaN, NaN),
    (float('nan'), NaN, NaN, NaN),
    (None, NaN, NaN, NaN),
    (text_with_a_number, 32, 5, 27)
]


@pytest.mark.parametrize("text,expected_chars_count,expected_spaces_count,expected_chars_without_spaces_count",
                         text_to_return_value_mapping)
def test_given_text_when_parsed_then_return_empty_or_valid_list_or_counts(
        text: str,
        expected_chars_count: int,
        expected_spaces_count: int,
        expected_chars_without_spaces_count: int
):
    # given, when
    actual_result = count_chars(text)

    # then
    assert expected_chars_count is actual_result, \
        "Didn't find the expected number of chars in the text" \
        f"Expected: {expected_chars_count}, Actual: {actual_result}"

    # given, when
    actual_result = count_spaces(text)

    # then
    assert expected_spaces_count is actual_result, \
        "Didn't find the expected number of spaces in the text" \
        f"Expected: {expected_spaces_count}, Actual: {actual_result}"

    # given, when
    actual_result = count_characters_excluding_spaces(text)

    # then
    assert expected_chars_without_spaces_count is actual_result, \
        "Didn't find the expected number of chars without spaces in the text" \
        f"Expected: {expected_chars_without_spaces_count}, Actual: {actual_result}"
