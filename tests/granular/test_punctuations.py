from nlp_profiler.core import gather_punctuations, count_punctuations  # noqa

text_with_punctuations = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."


def test_given_a_text_with_punctuations_when_parsed_then_return_only_punctuations():
    # given
    expected_results = ["'", ',', '-', '(', ';', ')', '.']

    # when
    actual_results = gather_punctuations(text_with_punctuations)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected punctuations in the text"


def test_given_a_text_with_punctuations_when_counted_then_return_count_of_punctuations():
    # given, when
    actual_results = count_punctuations(text_with_punctuations)

    # then
    assert actual_results == 7, \
        "Didn't find the expected number of punctuation marks in the text"
