# https://www.journaldev.com/23788/python-string-module
import string as string_module

import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.punctuations import (
    gather_repeated_punctuations,
    count_repeated_punctuations,
    ADDITIONAL_SYMBOLS,
)  # noqa

REPEATED_SYMBOLS = ADDITIONAL_SYMBOLS[0] + ADDITIONAL_SYMBOLS[0]

text_with_repeated_punctuations1 = (
    "This sentence doesn't seem to too many repeated commas,, " "periods or semi-colons (;;).."
)
text_with_repeated_punctuations2 = "283047 some chars ((((area"
text_with_repeated_punctuations3 = "283047 some chars [[area]] ))))"
text_with_repeated_punctuations4 = "283047 some chars area;; ::::"
text_with_repeated_punctuations5 = "283047 some chars [area];;; ::::----"
text_with_repeated_punctuations6 = (
    f"283047 some chars [[]]. area{REPEATED_SYMBOLS}"
)
text_with_repeated_punctuations7 = '283047 some chars [] """ \\ area'
text_with_repeated_punctuations8 = "283047 some chars //// \\\\\\ area"
text_with_repeated_punctuations9 = string_module.punctuation + ADDITIONAL_SYMBOLS

text_to_return_value_mapping = [
    (np.nan, []),
    (float("nan"), []),
    (None, []),
    (text_with_repeated_punctuations1, [(",,", ","), (";;", ";"), ("..", ".")]),
    (text_with_repeated_punctuations2, [("((((", "(")]),
    (text_with_repeated_punctuations3, [("[[", "["), ("]]", "]"), ("))))", ")")]),
    (text_with_repeated_punctuations4, [(";;", ";"), ("::::", ":")]),
    (text_with_repeated_punctuations5, [(";;;", ";"), ("::::", ":"), ("----", "-")]),
    (text_with_repeated_punctuations6, [("[[", "["), ("]]", "]"), (REPEATED_SYMBOLS, ADDITIONAL_SYMBOLS[0])]),
    (text_with_repeated_punctuations7, [('"""', '"')]),
    (text_with_repeated_punctuations8, [("////", "/"), ("\\\\\\", "\\")]),
    (text_with_repeated_punctuations9, []),
]


@pytest.mark.parametrize("text,expected_result", text_to_return_value_mapping)
def test_given_a_text_when_parsed_then_return_empty_or_a_valid_list(text: str, expected_result: str):
    # given, when
    actual_result = gather_repeated_punctuations(text)

    # then
    assert expected_result == actual_result, "Didn't find the expected punctuations in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"


text_to_group_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_repeated_punctuations1, 3),
    (text_with_repeated_punctuations2, 1),
    (text_with_repeated_punctuations3, 3),
    (text_with_repeated_punctuations4, 2),
    (text_with_repeated_punctuations5, 3),
    (text_with_repeated_punctuations6, 3),
    (text_with_repeated_punctuations7, 1),
    (text_with_repeated_punctuations8, 2),
    (text_with_repeated_punctuations9, 0),
]


@pytest.mark.parametrize("text,expected_result", text_to_group_count_mapping)
def test_given_a_text_when_counted_then_return_NaN_or_count_of_punctuations(text: str, expected_result: float):
    # given, when
    actual_result = count_repeated_punctuations(text)

    # then
    assert expected_result is actual_result, "Didn't find the expected number of punctuations in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"
