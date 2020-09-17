from nlp_profiler.core import gather_words, words_count  # noqa

text_with_a_number = '2833047 people live in this area'


def test_given_a_text_with_words_when_parsed_then_return_only_the_words():
    # given
    expected_results = ['people', 'live', 'in', 'this', 'area']

    # when
    actual_results = gather_words(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected words in the text"


def test_given_a_text_with_words_when_counted_then_return_count_of_words():
    # given, when
    actual_results = words_count(text_with_a_number)

    # then
    assert actual_results == 5, \
        "Didn't find the expected number of words in the text"
