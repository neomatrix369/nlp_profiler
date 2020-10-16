import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.emojis \
    import gather_emojis, count_emojis  # noqa

text_with_emojis = "I love ⚽ very much 😁"

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
    actual_result = gather_emojis(text)

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
    actual_result = count_emojis(text)

    # then
    assert expected_result is actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_emoji_when_parsed_then_return_only_emojis():
    # given
    expected_results = ['soccer_ball', 'beaming_face_with_smiling_eyes']

    # when
    actual_results = gather_emojis(text_with_emojis)

    # then
    assert expected_results == actual_results, \
        "Didn't find the two emojis ⚽ and 😁 in the text"


def test_given_a_text_with_emoji_when_counted_then_return_number_of_emojis_found():
    # given, when
    actual_results = count_emojis(text_with_emojis)

    # then
    assert actual_results == 2, \
        "Didn't find the expected two emojis in the text"
