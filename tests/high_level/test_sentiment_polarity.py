import math

from nlp_profiler.core import NOT_APPLICABLE, sentiment_polarity_score, \
    sentiment_polarity_summarised, sentiment_polarity  # noqa

positive_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
negative_text = "2833047 people live in this area. It is not a good area."
neutral_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."


def test_given_an_invalid_text_when_sentiment_analysis_is_applied_then_no_sentiment_analysis_info_is_returned():
    # given, when: text is not defined
    actual_results = sentiment_polarity_score(None)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Sentiment polarity score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when: empty text
    actual_results = sentiment_polarity_score("")

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Sentiment polarity score should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"

    # given, when
    actual_results = sentiment_polarity(NOT_APPLICABLE)

    # then
    assert actual_results == NOT_APPLICABLE, \
        f"Sentiment polarity should NOT " \
        f"have been returned, expected {NOT_APPLICABLE}"


def test_given_a_text_when_sentiment_analysis_is_applied_then_sentiment_analysis_info_is_returned():
    assert_text_polarity(positive_text, 0.375000, 'Pretty positive', 'Positive')
    assert_text_polarity(negative_text, -0.10681818181818181, 'Pretty negative', 'Negative')
    assert_text_polarity(neutral_text, 0.0, 'Neutral', 'Neutral')


def assert_text_polarity(text,
                         expected_polarity_score,
                         expected_polarity,
                         expected_polarity_summarised):
    # given, when
    actual_results = sentiment_polarity_score(text)
    # then
    assert math.isclose(expected_polarity_score, actual_results,
                        rel_tol=1e-09, abs_tol=0.0), \
        "Sentiment polarity score didn't match for the text"

    # given, when
    actual_results = sentiment_polarity(actual_results)
    # then
    assert expected_polarity == actual_results, \
        "Sentiment polarity didn't match for the text"

    # given, when
    actual_results = sentiment_polarity_summarised(actual_results)
    # then
    assert expected_polarity_summarised == actual_results, \
        "Summarised Sentiment polarity didn't match for the text"
