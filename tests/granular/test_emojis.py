from nlp_profiler.core import gather_emojis, count_emojis  # noqa

text_with_emojis = "I love ⚽ very much 😁"


def test_given_a_text_with_emoji_when_parsed_then_return_only_emojis():
    # given
    expected_results = ['soccer_ball', 'beaming_face_with_smiling_eyes']

    # when
    actual_results = gather_emojis(text_with_emojis)

    # then
    assert expected_results == actual_results, \
        "Didn't find the two emojis ⚽ and 😁 in the text"


def test_given_a_text_with_emoji_when_counted_then_return_number_of_emojis_found():
    # given, when
    actual_results = count_emojis(text_with_emojis)

    # then
    assert actual_results == 2, \
        "Didn't find the expected two emojis in the text"
