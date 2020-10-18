import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.sentences import gather_sentences, count_sentences  # noqa

text_with_emojis = "I love ⚽ very much 😁"
text_with_emojis_ends_with_period = "I love ⚽ very much 😁."
text_with_a_number = '2833047 people live in this area.'
text_with_two_sentences = text_with_a_number + " " + text_with_emojis

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
    actual_result = gather_sentences(text)

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
    actual_result = count_sentences(text)

    # then
    assert expected_result is actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


@pytest.mark.parametrize("text,expected_result",
                         [
                             (text_with_emojis, 1),
                             (text_with_emojis_ends_with_period, 1),
                             (text_with_a_number, 1),
                             (text_with_two_sentences, 2),
                             ('....', 1),
                             (';;;;;;', 1),
                             ('', 0),
                             (' ', 0),
                             ('a', 1),
                             ('⚽😁', 1),
                         ])
def test_given_a_text_with_sentences_when_counted_then_return_the_count_of_sentences(
        text, expected_result
):
    # given, when
    actual_result = count_sentences(text)

    # then
    assert actual_result == expected_result, \
        "Didn't find the expected number of sentence in the text. " \
        f"Expected: {expected_result}, Actual: {actual_result}"


@pytest.mark.parametrize("text,expected_result",
                         [
                             (text_with_a_number, [text_with_a_number]),
                             (text_with_two_sentences, [text_with_a_number, text_with_emojis]),
                         ])
def test_given_a_text_with_sentences_when_parsed_then_return_the_sentences(
        text: str, expected_result: list
):
    # given, when
    actual_result = gather_sentences(text)

    # then
    assert expected_result == actual_result, \
        "Didn't find the expected sentence(s) in the text." \
        f"Expected: {expected_result}, Actual: {actual_result}"
