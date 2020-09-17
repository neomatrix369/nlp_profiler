from nlp_profiler.core import gather_sentences, count_sentences  # noqa

text_with_emojis = "I love ⚽ very much 😁"
text_with_a_number = '2833047 people live in this area'
text_with_two_sentences = text_with_a_number + "." + text_with_emojis


def test_given_a_text_with_sentences_when_parsed_then_return_the_sentences():
    # given
    expected_results = [text_with_a_number]

    # when
    actual_results = gather_sentences(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected sentence in the text"

    # given
    expected_results = [text_with_a_number, text_with_emojis]

    # when
    actual_results = gather_sentences(text_with_two_sentences)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected two sentences in the text"


def test_given_a_text_with_sentences_when_counted_then_return_the_count_of_sentences():
    # given, when
    actual_results = count_sentences(text_with_a_number)

    # then
    assert actual_results == 1, \
        "Didn't find the single expected sentence in the text"

    # given, when
    actual_results = count_sentences(text_with_two_sentences)

    # then
    assert actual_results == 2, \
        "Didn't find the two sentences in the text"
