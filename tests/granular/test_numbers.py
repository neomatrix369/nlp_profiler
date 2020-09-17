from nlp_profiler.core import gather_whole_numbers, count_whole_numbers  # noqa

text_with_a_number = '2833047 people live in this area'


def test_given_a_text_with_numbers_when_parsed_then_return_only_the_numbers():
    # given,
    expected_results = ['2833047']

    # when
    actual_results = gather_whole_numbers(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the number '2833047' in the text"


def test_given_a_text_with_a_number_when_counted_then_return_count_of_numbers_found():
    # given, when
    actual_results = count_whole_numbers(text_with_a_number)

    # then
    assert actual_results == 1, \
        "Didn't find the expected single number in the text"
