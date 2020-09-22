# Copyright 2020 Mani Sarkar

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

### Kaggle Utility script: https://www.kaggle.com/neomatrix369/nlp-profiler-class
### Kaggle kernel: https://www.kaggle.com/neomatrix369/nlp-profiler-simple-dataset
### Jupyter Notebook: https://github.com/neomatrix369/awesome-ai-ml-dl/blob/master/examples/better-nlp/notebooks/jupyter/nlp_profiler.ipynb

import sys
import tempfile

import pandas as pd
import swifter  # noqa
from joblib import Parallel, delayed, Memory
from tqdm.auto import tqdm

from nlp_profiler.alphanumeric import count_alpha_numeric
from nlp_profiler.chars_and_spaces \
    import count_spaces, count_chars, count_characters_excluding_spaces
from nlp_profiler.constants \
    import PARALLELISATION_METHOD, DEFAULT_PARALLEL, SWIFTER, \
    GRANULAR, HIGH_LEVEL, GRAMMAR_CHECK, SPELLING_CHECK
from nlp_profiler.duplicates import count_duplicates
from nlp_profiler.emojis import count_emojis
from nlp_profiler.dates import count_dates
from nlp_profiler.grammar_quality_check \
    import grammar_quality, grammar_check_score
from nlp_profiler.non_alphanumeric import count_non_alpha_numeric
from nlp_profiler.numbers import count_whole_numbers
from nlp_profiler.punctuations import count_punctuations
from nlp_profiler.sentences import count_sentences
from nlp_profiler.sentiment_polarity \
    import sentiment_polarity_score, sentiment_polarity, \
    sentiment_polarity_summarised
from nlp_profiler.sentiment_subjectivity \
    import sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity
from nlp_profiler.spelling_quality_check \
    import spelling_quality_score, spelling_quality, \
    spelling_quality_summarised
from nlp_profiler.stop_words import count_stop_words
from nlp_profiler.words import count_words

memory = Memory(tempfile.gettempdir(), compress=9, verbose=0)


def is_running_from_ipython():
    inJupyter = sys.argv[-1].endswith('json')
    return inJupyter


PROGRESS_BAR_WIDTH = 900 if is_running_from_ipython() else None


def apply_text_profiling(dataframe: pd.DataFrame,
                         text_column: str,
                         params: dict = {}) -> pd.DataFrame:
    columns_to_drop = list(set(dataframe.columns) - set([text_column]))
    new_dataframe = dataframe.drop(columns=columns_to_drop, axis=1).copy()

    default_params = {
        HIGH_LEVEL: True,
        GRANULAR: True,
        GRAMMAR_CHECK: False,  # default: False as slow process but can Enabled
        SPELLING_CHECK: True,  # default: True although slightly slow process but can Disabled
        PARALLELISATION_METHOD: DEFAULT_PARALLEL
    }

    default_params.update(params)

    print(f"final params: {default_params}")
    actions_mappings = [
        (GRANULAR, "Granular features", apply_granular_features),
        (HIGH_LEVEL, "High-level features", apply_high_level_features),
        (GRAMMAR_CHECK, "Grammar checks", apply_grammar_check),
        (SPELLING_CHECK, "Spelling checks", apply_spelling_check)
    ]

    for index, item in enumerate(actions_mappings.copy()):
        (param, _, _) = item
        if not default_params[param]:
            actions_mappings.remove(item)

    apply_profiling_progress_bar = get_progress_bar(actions_mappings)
    for _, (param, action_description, action_function) in \
            enumerate(apply_profiling_progress_bar):
        apply_profiling_progress_bar.set_description(action_description)
        action_function(
            action_description, new_dataframe,
            text_column, default_params[PARALLELISATION_METHOD]
        )

    return new_dataframe


def apply_granular_features(heading: str,
                            new_dataframe: pd.DataFrame,
                            text_column: dict,
                            parallelisation_method: str = DEFAULT_PARALLEL):
    granular_features_steps = [
        ('sentences_count', text_column, count_sentences),
        ('characters_count', text_column, count_chars),
        ('spaces_count', text_column, count_spaces),
        ('words_count', text_column, count_words),
        ('duplicates_count', text_column, count_duplicates),
        ('chars_excl_spaces_count', text_column, count_characters_excluding_spaces),
        ('emoji_count', text_column, count_emojis),
        ('whole_numbers_count', text_column, count_whole_numbers),
        ('alpha_numeric_count', text_column, count_alpha_numeric),
        ('non_alpha_numeric_count', text_column, count_non_alpha_numeric),
        ('punctuations_count', text_column, count_punctuations),
        ('stop_words_count', text_column, count_stop_words),
        ('dates_count', text_column, count_dates),
    ]
    generate_features(
        heading, granular_features_steps,
        new_dataframe, parallelisation_method
    )


def apply_high_level_features(heading: str,
                              new_dataframe: pd.DataFrame,
                              text_column: dict,
                              parallelisation_method: str = DEFAULT_PARALLEL):
    high_level_features_steps = [
        ('sentiment_polarity_score', text_column, sentiment_polarity_score),
        ('sentiment_polarity', 'sentiment_polarity_score', sentiment_polarity),
        ('sentiment_polarity_summarised', 'sentiment_polarity', sentiment_polarity_summarised),
        ('sentiment_subjectivity_score', text_column, sentiment_subjectivity_score),
        ('sentiment_subjectivity', 'sentiment_subjectivity_score', sentiment_subjectivity),
        ('sentiment_subjectivity_summarised', 'sentiment_subjectivity', sentiment_subjectivity_summarised),
    ]
    generate_features(
        heading, high_level_features_steps,
        new_dataframe, parallelisation_method
    )


def run_task(task_function, value: str):  # pragma: no cover
    # pragma: no cover => multiprocessing leads to loss of test coverage info
    cached_task_function = memory.cache(task_function)
    return cached_task_function(value)


def get_progress_bar(values: list) -> tqdm:
    cached_tqdm = memory.cache(tqdm)
    return cached_tqdm(values, ncols=PROGRESS_BAR_WIDTH)


def using_swifter(
        source_field, apply_function,
        source_column: str = None, new_column: str = None
) -> pd.DataFrame:
    return source_field \
        .swifter \
        .set_dask_scheduler(scheduler="processes") \
        .allow_dask_on_strings(enable=True) \
        .progress_bar(enable=True, desc=new_column) \
        .apply(apply_function, axis=1)


def using_joblib_parallel(
        source_field, apply_function,
        source_column: str, new_column: str,
) -> pd.DataFrame:
    source_values_to_transform = get_progress_bar(source_field.values)
    source_values_to_transform.set_description(new_column)

    result = Parallel(n_jobs=-1)(
        delayed(run_task)(
            apply_function, each_value
        ) for _, each_value in enumerate(source_values_to_transform)
    )
    source_values_to_transform.update()
    return result


def generate_features(main_header: str,
                      high_level_features_steps: list,
                      new_dataframe: pd.DataFrame,
                      parallelisation_method: str = DEFAULT_PARALLEL):
    generate_feature_progress_bar = get_progress_bar(high_level_features_steps)

    # Using swifter or Using joblib Parallel and delay method:
    parallelisation_method_function = using_joblib_parallel
    if parallelisation_method == SWIFTER:
        parallelisation_method_function = using_swifter

    for _, (new_column, source_column, transformation_function) in \
            enumerate(generate_feature_progress_bar):
        source_field = new_dataframe[source_column]
        generate_feature_progress_bar.set_description(
            f'{main_header}: {source_column} => {new_column}'
        )

        new_dataframe[new_column] = parallelisation_method_function(
            source_field, transformation_function,
            source_column, new_column
        )


def apply_spelling_check(heading: str,
                         new_dataframe: pd.DataFrame,
                         text_column: dict,
                         parallelisation_method: str = DEFAULT_PARALLEL):
    spelling_checks_steps = [
        ('spelling_quality_score', text_column, spelling_quality_score),
        ('spelling_quality', 'spelling_quality_score', spelling_quality),
        ('spelling_quality_summarised', 'spelling_quality', spelling_quality_summarised),
    ]
    generate_features(
        heading, spelling_checks_steps,
        new_dataframe, parallelisation_method
    )


def apply_grammar_check(heading: str,
                        new_dataframe: pd.DataFrame,
                        text_column: dict,
                        parallelisation_method: str = DEFAULT_PARALLEL):
    grammar_checks_steps = [
        ('grammar_check_score', text_column, grammar_check_score),
        ('grammar_check', 'grammar_check_score', grammar_quality),
    ]
    generate_features(
        heading, grammar_checks_steps,
        new_dataframe, parallelisation_method
    )
