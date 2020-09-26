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
from joblib import Memory

from nlp_profiler.constants import GRAMMAR_CHECK_SCORE_COL, GRAMMAR_CHECK_COL
from nlp_profiler.constants import \
    PARALLELISATION_METHOD_OPTION, DEFAULT_PARALLEL_METHOD, GRANULAR_OPTION, HIGH_LEVEL_OPTION, \
    GRAMMAR_CHECK_OPTION, SPELLING_CHECK_OPTION
from nlp_profiler.constants import \
    SENTIMENT_POLARITY_SCORE_COL, SENTIMENT_POLARITY_COL, SENTIMENT_POLARITY_SUMMARISED_COL
from nlp_profiler.constants import \
    SENTIMENT_SUBJECTIVITY_COL, SENTIMENT_SUBJECTIVITY_SCORE_COL, SENTIMENT_SUBJECTIVITY_SUMMARISED_COL
from nlp_profiler.constants import \
    SPELLING_QUALITY_SCORE_COL, SPELLING_QUALITY_COL, SPELLING_QUALITY_SUMMARISED_COL
from nlp_profiler.generate_features import generate_features, get_progress_bar
from nlp_profiler.grammar_quality_check \
    import grammar_quality, grammar_check_score
from nlp_profiler.granular_features import apply_granular_features
from nlp_profiler.sentiment_polarity \
    import sentiment_polarity_score, sentiment_polarity, \
    sentiment_polarity_summarised
from nlp_profiler.sentiment_subjectivity \
    import sentiment_subjectivity_score, \
    sentiment_subjectivity_summarised, sentiment_subjectivity
from nlp_profiler.spelling_quality_check \
    import spelling_quality_score, spelling_quality, \
    spelling_quality_summarised

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
        HIGH_LEVEL_OPTION: True,
        GRANULAR_OPTION: True,
        GRAMMAR_CHECK_OPTION: False,  # default: False as slow process but can Enabled
        SPELLING_CHECK_OPTION: True,  # default: True although slightly slow process but can Disabled
        PARALLELISATION_METHOD_OPTION: DEFAULT_PARALLEL_METHOD
    }

    default_params.update(params)

    print(f"final params: {default_params}")
    actions_mappings = [
        (GRANULAR_OPTION, "Granular features", apply_granular_features),
        (HIGH_LEVEL_OPTION, "High-level features", apply_high_level_features),
        (GRAMMAR_CHECK_OPTION, "Grammar checks", apply_grammar_check),
        (SPELLING_CHECK_OPTION, "Spelling checks", apply_spelling_check)
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
            text_column, default_params[PARALLELISATION_METHOD_OPTION]
        )

    return new_dataframe


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


def apply_spelling_check(heading: str,
                         new_dataframe: pd.DataFrame,
                         text_column: dict,
                         parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    spelling_checks_steps = [
        (SPELLING_QUALITY_SCORE_COL, text_column, spelling_quality_score),
        (SPELLING_QUALITY_COL, SPELLING_QUALITY_SCORE_COL, spelling_quality),
        (SPELLING_QUALITY_SUMMARISED_COL, SPELLING_QUALITY_COL, spelling_quality_summarised),
    ]
    generate_features(
        heading, spelling_checks_steps,
        new_dataframe, parallelisation_method
    )


def apply_grammar_check(heading: str,
                        new_dataframe: pd.DataFrame,
                        text_column: dict,
                        parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    grammar_checks_steps = [
        (GRAMMAR_CHECK_SCORE_COL, text_column, grammar_check_score),
        (GRAMMAR_CHECK_COL, GRAMMAR_CHECK_SCORE_COL, grammar_quality),
    ]
    generate_features(
        heading, grammar_checks_steps,
        new_dataframe, parallelisation_method
    )
