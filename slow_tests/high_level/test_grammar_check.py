import pytest
import numpy as np
from nlp_profiler.core \
    import NOT_APPLICABLE, grammar_check_score, grammar_quality  # noqa

grammar_issues_text = 'Everyone here is so hardworking. Hardworking people. ' \
                      'I think hardworking people are a good trait in our company.'
no_grammar_issues = 'Python is a programming language.'

text_to_return_value_mapping = [
    (np.nan, NOT_APPLICABLE),
    (float('nan'), NOT_APPLICABLE),
    (None, NOT_APPLICABLE),
    ("", NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_an_invalid_text_when_grammar_check_is_applied_then_no_info_is_returned(
        text: str, expected_result: str
):
    # given, when: text is not defined
    actual_results = grammar_check_score(text)

    # then
    assert actual_results == expected_result, \
        f"Grammar quality score should NOT " \
        f"have been returned, expected {expected_result}"

    # given, when
    actual_results = grammar_quality(expected_result)

    # then
    assert actual_results == expected_result, \
        f"Grammar quality should NOT " \
        f"have been returned, expected {expected_result}"


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
