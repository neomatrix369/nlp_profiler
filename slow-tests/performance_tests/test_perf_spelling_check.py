import os
import sys
from datetime import datetime
from time import time
from contextlib import redirect_stdout
import git

sys.path.insert(0, '../../performance-tests/high_level')
from nlp_profiler.spelling_quality_check import spelling_quality_score
from line_profiler import LineProfiler

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # given
    TARGET_PROFILE_REPORT_FOLDER = '.cprofile/'
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
    end_execution_time = time()
    actual_execution_time = end_execution_time - start_execution_time

    short_sha = shorten_sha(git_current_head_sha())
    output_filename = f'{TARGET_PROFILE_REPORT_FOLDER}/spelling_quality_check-' \
                      f'{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}-{short_sha}'
    with open(f'{output_filename}.txt', 'w') as file:
        with redirect_stdout(file):
            profile.print_stats()

    profile.dump_stats(f'{output_filename}.lprof')

    # then
    assert actual_execution_time <= expected_execution_time, \
        f"Expected duration: {expected_execution_time}, Actual duration: {actual_execution_time}. " \
        f"Slow down by: {abs(actual_execution_time - expected_execution_time)} seconds. " \
        f"We have crossed the benchmark limit after a speed up via commit a81ed70."


def shorten_sha(long_sha):
    return long_sha[:7]


def git_current_head_sha():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.commit.hexsha


def generate_data() -> list:
    text_with_emojis = "I love ⚽ very much 😁."
    text_with_a_number = '2833047 people live in this area. It is not a good area.'
    text_with_two_numbers = '2833047 and 1111 people live in this area.'
    text_with_punctuations = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
    text_with_a_date = "Todays date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
    text_with_dates = "Todays date is 28/04/2020 and tomorrow's date is 29/04/2020."
    text_with_duplicates = 'Everyone here is so hardworking. Hardworking people. ' \
                           'I think hardworking people are a good trait in our company.'
    data = [text_with_emojis, text_with_a_number, text_with_two_numbers,
            text_with_punctuations, text_with_a_date, text_with_dates, text_with_duplicates]

    new_data = []
    for index in range(1):
        new_data.extend(data)
    return new_data
