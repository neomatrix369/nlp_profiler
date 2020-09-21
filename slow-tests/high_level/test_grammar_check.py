import numpy as np
import pytest

from nlp_profiler.constants import NaN, NOT_APPLICABLE
from nlp_profiler.core \
    import grammar_check_score, grammar_quality  # noqa

grammar_issues_text = 'Everyone here is so hardworking. Hardworking people. ' \
                      'I think hardworking people are a good trait in our company.'
no_grammar_issues = 'Python is a programming language.'

text_to_return_value_mapping = [
    (np.nan, NaN, NOT_APPLICABLE),
    (float('nan'), NaN, NOT_APPLICABLE),
    (None, NaN, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_score,expected_quality",
                         text_to_return_value_mapping)
def test_given_an_invalid_text_when_grammar_check_is_applied_then_no_info_is_returned(
        text: str, expected_score: float, expected_quality: str
):
    # given, when: text is not defined
    actual_score = grammar_check_score(text)

    # then
    assert actual_score is expected_score, \
        f"Grammar quality score should NOT " \
        f"have been returned, expected {expected_score}"

    # given, when
    actual_quality = grammar_quality(actual_score)

    # then
    assert actual_quality == expected_quality, \
        f"Grammar quality should NOT " \
        f"have been returned, expected {expected_quality}"


def test_given_a_correct_text_when_grammar_check_is_applied_then_no_grammar_issues_is_returned():
    # given, when
    actual_results = grammar_check_score(no_grammar_issues)

    # then
    assert actual_results == 0, \
        "Grammar check should have passed and returned a good score"

    # given
    expected_results = 'No issues'

    # when
    actual_results = grammar_quality(actual_results)

    # then
    assert expected_results == actual_results, \
        "Grammar check should have passed with no issues"


def test_given_a_text_when_grammar_check_is_applied_then_grammar_check_analysis_info_is_returned():
    # given, when
    actual_results = grammar_check_score(grammar_issues_text)

    # then
    assert actual_results == 3, \
        "Grammar check score didn't match for the text"

    # given
    expected_results = '3 issues'

    # when
    actual_results = grammar_quality(actual_results)

    # then
    assert expected_results == actual_results, \
        "Grammar check didn't match for the text"


grammar_check_score_to_words_mapping = [
    (NaN, NOT_APPLICABLE),
    (0, "No issues"),
    (1, "1 issue"),
    (2, "2 issues"),
]


@pytest.mark.parametrize("score,expected_result",
                         grammar_check_score_to_words_mapping)
def test_given_spelling_check_score_when_converted_to_words_then_return_right_word(
        score: float, expected_result: str
):
    # given, when
    actual_result = grammar_quality(score)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"