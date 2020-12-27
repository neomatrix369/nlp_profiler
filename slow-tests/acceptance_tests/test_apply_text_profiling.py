import os

import pandas as pd
from pandas.util.testing import assert_equal

from nlp_profiler.constants \
    import HIGH_LEVEL_OPTION, GRANULAR_OPTION, GRAMMAR_CHECK_OPTION, \
    SPELLING_CHECK_OPTION, EASE_OF_READING_CHECK_OPTION
from nlp_profiler.core import apply_text_profiling
from tests.common_functions import generate_data, remove_joblib_cache

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'


def setup_model(module):
    remove_joblib_cache()


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
    assert_equal(expected_dataframe.drop('text', axis=1), actual_dataframe.drop('text', axis=1))


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
    assert_equal(expected_dataframe.drop('text', axis=1), actual_dataframe.drop('text', axis=1))


def create_source_dataframe():
    data = generate_data()
    return pd.DataFrame(data, columns=['text'])
