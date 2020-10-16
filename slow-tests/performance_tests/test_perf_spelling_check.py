import os
from contextlib import redirect_stdout
from datetime import datetime
from time import time

from line_profiler import LineProfiler

from nlp_profiler.high_level_features.spelling_quality_check \
    import spelling_quality_score
from .common_functions import shorten_sha, git_current_head_sha, generate_data

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'
TARGET_PROFILE_REPORT_FOLDER = '.cprofile/'


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # given
    if not os.path.exists(TARGET_PROFILE_REPORT_FOLDER):
        os.makedirs(TARGET_PROFILE_REPORT_FOLDER)
    profile = LineProfiler()
    source_data = generate_data()
    expected_execution_time = 32  # benchmarked: (first-time) 31.051079034805298, (cached) 0.918392 seconds

    # when: using default method (joblib Parallel) for parallelisation
    start_execution_time = time()
    profile_wrapper = profile(spelling_quality_score)
    for each in source_data:
        profile_wrapper(each)
    actual_execution_time = time() - start_execution_time

    output_filename = f'{TARGET_PROFILE_REPORT_FOLDER}/spelling_quality_check-' \
                      f'{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}-' \
                      f'{shorten_sha(git_current_head_sha())}'
    with open(f'{output_filename}.txt', 'w') as file:
        with redirect_stdout(file):
            profile.print_stats()

    profile.dump_stats(f'{output_filename}.lprof')

    # then
    assert actual_execution_time <= expected_execution_time, \
        f"Expected duration: {expected_execution_time}, Actual duration: {actual_execution_time}. " \
        f"Slow down by: {abs(actual_execution_time - expected_execution_time)} seconds. " \
        f"We have crossed the benchmark limit after a speed up via commit a81ed70."
