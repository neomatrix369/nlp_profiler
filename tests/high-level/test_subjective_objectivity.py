import math

from nlp_profiler.core import sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity  # noqa

some_text = '2833047 and 1111 people live in this area.'


def test_given_a_text_when_subjectivity_analysis_is_applied_then_subjective_analysis_info_is_returned():
    # given
    expected_results = 0.50

    # when
    actual_results = sentiment_subjectivity_score(some_text)

    # then
    assert math.isclose(expected_results, actual_results,
                        rel_tol=1e-09, abs_tol=0.0), \
        "Subjectivity/objectivity score didn't match for the text"

    # given
    expected_results = 'Objective/subjective'

    # when
    actual_results = sentiment_subjectivity(actual_results)

    # then
    assert expected_results == actual_results, \
        "Subjectivity/objectivity polarity didn't match for the text"

    # given
    expected_results = 'Objective/subjective'

    # when
    actual_results = sentiment_subjectivity_summarised(actual_results)

    # then
    assert expected_results == actual_results, \
        "Summarised Subjectivity/Objectivity polarity didn't match for the text"
