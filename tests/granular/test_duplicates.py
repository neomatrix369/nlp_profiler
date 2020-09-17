from nlp_profiler.core import gather_duplicates, count_duplicates  # noqa

text_with_a_number = '2833047 people live in this area'
text_with_duplicates = 'Everyone here is so hardworking. hardworking people. ' \
                       'I think hardworking people are a good trait in our company'


def test_given_a_text_with_no_duplicates_when_parsed_then_return_empty():
    # given
    expected_results = {}

    # when
    actual_results = gather_duplicates(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Should have NOT found duplicates in the text"


def test_given_a_text_with_duplicates_when_parsed_then_return_the_duplicates():
    # given
    expected_results = {'.': 2, 'hardworking': 3, 'people': 2}

    # when
    actual_results = gather_duplicates(text_with_duplicates)

    # then
    assert expected_results == actual_results, \
        "Should have found multiple duplicates in the text"


def test_given_a_text_with_duplicates_when_counted_then_return_the_duplicates_count():
    # given,  when
    actual_results = count_duplicates(text_with_a_number)

    # then
    assert actual_results == 0, \
        "Should have NOT found duplicates in the text"

    # given,  when
    actual_results = count_duplicates(text_with_duplicates)

    # then
    assert actual_results == 3, \
        "Should have found a few duplicates in the text"
