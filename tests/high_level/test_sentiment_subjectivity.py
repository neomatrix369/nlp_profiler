import math

import pytest

from nlp_profiler.core import NOT_APPLICABLE, sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity  # noqa

objective_subjective_text = '2833047 and 1111 people live in this area.'
objective_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
subjective_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."


def test_given_an_invalid_text_when_sentiment_subjectivity_analysis_is_applied_then_no_sentiment_subjectivity_analysis_info_is_returned():
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


def test_given_a_text_when_sentiment_subjectivity_analysis_is_applied_then_subjective_analysis_info_is_returned():
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
        "Sentiment subjectivity didn't match for the text"
    # given,  when
    actual_results = sentiment_subjectivity_summarised(actual_results)
    # then
    assert expected_summarised_sentiment_subjectivity == actual_results, \
        "Summarised Sentiment subjectivity didn't match for the text"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
sentiment_subjectivity_score_to_words_mapping = [
    (1, 1.0, "Very subjective"),  # ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    (0.99555, 0.99555, "Very subjective"),  # ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite subjective"),  # ["Quite subjective", 87, 99],  # Almost Certain: 93%: Give or take 6%
    (0.65, 0.65, "Pretty subjective"),  # ["Pretty subjective", 63, 87],  # Probable: 75%: Give or take about 12%
    (0.50, 0.50, "Objective/subjective"),
    # ["Objective/subjective", 40, 63],  # Chances About Even: 50%: Give or take about 10%
    (0.35, 0.35, "Pretty objective"),  # ["Pretty objective", 12, 40],  # Probably Not: 30%: Give or take about 10%
    (0.08, 0.08, "Quite objective"),  # ["Quite objective", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    (0.01, 0.01, "Very objective"),  # ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
    (0.0, 0.00, "Very objective"),  # ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_subjectivity_in_words",
                         sentiment_subjectivity_score_to_words_mapping)
def test_given_sentiment_subjectivity_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_subjectivity_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_subjectivity_in_words:", expected_subjectivity_in_words)
    actual_result = sentiment_subjectivity(original_score)

    # then
    assert expected_subjectivity_in_words == actual_result
