import math

from nlp_profiler.core import NOT_APPLICABLE, sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity  # noqa

objective_subjective_text = '2833047 and 1111 people live in this area.'
objective_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
subjective_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."


def test_given_an_invalid_text_when_subjectivity_analysis_is_applied_then_no_subjectivity_analysis_info_is_returned():
    # given, when: text is not defined
    actual_results = sentiment_subjectivity_score(None)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Subjectivity/objectivity score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when: empty text
    actual_results = sentiment_subjectivity_score("")

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Subjectivity/objectivity score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when
    actual_results = sentiment_subjectivity(NOT_APPLICABLE)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Subjectivity/objectivity should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"


def test_given_a_text_when_subjectivity_analysis_is_applied_then_subjective_analysis_info_is_returned():
    assert_sentiment_subjectivity(objective_subjective_text, 0.50, 'Objective/subjective', 'Objective/subjective')
    assert_sentiment_subjectivity(subjective_text, 0.75, 'Pretty subjective', 'Subjective')
    assert_sentiment_subjectivity(objective_text, 0.0, 'Very objective', 'Objective')


def assert_sentiment_subjectivity(text, expected_sentiment_subjectivity_score, 
                                  expected_sentiment_subjectivity,
                                  expected_summarised_sentiment_subjectivity):
    # given, when
    actual_results = sentiment_subjectivity_score(text)
    # then
    assert math.isclose(expected_sentiment_subjectivity_score, actual_results,
                        rel_tol=1e-09, abs_tol=0.0), \
        "Subjectivity/objectivity score didn't match for the text"
    # given, when
    actual_results = sentiment_subjectivity(actual_results)
    # then
    assert expected_sentiment_subjectivity == actual_results, \
        "Subjectivity/objectivity polarity didn't match for the text"
    # given,  when
    actual_results = sentiment_subjectivity_summarised(actual_results)
    # then
    assert expected_summarised_sentiment_subjectivity == actual_results, \
        "Summarised Subjectivity/Objectivity polarity didn't match for the text"
