from nlp_profiler.core import gather_dates, count_dates  # noqa

text_with_date = "Todays date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020"
text_with_dates = "Todays date is 28/04/2020 and tomorrow's date is 29/04/2020"


def test_given_a_text_with_a_date_when_parsed_then_return_the_date_found():
    # given
    expected_results = [('28', '04', '2020')]

    # when: NO date-formatting param passed, default format used (dd/mm/yyyy)
    actual_results = gather_dates(text_with_date)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected formatted date in the text (no date-formatting param passed)"

    # given
    expected_results = [('04', '28', '2020')]

    # when: date-formatting param passed
    actual_results = gather_dates(text_with_date, 'mm/dd/yyyy')

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected formatted date in the text (date-formatting param passed)"


def test_given_a_text_with_dates_when_parsed_then_return_the_dates_found():
    # given
    expected_results = [('28', '04', '2020'), ('29', '04', '2020')]

    # when: NO date-formatting param passed, default format used (dd/mm/yyyy)
    actual_results = gather_dates(text_with_dates)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected formatted dates in the text (date-formatting param passed)"


def test_given_a_text_with_one_or_more_dates_when_counted_then_return_number_of_dates_found():
    # given, when
    actual_results = count_dates(text_with_date)

    # then
    assert actual_results == 1, \
        "Didn't find the expected single date in the text"

    # given, when
    actual_results = count_dates(text_with_dates)

    # then
    assert actual_results == 2, \
        "Didn't find the expected two dates in the text"
