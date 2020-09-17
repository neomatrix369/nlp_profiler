from nlp_profiler.core import gather_alpha_numeric, count_alpha_numeric  # noqa

text_with_alphanumeric_chars = '2833047 people live in this area'


def test_given_a_alphanumeric_text_when_parsed_then_return_alphanumeric_chars():
    # given,
    expected_results = list(text_with_alphanumeric_chars.replace(' ', ''))

    # when
    actual_results = gather_alpha_numeric(text_with_alphanumeric_chars)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected alpha numeric chars in the text"


def test_given_a_alphanumeric_text_when_counted_then_return_number_of_alphanumeric_chars():
    # given
    expected_results = len(list(text_with_alphanumeric_chars.replace(' ', '')))

    # when
    actual_results = count_alpha_numeric(text_with_alphanumeric_chars)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected number of alpha numeric chars in the text"
