from nlp_profiler.core import grammar_check_score, grammar_quality  # noqa

grammar_issues_text = 'Everyone here is so hardworking. Hardworking people. ' \
                      'I think hardworking people are a good trait in our company.'
no_grammar_issues = 'Python is a programming language.'


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
