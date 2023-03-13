from nlp_profiler.high_level_features.spelling_quality_check import spelling_quality_score

from tests.common_functions import assert_benchmark


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # benchmarked:
    #   (first-time) 31.051079034805298 seconds
    #   (cached) 0.918392 seconds
    #   (At commit a81ed70) 31.051079034805298 seconds
    #   (GitHub Actions at c9cdf1b - Linux) 56.95482301712036 to 63.139883041381836 seconds
    #   (GitHub Actions at c9cdf1b - Windows) 81.37646651268005 to 85.25863766670227 seconds
    expected_execution_time = 90

    assert_benchmark(expected_execution_time, spelling_quality_score, "spelling_quality_check", "c9cdf1b")
