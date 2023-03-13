from nlp_profiler.granular_features import apply_granular_features

from tests.common_functions import assert_benchmark_multiple_features


def test_given_a_text_column_when_profiler_is_applied_with_granular_analysis_then_it_finishes_quick():
    # benchmarked:
    # Commit: 8dce2b47f
    #   (first-time): 24.814494848251343 seconds
    #   (cached): 14.4172 seconds
    expected_execution_time = 25

    assert_benchmark_multiple_features(
        expected_execution_time,
        apply_granular_features,
        "Granular Features",
        "default",
        "apply_granular_features",
        "46646bf",
    )
