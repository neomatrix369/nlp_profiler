import math

import pytest

from nlp_profiler.core import NOT_APPLICABLE, spelling_quality_score, \
    spelling_quality, spelling_quality_summarised  # noqa

good_spelling_text = '2833047 people live in this area. It is not a good area. 2833047 people live in this area. It is not a good area. 2833047 people live in this area. It is not a good area.'
bad_spelling_text = "2833047 people live in this arae. It is tno a godo area. swa peeeple live in this area."
very_bad_spelling_text = "I'm asdaskld asdasd asdasd asdasd."


def test_given_an_invalid_text_when_spell_check_is_applied_then_no_spell_check_info_is_returned():
    # given, when: text is not defined
    actual_results = spelling_quality_score(None)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Spell quality check score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when: empty text
    actual_results = spelling_quality_score("")

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Spell quality check score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when
    actual_results = spelling_quality(NOT_APPLICABLE)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Spell quality check should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"


def test_given_a_text_when_spell_check_is_applied_then_spell_check_analysis_info_is_returned():
    verify_spelling_check(good_spelling_text, 0.9166666666666666, 'Quite good', 'Good')
    verify_spelling_check(bad_spelling_text, 0.7222222222222222, 'Bad', 'Bad')
    verify_spelling_check(very_bad_spelling_text, 0.16666666666666666, 'Quite bad', 'Bad')


def verify_spelling_check(text,
                          expected_spelling_check_score,
                          expected_spelling_check,
                          expected_summarised_spelling_check):
    # given, when
    actual_results = spelling_quality_score(text)
    # then
    assert math.isclose(expected_spelling_check_score, actual_results,
                        rel_tol=1e-09, abs_tol=0.0), \
        "Spell check score didn't match for the text"
    # given, when
    actual_results = spelling_quality(actual_results)
    # then
    assert expected_spelling_check == actual_results, \
        "Spelling quality check didn't match for the text"
    # given, when
    actual_results = spelling_quality_summarised(actual_results)
    # then
    assert expected_summarised_spelling_check == actual_results, \
        "Summarised spelling quality check didn't match for the text"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
spelling_check_score_mapping = [
    (0.99555, 0.99555, "Very good"),  # ["Very good", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite good"),  # ["Quite good", 90, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.88, 0.88, "Good"),  # ["Good", 87, 90],  # Quite Good: Almost Certain: 93%: Give or take 6%
    (0.70, 0.70, "Bad"),  # ["Bad", 63, 87],  # Pretty: Good: Probable: 75%: Give or take about 12%
    (0.50, 0.50, "Pretty bad"),  # ["Pretty bad", 40, 63],  # So/so: Chances About Even: 50%: Give or take about 10%
    (0.30, 0.30, "Quite bad"),  # ["Quite bad", 12, 40],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    (0.08, 0.08, "Very bad"),  # ["Very bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
    (0.01, 0.01, "Very bad"),  # ["Very bad", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_spelling_quality_in_words",
                         spelling_check_score_mapping)
def test_given_spelling_check_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_spelling_quality_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_spelling_quality_in_words:", expected_spelling_quality_in_words)
    actual_result = spelling_quality(original_score)

    # then
    assert expected_spelling_quality_in_words == actual_result
