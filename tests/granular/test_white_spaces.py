import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.chars_spaces_and_whitespaces import (
    count_chars,
    count_whitespaces,
    count_characters_excluding_whitespaces,
    gather_repeated_whitespaces,
    count_repeated_whitespaces,
)  # noqa

text_with_a_number = "2833047 pe\nople li\tve i\rn this area"

text_to_return_value_mapping = [
    (np.nan, NaN, NaN, NaN),
    (float("nan"), NaN, NaN, NaN),
    (None, NaN, NaN, NaN),
    (text_with_a_number, 35, 8, 27),
]


@pytest.mark.parametrize(
    "text,expected_chars_count,expected_whitespaces_count,expected_chars_without_whitespaces_count",
    text_to_return_value_mapping,
)
def test_given_text_when_parsed_then_return_empty_or_valid_list_or_counts(
    text: str, expected_chars_count: int, expected_whitespaces_count: int, expected_chars_without_whitespaces_count: int
):
    # given, when
    actual_result = count_chars(text)

    # then
    assert expected_chars_count is actual_result, (
        "Didn't find the expected number of chars in the text"
        f"Expected: {expected_chars_count}, Actual: {actual_result}"
    )

    # given, when
    actual_result = count_whitespaces(text)

    # then
    assert expected_whitespaces_count is actual_result, (
        "Didn't find the expected number of spaces in the text"
        f"Expected: {expected_whitespaces_count}, Actual: {actual_result}"
    )

    # given, when
    actual_result = count_characters_excluding_whitespaces(text)

    # then
    assert expected_chars_without_whitespaces_count is actual_result, (
        "Didn't find the expected number of chars without spaces in the text"
        f"Expected: {expected_chars_without_whitespaces_count}, Actual: {actual_result}"
    )


text_with_repeated_whitespaces1 = "2833047   \t\tpeople live in th\ris area"
text_with_repeated_whitespaces2 = "2833047   people\r\r     live in th\tis area"
text_with_repeated_whitespaces3 = "2833047   people\n\n   live in   th\nis area"

text_to_repeated_counts_mapping = [
    (np.nan, NaN, NaN),
    (float("nan"), NaN, NaN),
    (None, NaN, NaN),
    (text_with_a_number, [], 0),
    (text_with_repeated_whitespaces1, [("   ", " "), ("\t\t", "\t")], 2),
    (text_with_repeated_whitespaces2, [("   ", " "), ("\r\r", "\r"), ("     ", " ")], 3),
    (text_with_repeated_whitespaces3, [("   ", " "), ("\n\n", "\n"), ("   ", " "), ("   ", " ")], 4),
]


@pytest.mark.parametrize(
    "text,expected_repeated_whitespaces,expected_repeated_whitespaces_count", text_to_repeated_counts_mapping
)
def test_given_text_when_parsed_then_return_empty_or_valid_list_or_repeated_counts(
    text: str, expected_repeated_whitespaces: list, expected_repeated_whitespaces_count: int
):
    # given, when
    actual_result = gather_repeated_whitespaces(text)

    # then
    assert (expected_repeated_whitespaces is actual_result) or (expected_repeated_whitespaces == actual_result), (
        "Didn't find the expected repeated spaces in the text.\n"
        f"Expected: {expected_repeated_whitespaces}, Actual: {actual_result}"
    )

    # given, when
    actual_count = count_repeated_whitespaces(text)

    # then
    assert (expected_repeated_whitespaces_count is actual_count) or (
        expected_repeated_whitespaces_count == actual_count
    ), (
        "Didn't find the expected number of repeated spaces in the text.\n"
        f"Expected: {expected_repeated_whitespaces_count}, Actual: {actual_count}"
    )
