from nlp_profiler.core \
    import NOT_APPLICABLE, gather_sentences, count_sentences  # noqa
import numpy as np
import pytest

text_with_emojis = "I love ⚽ very much 😁"
text_with_a_number = '2833047 people live in this area'
text_with_two_sentences = text_with_a_number + "." + text_with_emojis

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_invalid_text_when_parsed_then_return_empty_list(
        text: str, expected_result: list
):
    # given, when
    actual_result = gather_sentences(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


text_to_return_count_mapping = [
    (np.nan, NOT_APPLICABLE),
    (float('nan'), NOT_APPLICABLE),
    (None, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_count_mapping)
def test_given_invalid_text_when_counted_then_return_NOT_APPLICABLE(
        text: str, expected_result: list
):
    # given, when
    actual_result = count_sentences(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_sentences_when_parsed_then_return_the_sentences():
    # given
    expected_results = [text_with_a_number]

    # when
    actual_results = gather_sentences(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected sentence in the text"

    # given
    expected_results = [text_with_a_number, text_with_emojis]

    # when
    actual_results = gather_sentences(text_with_two_sentences)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected two sentences in the text"


def test_given_a_text_with_sentences_when_counted_then_return_the_count_of_sentences():
    # given, when
    actual_results = count_sentences(text_with_a_number)

    # then
    assert actual_results == 1, \
        "Didn't find the single expected sentence in the text"

    # given, when
    actual_results = count_sentences(text_with_two_sentences)

    # then
    assert actual_results == 2, \
        "Didn't find the two sentences in the text"
