from nlp_profiler.core import sentiment_polarity_score, \
    sentiment_polarity_summarised, sentiment_polarity  # noqa

some_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."


def test_given_a_text_when_sentiment_analysis_is_applied_then_sentiment_analysis_info_is_returned():
    # given
    expected_results = 0.375000

    # when
    actual_results = sentiment_polarity_score(some_text)

    # then
    assert expected_results == actual_results, \
        "Sentiment polarity score didn't match for the text"

    # given
    expected_results = 'Pretty positive'

    # when
    actual_results = sentiment_polarity(actual_results)

    # then
    assert expected_results == actual_results, \
        "Sentiment polarity didn't match for the text"

    # given
    expected_results = 'Positive'

    # when
    actual_results = sentiment_polarity_summarised(actual_results)

    # then
    assert expected_results == actual_results, \
        "Summarised Sentiment polarity didn't match for the text"
