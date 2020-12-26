import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.numbers \
    import gather_repeated_digits, count_repeated_digits  # noqa

text_with_repeated_digits1 = '283047 people live in this 999999 area'
text_with_repeated_digits2 = '283047 people live in this 00000area'
text_with_repeated_digits3 = '283047 people live in this area 11111'
text_with_repeated_digits4 = '283047 people live in this area3333 2222'
text_with_repeated_digits5 = '283047 people live in this area3333 22224444'
text_with_repeated_digits6 = '283047 people live in this 6 area'
text_with_repeated_digits7 = '283047 people live in this 55 area'
text_with_repeated_digits8 = '283047 people live in this 888 area'

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
    (text_with_repeated_digits1, [('999999', '9')]),
    (text_with_repeated_digits2, [('00000', '0')]),
    (text_with_repeated_digits3, [('11111', '1')]),
    (text_with_repeated_digits4, [('3333', '3'), ('2222', '2')]),
    (text_with_repeated_digits5, [('3333', '3'), ('2222', '2'), ('4444', '4')]),
    (text_with_repeated_digits6, []),
    (text_with_repeated_digits7, [('55', '5')]),
    (text_with_repeated_digits8, [('888', '8')]),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_a_text_when_parsed_then_return_empty_or_a_valid_list(
        text: str, expected_result: str
):
    # given, when
    actual_result = gather_repeated_digits(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected digits in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"


text_to_group_count_mapping = [
    (np.nan, NaN),
    (float('nan'), NaN),
    (None, NaN),
    (text_with_repeated_digits1, 1),
    (text_with_repeated_digits2, 1),
    (text_with_repeated_digits3, 1),
    (text_with_repeated_digits4, 2),
    (text_with_repeated_digits5, 3),
    (text_with_repeated_digits6, 0),
    (text_with_repeated_digits7, 1),
    (text_with_repeated_digits8, 1)
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_group_count_mapping)
def test_given_a_text_when_counted_then_return_NaN_or_count_of_digits(
        text: str, expected_result: float
):
    # given, when
    actual_result = count_repeated_digits(text)

    # then
    assert expected_result is actual_result, \
        "Didn't find the expected number of digits in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"
