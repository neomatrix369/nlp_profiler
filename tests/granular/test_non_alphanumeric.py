from nlp_profiler.core \
    import gather_non_alpha_numeric, count_non_alpha_numeric  # noqa

text_with_a_number = '2833047 people live in this area'
text_with_emojis = "I love ⚽ very much 😁"
text_with_alphanumeric_chars = '2833047 people live in this area'


def test_given_a_text_with_non_alphanumeric_chars_when_parsed_then_return_non_alphanumeric_chars():
    # given: a number in a text
    expected_results = [' ', ' ', ' ', ' ', ' ']

    # when
    actual_results = gather_non_alpha_numeric(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected non-alphanumeric chars in the text with a number"

    # given: emojis in text
    expected_results = [' ', ' ', '⚽', ' ', ' ', ' ', '😁']

    # when
    actual_results = gather_non_alpha_numeric(text_with_emojis)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected non-alphanumeric chars in the text with emoji"


def test_given_a_alphanumeric_text_when_counted_then_return_number_of_alphanumeric_chars():
    # given, when
    actual_results = count_non_alpha_numeric(text_with_a_number)

    # then
    assert actual_results == 5, \
        "Didn't find the expected number of non-alphanumeric " \
        "chars in the text with a number"

    # given, when
    actual_results = count_non_alpha_numeric(text_with_emojis)

    # then
    assert actual_results == 7, \
        "Didn't find the expected number of non-alphanumeric " \
        "chars in the text with emojis"
