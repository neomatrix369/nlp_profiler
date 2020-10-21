from nlp_profiler.high_level_features.spelling_quality_check \
    import spelling_quality_score
from .common_functions import assert_benchmark


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # benchmarked:
    #   (first-time) 31.051079034805298 seconds
    #   (cached) 0.918392 seconds
    expected_execution_time = 32

    assert_benchmark(expected_execution_time,
                     spelling_quality_score,
                     'spelling_quality_check',
                     'a81ed70')
