import os

import pandas as pd
from pandas.util.testing import assert_equal

from nlp_profiler.constants \
    import HIGH_LEVEL_OPTION, GRANULAR_OPTION, GRAMMAR_CHECK_OPTION, \
        SPELLING_CHECK_OPTION, EASE_OF_READING_CHECK_OPTION
from nlp_profiler.core import apply_text_profiling

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'


def test_given_a_text_column_when_profiler_is_applied_grammar_check_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe_grammar_check.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when: in the interest of time, only perform grammar check
    # other tests are covering for high_level and granular functionality
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", {HIGH_LEVEL_OPTION: False,
                                   SPELLING_CHECK_OPTION: False,
                                   GRANULAR_OPTION: False,
                                   EASE_OF_READING_CHECK_OPTION: False,
                                   GRAMMAR_CHECK_OPTION: True}
    )

    # then
    assert_equal(expected_dataframe, actual_dataframe)


def test_given_a_text_column_when_profiler_is_applied_ease_of_reading_check_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe_ease_of_reading_check.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when: in the interest of time, only perform ease of reading check
    # other tests are covering for high_level and granular functionality
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", {HIGH_LEVEL_OPTION: False,
                                   SPELLING_CHECK_OPTION: False,
                                   GRANULAR_OPTION: False,
                                   EASE_OF_READING_CHECK_OPTION: True,
                                   GRAMMAR_CHECK_OPTION: False}
    )

    # then
    assert_equal(expected_dataframe, actual_dataframe)

def create_source_dataframe():
    text_with_emojis = "I love ⚽ very much 😁."
    text_with_a_number = '2833047 people live in this area. It is not a good area.'
    text_with_two_numbers = '2833047 and 1111 people live in this area.'
    text_with_punctuations = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
    text_with_a_date = "Todays date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
    text_with_dates = "Todays date is 28/04/2020 and tomorrow's date is 29/04/2020."
    text_with_duplicates = 'Everyone here is so hardworking. Hardworking people. ' \
                           'I think hardworking people are a good trait in our company.'
    text_with_repeated_letters = 'Harrington PPPPPPpppppeople work hard. ' \
                           'I think they have a goodd traittttt.'
    text_with_repeated_digits = '283047 people live in this area3333 22224444'
    text_with_repeated_punctuations = '283047 people live in this area[[[ ]]] :::;;;;'
    data = [text_with_emojis, text_with_a_number, text_with_two_numbers, text_with_repeated_letters,
            text_with_repeated_digits, text_with_punctuations, text_with_repeated_punctuations,
            text_with_a_date, text_with_dates, text_with_duplicates]

    return pd.DataFrame(data, columns=['text'])
