import pandas as pd

from nlp_profiler.alphanumeric import count_alpha_numeric
from nlp_profiler.chars_and_spaces \
    import count_spaces, count_chars, count_characters_excluding_spaces
from nlp_profiler.constants import \
    ALPHA_NUMERIC_COUNT_COL, WHOLE_NUMBERS_COUNT_COL, EMOJI_COUNT_COL, CHARS_EXCL_SPACES_COUNT_COL
from nlp_profiler.constants import CHARACTERS_COUNT_COL, SENTENCES_COUNT_COL
from nlp_profiler.constants import \
    DATES_COUNT_COL, STOP_WORDS_COUNT_COL, PUNCTUATIONS_COUNT_COL, NON_ALPHA_NUMERIC_COUNT_COL
from nlp_profiler.constants import \
    DEFAULT_PARALLEL_METHOD
from nlp_profiler.constants import DUPLICATES_COUNT_COL, COUNT_WORDS_COL, SPACES_COUNT_COL
from nlp_profiler.dates import count_dates
from nlp_profiler.duplicates import count_duplicates
from nlp_profiler.emojis import count_emojis
from nlp_profiler.generate_features import generate_features
from nlp_profiler.non_alphanumeric import count_non_alpha_numeric
from nlp_profiler.numbers import count_whole_numbers
from nlp_profiler.punctuations import count_punctuations
from nlp_profiler.sentences import count_sentences
from nlp_profiler.stop_words import count_stop_words
from nlp_profiler.words import count_words


def apply_granular_features(heading: str,
                            new_dataframe: pd.DataFrame,
                            text_column: dict,
                            parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    granular_features_steps = [
        (SENTENCES_COUNT_COL, text_column, count_sentences),
        (CHARACTERS_COUNT_COL, text_column, count_chars),
        (SPACES_COUNT_COL, text_column, count_spaces),
        (COUNT_WORDS_COL, text_column, count_words),
        (DUPLICATES_COUNT_COL, text_column, count_duplicates),
        (CHARS_EXCL_SPACES_COUNT_COL, text_column, count_characters_excluding_spaces),
        (EMOJI_COUNT_COL, text_column, count_emojis),
        (WHOLE_NUMBERS_COUNT_COL, text_column, count_whole_numbers),
        (ALPHA_NUMERIC_COUNT_COL, text_column, count_alpha_numeric),
        (NON_ALPHA_NUMERIC_COUNT_COL, text_column, count_non_alpha_numeric),
        (PUNCTUATIONS_COUNT_COL, text_column, count_punctuations),
        (STOP_WORDS_COUNT_COL, text_column, count_stop_words),
        (DATES_COUNT_COL, text_column, count_dates),
    ]
    generate_features(
        heading, granular_features_steps,
        new_dataframe, parallelisation_method
    )
