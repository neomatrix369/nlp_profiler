import math

from nlp_profiler.core import spelling_quality_score, \
    spelling_quality, spelling_quality_summarised  # noqa

some_text = '2833047 people live in this area. It is not a good area.'


def test_given_a_text_when_spell_check_is_applied_then_spell_check_analysis_info_is_returned():
    # given
    expected_results = 0.9688017898574743

    # when
    actual_results = spelling_quality_score(some_text)

    # then
    assert math.isclose(expected_results, actual_results,
                        rel_tol=1e-09, abs_tol=0.0), \
        "Spell check score didn't match for the text"

    # given
    expected_results = 'Quite good'

    # when
    actual_results = spelling_quality(actual_results)

    # then
    assert expected_results == actual_results, \
        "Spelling quality check didn't match for the text"

    # given
    expected_results = 'Good'

    # when
    actual_results = spelling_quality_summarised(actual_results)

    # then
    assert expected_results == actual_results, \
        "Summarised spelling quality check didn't match for the text"
