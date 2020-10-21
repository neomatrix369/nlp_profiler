from nlp_profiler.high_level_features.grammar_quality_check \
    import grammar_check_score
from .common_functions import assert_benchmark


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # benchmarked:
    #   (first-time): 46.694923639297485 seconds
    #   (cached): 5.918392 seconds
    #   (new run at 5088e8d): 12.149042129516602 seconds
    expected_execution_time = 13

    assert_benchmark(expected_execution_time,
                     grammar_check_score,
                     'grammar_check_score',
                     '51a8952')
