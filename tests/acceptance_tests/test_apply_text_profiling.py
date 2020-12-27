import os

import pandas as pd
from pandas.util.testing import assert_frame_equal

from nlp_profiler.constants \
    import PARALLELISATION_METHOD_OPTION, SWIFTER_METHOD, \
    HIGH_LEVEL_OPTION, GRANULAR_OPTION, SPELLING_CHECK_OPTION, EASE_OF_READING_CHECK_OPTION
from nlp_profiler.core import apply_text_profiling
from nlp_profiler.granular_features.punctuations import ADDITIONAL_SYMBOLS

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'


def test_given_a_text_column_when_profiler_using_parallel_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when: using default method (joblib Parallel) for parallelisation
    actual_dataframe = apply_text_profiling(source_dataframe, "text")

    # then
    assert_frame_equal(expected_dataframe.drop('text', axis=1),
                       actual_dataframe.drop('text', axis=1), check_like=True)


def test_given_a_text_column_when_profiler_using_swifter_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when: using swifter method for parallelisation
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", params={PARALLELISATION_METHOD_OPTION: SWIFTER_METHOD}
    )

    # then
    assert_frame_equal(expected_dataframe.drop('text', axis=1),
                       actual_dataframe.drop('text', axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_without_high_level_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe_no_high_level.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", {
            HIGH_LEVEL_OPTION: False,
            SPELLING_CHECK_OPTION: False,
            GRANULAR_OPTION: True,
            EASE_OF_READING_CHECK_OPTION: False
        }
    )

    # then
    assert_frame_equal(expected_dataframe.drop('text', axis=1),
                       actual_dataframe.drop('text', axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_without_granular_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f'{EXPECTED_DATA_PATH}/expected_profiled_dataframe_no_granular.csv'
    expected_dataframe = pd.read_csv(csv_filename)

    # when
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", {GRANULAR_OPTION: False}
    )

    # then
    assert_frame_equal(expected_dataframe.drop('text', axis=1),
                       actual_dataframe.drop('text', axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_with_then_all_options_disabled_then_no_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    expected_dataframe = source_dataframe.copy()

    # when
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", {HIGH_LEVEL_OPTION: False, \
                                   SPELLING_CHECK_OPTION: False, \
                                   GRANULAR_OPTION: False, \
                                   EASE_OF_READING_CHECK_OPTION: False}
    )

    # then
    assert_frame_equal(actual_dataframe.drop('text', axis=1),
                       expected_dataframe.drop('text', axis=1),
                       check_like=True)  # source dataframe is returned


def create_source_dataframe():
    repeated_symbols = ADDITIONAL_SYMBOLS[0] + ADDITIONAL_SYMBOLS[0]
    text_with_emojis = "I love ⚽ very much 😁."
    text_with_a_number = '2833047 people live in this area. It is not a good area.'
    text_with_two_numbers = '2833047 and 1111 people live in this area.'
    text_with_punctuations = "This sentence does not seem to have too many commas, periods or semicolons (;)."
    text_with_a_date = "The date today is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
    text_with_dates = "The date today is 28/04/2020 and tomorrow's date is 29/04/2020."
    text_with_duplicates = 'Everyone here works so hard. People work hard. ' \
                           'I think they have a good trait.'
    text_with_repeated_letters = 'Harrington PPPPPPpppppeople work hard.' \
                                 ' I think they have a goodd traittttt.'
    text_with_repeated_digits = '283047 people live in this area3333 22224444'
    text_with_repeated_punctuations = '283047 people live in this area[[[ ]]] :::;;;;' + repeated_symbols
    text_with_repeated_spaces = '283047   people live in this  area'
    text_with_whitespaces = '2833047 pe\nople li\tve i\rn this area'
    text_with_repeated_whitespaces = '2833047   \r\rpeople\n\n   live in   th\nis are\t\ta'
    text_with_english_chars = '±§£ABCDEabcdef0123456789\nis are\t\n' + r"""!#$%&()*+-./:;<=>?@[\]^_`{|}~"""
    text_with_non_english_chars = '2833047 pe\nople li\tve i\rn this area' \
                                  '‚ƒ„…†‡ˆ‰Š‹ŒŽ•™š›œžŸ¡¢¤¥¦¨©ª«¬­®¯°²³´"' \
                                  'µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß' \
                                  'àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ' \
                                  'This sentence is in japanese (kana) ろぬふうえおやゆゆわほへへて' \
                                  'This sentence is in japanese (kana compact) おっあこおおがおんわお' \
                                  'فصصصشببلااتنخمككك This sentence is in arabic'
    data = [text_with_emojis, text_with_a_number, text_with_two_numbers, text_with_repeated_letters,
            text_with_repeated_digits, text_with_punctuations, text_with_repeated_punctuations,
            text_with_a_date, text_with_dates, text_with_duplicates, text_with_repeated_spaces,
            text_with_whitespaces, text_with_repeated_whitespaces,
            text_with_english_chars, text_with_non_english_chars]

    return pd.DataFrame(data, columns=['text'])
