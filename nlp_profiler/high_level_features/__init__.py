import pandas as pd

from nlp_profiler.constants import \
    DEFAULT_PARALLEL_METHOD
from nlp_profiler.constants import \
    SENTIMENT_POLARITY_SCORE_COL, SENTIMENT_POLARITY_COL, SENTIMENT_POLARITY_SUMMARISED_COL
from nlp_profiler.constants import \
    SENTIMENT_SUBJECTIVITY_COL, SENTIMENT_SUBJECTIVITY_SCORE_COL, SENTIMENT_SUBJECTIVITY_SUMMARISED_COL
from nlp_profiler.generate_features import generate_features
from nlp_profiler.high_level_features.sentiment_polarity \
    import sentiment_polarity_score, sentiment_polarity, \
    sentiment_polarity_summarised
from nlp_profiler.high_level_features.sentiment_subjectivity \
    import sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity


def apply_high_level_features(heading: str,
                              new_dataframe: pd.DataFrame,
                              text_column: dict,
                              parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    high_level_features_steps = [
        (SENTIMENT_POLARITY_SCORE_COL, text_column, sentiment_polarity_score),
        (SENTIMENT_POLARITY_COL, SENTIMENT_POLARITY_SCORE_COL, sentiment_polarity),
        (SENTIMENT_POLARITY_SUMMARISED_COL, SENTIMENT_POLARITY_COL, sentiment_polarity_summarised),
        (SENTIMENT_SUBJECTIVITY_SCORE_COL, text_column, sentiment_subjectivity_score),
        (SENTIMENT_SUBJECTIVITY_COL, SENTIMENT_SUBJECTIVITY_SCORE_COL, sentiment_subjectivity),
        (SENTIMENT_SUBJECTIVITY_SUMMARISED_COL, SENTIMENT_SUBJECTIVITY_COL, sentiment_subjectivity_summarised),
    ]
    generate_features(
        heading, high_level_features_steps,
        new_dataframe, parallelisation_method
    )
