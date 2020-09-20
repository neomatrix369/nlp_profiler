import os
import sys
import time

sys.path.insert(0, '.')
from nlp_profiler.spelling_quality_check import spelling_quality_score
from line_profiler import LineProfiler

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f'{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data'


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # given
    profile = LineProfiler()
    source_data = generate_data()
    expected_execution_time = 0.025  # seconds

    # when: using default method (joblib Parallel) for parallelisation
    start_execution_time = time.time()
    profile_wrapper = profile(spelling_quality_score)
    [profile_wrapper(each) for each in source_data]
    end_execution_time = time.time()
    actual_execution_time = end_execution_time - start_execution_time
    profile.print_stats()
    profile.dump_stats(f'.cprofile/spelling_quality_check-{time.time()}.lprof')

    # then
    assert expected_execution_time <= actual_execution_time


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
    for index in range(5):
        new_data.extend(data)
    return new_data
