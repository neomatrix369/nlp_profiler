import pandas as pd

from nlp_profiler.constants import CHARACTERS_COUNT_COL, SENTENCES_COUNT_COL
from nlp_profiler.constants import \
    DATES_COUNT_COL, STOP_WORDS_COUNT_COL, PUNCTUATIONS_COUNT_COL, \
    REPEATED_PUNCTUATIONS_COUNT_COL, NON_ALPHA_NUMERIC_COUNT_COL
from nlp_profiler.constants import \
    DEFAULT_PARALLEL_METHOD
from nlp_profiler.constants import \
    DUPLICATES_COUNT_COL, COUNT_WORDS_COL, SPACES_COUNT_COL, CHARS_EXCL_SPACES_COUNT_COL, \
    REPEATED_SPACES_COUNT_COL, WHITESPACES_COUNT_COL, CHARS_EXCL_WHITESPACES_COUNT_COL, \
    REPEATED_WHITESPACES_COUNT_COL, ALPHA_NUMERIC_COUNT_COL, REPEATED_LETTERS_COUNT_COL, \
    WHOLE_NUMBERS_COUNT_COL, REPEATED_DIGITS_COUNT_COL, EMOJI_COUNT_COL, \
    NOUN_PHASE_COUNT_COL, ENGLISH_CHARACTERS_COUNT_COL, NON_ENGLISH_CHARACTERS_COUNT_COL
from nlp_profiler.generate_features import generate_features
from nlp_profiler.granular_features.alphanumeric import count_alpha_numeric
from nlp_profiler.granular_features.chars_spaces_and_whitespaces \
    import count_spaces, count_chars, count_characters_excluding_spaces, \
    count_repeated_spaces
from nlp_profiler.granular_features.chars_spaces_and_whitespaces import \
    count_whitespaces, count_characters_excluding_whitespaces, \
    count_repeated_whitespaces
from nlp_profiler.granular_features.dates import count_dates
from nlp_profiler.granular_features.duplicates import count_duplicates
from nlp_profiler.granular_features.emojis import count_emojis
from nlp_profiler.granular_features.english_non_english_chars \
    import count_english_chars, count_non_english_chars
from nlp_profiler.granular_features.letters import count_repeated_letters
from nlp_profiler.granular_features.non_alphanumeric import count_non_alpha_numeric
from nlp_profiler.granular_features.noun_phase_count import count_noun_phase
from nlp_profiler.granular_features.numbers import count_whole_numbers, count_repeated_digits
from nlp_profiler.granular_features.punctuations import count_punctuations, count_repeated_punctuations
from nlp_profiler.granular_features.sentences import count_sentences
from nlp_profiler.granular_features.stop_words import count_stop_words
from nlp_profiler.granular_features.words import count_words


def apply_granular_features(heading: str,
                            new_dataframe: pd.DataFrame,
                            text_column: str,
                            parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    steps_for_features = [
        (SENTENCES_COUNT_COL, text_column, count_sentences),
        (CHARACTERS_COUNT_COL, text_column, count_chars),
        (REPEATED_LETTERS_COUNT_COL, text_column, count_repeated_letters),
        (SPACES_COUNT_COL, text_column, count_spaces),
        (CHARS_EXCL_SPACES_COUNT_COL, text_column, count_characters_excluding_spaces),
        (REPEATED_SPACES_COUNT_COL, text_column, count_repeated_spaces),
        (WHITESPACES_COUNT_COL, text_column, count_whitespaces),
        (CHARS_EXCL_WHITESPACES_COUNT_COL, text_column, count_characters_excluding_whitespaces),
        (REPEATED_WHITESPACES_COUNT_COL, text_column, count_repeated_whitespaces),
        (COUNT_WORDS_COL, text_column, count_words),
        (DUPLICATES_COUNT_COL, text_column, count_duplicates),
        (EMOJI_COUNT_COL, text_column, count_emojis),
        (REPEATED_DIGITS_COUNT_COL, text_column, count_repeated_digits),
        (WHOLE_NUMBERS_COUNT_COL, text_column, count_whole_numbers),
        (ALPHA_NUMERIC_COUNT_COL, text_column, count_alpha_numeric),
        (NON_ALPHA_NUMERIC_COUNT_COL, text_column, count_non_alpha_numeric),
        (PUNCTUATIONS_COUNT_COL, text_column, count_punctuations),
        (REPEATED_PUNCTUATIONS_COUNT_COL, text_column, count_repeated_punctuations),
        (STOP_WORDS_COUNT_COL, text_column, count_stop_words),
        (DATES_COUNT_COL, text_column, count_dates),
        (NOUN_PHASE_COUNT_COL, text_column, count_noun_phase),
        (ENGLISH_CHARACTERS_COUNT_COL, text_column, count_english_chars),
        (NON_ENGLISH_CHARACTERS_COUNT_COL, text_column, count_non_english_chars)
    ]
    generate_features(
        heading, steps_for_features,
        new_dataframe, parallelisation_method
    )
