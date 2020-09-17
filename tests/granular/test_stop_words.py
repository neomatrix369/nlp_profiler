from nlp_profiler.core import gather_stop_words, count_stop_words  # noqa

text_with_a_number = '2833047 people live in this area'


def test_given_a_text_with_stop_words_when_parsed_then_return_only_the_stop_words():
    # given
    expected_results = ['in', 'this']

    # when
    actual_results = gather_stop_words(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected words in the text"


def test_given_a_text_with_stop_words_when_counted_then_return_count_of_stop_words():
    # given, when
    actual_results = count_stop_words(text_with_a_number)

    # then
    assert actual_results == 2, \
        "Didn't find the expected number of words in the text"
