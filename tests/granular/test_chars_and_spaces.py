import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.chars_spaces_and_whitespaces \
    import count_chars, count_spaces, count_characters_excluding_spaces, \
    gather_repeated_spaces, count_repeated_spaces  # noqa

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


text_with_repeated_spaces1 = '2833047   people live in this area'
text_with_repeated_spaces2 = '2833047   people     live in this area'
text_with_repeated_spaces3 = '2833047   people   live in   this area'

text_to_repeated_counts_mapping = [
    (np.nan, NaN, NaN),
    (float('nan'), NaN, NaN),
    (None, NaN, NaN),
    (text_with_a_number, [], 0),
    (text_with_repeated_spaces1, [('   ', ' ')], 1),
    (text_with_repeated_spaces2, [('   ', ' '), ('     ', ' ')], 2),
    (text_with_repeated_spaces3, [('   ', ' '), ('   ', ' '), ('   ', ' ')], 3)
]


@pytest.mark.parametrize("text,expected_repeated_spaces,expected_repeated_spaces_count",
                         text_to_repeated_counts_mapping)
def test_given_text_when_parsed_then_return_empty_or_valid_list_or_repeated_counts(
        text: str,
        expected_repeated_spaces: list,
        expected_repeated_spaces_count: int
):
    # given, when
    actual_result = gather_repeated_spaces(text)

    # then
    assert (expected_repeated_spaces is actual_result) or \
           (expected_repeated_spaces == actual_result), \
        "Didn't find the expected repeated spaces in the text.\n" \
        f"Expected: {expected_repeated_spaces}, Actual: {actual_result}"

    # given, when
    actual_count = count_repeated_spaces(text)

    # then
    assert (expected_repeated_spaces_count is actual_count) or \
           (expected_repeated_spaces_count == actual_count), \
        "Didn't find the expected number of repeated spaces in the text.\n" \
        f"Expected: {expected_repeated_spaces_count}, Actual: {actual_count}"
