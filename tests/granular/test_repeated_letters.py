import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.letters \
    import gather_repeated_letters, count_repeated_letters  # noqa

text_with_repeated_letters1 = '2833047 people live in this aaaaa area'
text_with_repeated_letters2 = '2833047 people live in this aaaaaarea'
text_with_repeated_letters3 = '2833047 people live in this area BBBBBBB'
text_with_repeated_letters4 = '2833047 people live in this areaBBBBBBB CCCC'
text_with_repeated_letters5 = '2833047 people live in this areaBBBBBBB CCCCdddd'
text_with_repeated_letters6 = '2833047 people live in this aa area'
text_with_repeated_letters7 = '2833047 people live in this ccc area'

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
    (text_with_repeated_letters1, [('aaaaa', 'a')]),
    (text_with_repeated_letters2, [('aaaaaa', 'a')]),
    (text_with_repeated_letters3, [('BBBBBBB', 'B')]),
    (text_with_repeated_letters4, [('BBBBBBB', 'B'), ('CCCC', 'C')]),
    (text_with_repeated_letters5, [('BBBBBBB', 'B'), ('CCCC', 'C'), ('dddd', 'd')]),
    (text_with_repeated_letters6, []),
    (text_with_repeated_letters7, [('ccc', 'c')]),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_a_text_when_parsed_then_return_empty_or_a_valid_list(
        text: str, expected_result: str
):
    # given, when
    actual_result = gather_repeated_letters(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected letters in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"


text_to_group_count_mapping = [
    (np.nan, NaN),
    (float('nan'), NaN),
    (None, NaN),
    (text_with_repeated_letters1, 1),
    (text_with_repeated_letters2, 1),
    (text_with_repeated_letters3, 1),
    (text_with_repeated_letters4, 2),
    (text_with_repeated_letters5, 3),
    (text_with_repeated_letters6, 0),
    (text_with_repeated_letters7, 1),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_group_count_mapping)
def test_given_a_text_when_counted_then_return_NaN_or_count_of_letters(
        text: str, expected_result: float
):
    # given, when
    actual_result = count_repeated_letters(text)

    # then
    assert expected_result is actual_result, \
        "Didn't find the expected number of letters in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"
