from nlp_profiler.high_level_features.ease_of_reading_check \
    import ease_of_reading_score
from .common_functions import assert_benchmark


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # benchmarked:
    #   (first-time): 2.6088788509368896 seconds
    #   (cached): 0.0048389434814453125 seconds
    expected_execution_time = 2.8

    assert_benchmark(expected_execution_time,
                     ease_of_reading_score,
                     'ease_of_reading_score',
                     'aaceb9d')
