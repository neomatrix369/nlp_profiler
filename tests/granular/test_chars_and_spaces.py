from nlp_profiler.core import count_spaces, count_characters_excluding_spaces  # noqa

text_with_a_number = '2833047 people live in this area'


def test_given_a_text_with_spaces_when_counted_for_spaces_then_return_that_count():
    # given, when
    actual_results = count_spaces(text_with_a_number)

    # then
    assert actual_results == 5, \
        "Didn't find the expected number of spaces in the text"


def test_given_a_text_with_spaces_when_counted_for_chars_then_return_that_count():
    # given, when
    actual_results = count_characters_excluding_spaces(text_with_a_number)

    # then
    assert actual_results == 27, \
        "Didn't find the expected number of chars without spaces in the text"
