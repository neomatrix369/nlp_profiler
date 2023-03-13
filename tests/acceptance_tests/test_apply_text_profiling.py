import os

import pandas as pd
from pandas.util.testing import assert_frame_equal

from nlp_profiler.constants import (
    PARALLELISATION_METHOD_OPTION,
    SWIFTER_METHOD,
    HIGH_LEVEL_OPTION,
    GRANULAR_OPTION,
    SPELLING_CHECK_OPTION,
    EASE_OF_READING_CHECK_OPTION,
)
from nlp_profiler.core import apply_text_profiling
from tests.common_functions import generate_data, remove_joblib_cache

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f"{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data"


def setup_model(module):
    remove_joblib_cache()


def test_given_a_text_column_when_profiler_using_parallel_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f"{EXPECTED_DATA_PATH}/expected_profiled_dataframe.csv"
    expected_dataframe = pd.read_csv(csv_filename)

    # when: using default method (joblib Parallel) for parallelisation
    actual_dataframe = apply_text_profiling(source_dataframe, "text")

    # then
    assert_frame_equal(expected_dataframe.drop("text", axis=1), actual_dataframe.drop("text", axis=1), check_like=True)


def test_given_a_text_column_when_profiler_using_swifter_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f"{EXPECTED_DATA_PATH}/expected_profiled_dataframe.csv"
    expected_dataframe = pd.read_csv(csv_filename)

    # when: using swifter method for parallelisation
    actual_dataframe = apply_text_profiling(
        source_dataframe, "text", params={PARALLELISATION_METHOD_OPTION: SWIFTER_METHOD}
    )

    # then
    assert_frame_equal(expected_dataframe.drop("text", axis=1), actual_dataframe.drop("text", axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_without_high_level_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f"{EXPECTED_DATA_PATH}/expected_profiled_dataframe_no_high_level.csv"
    expected_dataframe = pd.read_csv(csv_filename)

    # when
    actual_dataframe = apply_text_profiling(
        source_dataframe,
        "text",
        {
            HIGH_LEVEL_OPTION: False,
            SPELLING_CHECK_OPTION: False,
            GRANULAR_OPTION: True,
            EASE_OF_READING_CHECK_OPTION: False,
        },
    )

    # then
    assert_frame_equal(expected_dataframe.drop("text", axis=1), actual_dataframe.drop("text", axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_without_granular_analysis_then_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    csv_filename = f"{EXPECTED_DATA_PATH}/expected_profiled_dataframe_no_granular.csv"
    expected_dataframe = pd.read_csv(csv_filename)

    # when
    actual_dataframe = apply_text_profiling(source_dataframe, "text", {GRANULAR_OPTION: False})

    # then
    assert_frame_equal(expected_dataframe.drop("text", axis=1), actual_dataframe.drop("text", axis=1), check_like=True)


def test_given_a_text_column_when_profiler_is_applied_with_then_all_options_disabled_then_no_profiled_dataset_is_returned():
    # given
    source_dataframe = create_source_dataframe()
    expected_dataframe = source_dataframe.copy()

    # when
    actual_dataframe = apply_text_profiling(
        source_dataframe,
        "text",
        {
            HIGH_LEVEL_OPTION: False,
            SPELLING_CHECK_OPTION: False,
            GRANULAR_OPTION: False,
            EASE_OF_READING_CHECK_OPTION: False,
        },
    )

    # then
    assert_frame_equal(
        actual_dataframe.drop("text", axis=1), expected_dataframe.drop("text", axis=1), check_like=True
    )  # source dataframe is returned


def create_source_dataframe():
    data = generate_data()
    return pd.DataFrame(data, columns=["text"])
