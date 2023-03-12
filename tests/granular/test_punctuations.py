import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.punctuations import (
    gather_punctuations,
    count_punctuations,
    ADDITIONAL_SYMBOLS,
)  # noqa

text_with_punctuations = (
    "This sentence doesn't seem to too many commas, periods or semi-colons (;)." + ADDITIONAL_SYMBOLS
)

text_to_return_value_mapping = [
    (np.nan, []),
    (float("nan"), []),
    (None, []),
    (text_with_punctuations, ["'", ",", "-", "(", ";", ")", "."] + list(ADDITIONAL_SYMBOLS)),
]


@pytest.mark.parametrize("text,expected_result", text_to_return_value_mapping)
def test_given_a_text_when_parsed_then_return_an_empty_list_or_list_of_punctuations(text: str, expected_result: str):
    # given, when
    actual_result = gather_punctuations(text)

    # then
    assert expected_result == actual_result, (
        "Didn't find the expected punctuations in the text" f"Expected: {expected_result}, Actual: {actual_result}"
    )


text_to_return_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_punctuations, 11),
]


@pytest.mark.parametrize("text,expected_result", text_to_return_count_mapping)
def test_given_a_text_when_counted_then_return_NaN_or_count_of_punctuations(text: str, expected_result: float):
    # given, when
    actual_result = count_punctuations(text)

    # then
    assert expected_result is actual_result, (
        "Didn't find the expected number of punctuation marks in the text"
        f"Expected: {expected_result}, Actual: {actual_result}"
    )
