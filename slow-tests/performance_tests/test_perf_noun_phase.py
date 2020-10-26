from nlp_profiler.granular_features.noun_phase_count import count_noun_phase
from .common_functions import assert_benchmark


def test_given_a_text_column_when_profiler_is_applied_with_high_level_analysis_then_it_finishes_quick():
    # benchmarked:
    #   (first-time): 0.7727630138397217 seconds
    #   (cached): 0.7233660221099854 seconds
    expected_execution_time = 0.10

    assert_benchmark(expected_execution_time,
                     count_noun_phase,
                     'noun_phrase_count',
                     '5088e8d')
