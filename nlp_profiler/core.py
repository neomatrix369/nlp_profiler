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

import re
import tempfile
from itertools import groupby

import emoji
import joblib
# Grammar Check
import language_tool_python
import nltk
import pandas as pd
from joblib import Parallel, delayed
from nltk.corpus import stopwords
# NLP
from nltk.tokenize import word_tokenize
# Sentiment Analysis
from textblob import TextBlob
from tqdm.auto import tqdm
import swifter  # noqa

from nlp_profiler.constants import \
    NOT_APPLICABLE, PARALLELISATION_METHOD, DEFAULT_PARALLEL, SWIFTER, \
    GRANULAR, HIGH_LEVEL, GRAMMAR_CHECK
from nlp_profiler.sentences import count_sentences
from nlp_profiler.spelling_quality_check \
    import spelling_quality_score, spelling_quality, spelling_quality_summarised

nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

nltk.download('punkt')

memory = joblib.Memory(tempfile.gettempdir(), compress=9, verbose=0)


def is_running_from_ipython():
    from IPython import get_ipython
    return get_ipython() is not None


PROGRESS_BAR_WIDTH = 900 if is_running_from_ipython() else None


def apply_text_profiling(dataframe: pd.DataFrame,
                         text_column: str,
                         params: dict = {}) -> pd.DataFrame:
    columns_to_drop = list(set(dataframe.columns) - set([text_column]))
    new_dataframe = dataframe.drop(columns=columns_to_drop, axis=1).copy()

    default_params = {
        HIGH_LEVEL: True,
        GRANULAR: True,
        GRAMMAR_CHECK: False,
        PARALLELISATION_METHOD: DEFAULT_PARALLEL
    }

    default_params.update(params)

    print(f"final params: {default_params}")
    actions_mappings = [
        (GRANULAR, "Granular features", apply_granular_features),
        (HIGH_LEVEL, "High-level features", apply_high_level_features),
        (GRAMMAR_CHECK, "Grammar checks", apply_grammar_check)
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
        ('spelling_quality_score', text_column, spelling_quality_score),
        ('spelling_quality', 'spelling_quality_score', spelling_quality),
        ('spelling_quality_summarised', 'spelling_quality', spelling_quality_summarised),

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
    return source_field.swifter.apply(apply_function, axis=1)


def using_joblib_parallel(
        source_field, apply_function,
        source_column: str, new_column: str,
) -> pd.DataFrame:
    source_values_to_transform = get_progress_bar(source_field.values)
    source_values_to_transform.set_description(
        f'Applying {source_column} => {new_column}'
    )

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


### Sentiment analysis

def sentiment_polarity_summarised(polarity: str) -> str:
    if polarity == NOT_APPLICABLE:
        return NOT_APPLICABLE

    if 'negative' in polarity.lower():
        return 'Negative'
    if 'positive' in polarity.lower():
        return 'Positive'

    return polarity


# Docs: https://textblob.readthedocs.io/en/dev/quickstart.html
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
sentiment_polarity_to_words_mapping = [
    ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    ["Quite positive", 87, 99],  # Almost Certain: 93%: Give or take 6%
    ["Pretty positive", 51, 87],  # Probable: 75%: Give or take about 12%
    ["Neutral", 49, 51],  # Chances About Even: 50%: Give or take about 10%
    ["Pretty negative", 12, 49],  # Probably Not: 30%: Give or take about 10%
    ["Quite negative", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
]


def sentiment_polarity(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    score = float(score)
    score = (score + 1) / 2  # see https://stats.stackexchange.com/questions/70801/how-to-normalize-data-to-0-1-range
    score = score * 100
    for _, each_slab in enumerate(sentiment_polarity_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_polarity_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    return TextBlob(text).sentiment.polarity


### Sentiment Subjectivity

def sentiment_subjectivity_summarised(subjectivity: str) -> str:
    if subjectivity == NOT_APPLICABLE:
        return NOT_APPLICABLE

    if '/' in subjectivity:
        return subjectivity
    elif 'subjective' in subjectivity.lower():
        return 'Subjective'

    return 'Objective'


### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
sentiment_subjectivity_to_words_mapping = [
    ["Very subjective", 99, 100],  # Certain: 100%: Give or take 0%
    ["Quite subjective", 87, 99],  # Almost Certain: 93%: Give or take 6%
    ["Pretty subjective", 63, 87],  # Probable: 75%: Give or take about 12%
    ["Objective/subjective", 40, 63],  # Chances About Even: 50%: Give or take about 10%
    ["Pretty objective", 12, 40],  # Probably Not: 30%: Give or take about 10%
    ["Quite objective", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    ["Very objective", 0, 2]  # Impossible 0%: Give or take 0%
]


def sentiment_subjectivity(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    score = float(score) * 100

    for _, each_slab in enumerate(sentiment_subjectivity_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_subjectivity_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    return TextBlob(text).sentiment.subjectivity


### Grammar check: this is a very slow process
### take a lot of time per text it analysis
def grammar_check_score(text: str) -> int:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    tool = language_tool_python.LanguageTool('en-GB')
    matches = tool.check(text)
    return len(matches)


def grammar_quality(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    if score == 1:
        return "1 issue"
    elif score > 1:
        return f"{score} issues"

    return "No issues"


### Emojis

def gather_emojis(text: str) -> list:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return []

    emoji_expaned_text = emoji.demojize(text)
    return re.findall(r'\:(.*?)\:', emoji_expaned_text)


def count_emojis(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    list_of_emojis = gather_emojis(text)
    return len(list_of_emojis)


### Numbers
def gather_whole_numbers(text: str) -> list:
    if not isinstance(text, str):
        return []

    line = re.findall(r'[0-9]+', text)
    return line


def count_whole_numbers(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_whole_numbers(text))


### Alphanumeric
def gather_alpha_numeric(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall('[A-Za-z0-9]', text)


def count_alpha_numeric(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_alpha_numeric(text))


### Non-alphanumeric
def gather_non_alpha_numeric(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall('[^A-Za-z0-9]', text)


def count_non_alpha_numeric(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_non_alpha_numeric(text))


### Punctuations
def gather_punctuations(text: str) -> list:
    if not isinstance(text, str):
        return []

    line = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string = "".join(line)
    return list(string)


def count_punctuations(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_punctuations(text))


### Stop words
def gather_stop_words(text: str) -> list:
    if not isinstance(text, str):
        return []

    word_tokens = word_tokenize(text)
    found_stop_words = [word for _, word in enumerate(word_tokens)
                        if word in STOP_WORDS]
    return found_stop_words


def count_stop_words(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_stop_words(text))


### Dates
def gather_dates(text: str, date_format: str = 'dd/mm/yyyy') -> list:
    if not isinstance(text, str):
        return []

    ddmmyyyy = r'\b(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/([0-9]{4})\b'
    mmddyyyy = r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b'
    regex_list = {
        'dd/mm/yyyy': ddmmyyyy, 'mm/dd/yyyy': mmddyyyy
    }
    return re.findall(regex_list[date_format], text)


def count_dates(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_dates(text))


### Words count
def gather_words(text: str) -> list:
    if not isinstance(text, str):
        return []

    return re.findall(r'\b[^\d\W]+\b', text)


def count_words(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE
    return len(gather_words(text))


### Number of spaces
def count_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    spaces = re.findall(r' ', text)
    return len(spaces)


### Number of characters without spaces
def gather_duplicates(text: str) -> dict:
    if not isinstance(text, str):
        return []

    tokenized_text = word_tokenize(text.lower())
    sorted_tokenized_text = sorted(tokenized_text)
    duplicates = {}
    for _, (value, group) in enumerate(groupby(sorted_tokenized_text)):
        frequency = len(list(group))
        if frequency > 1:
            duplicates.update({value: frequency})

    return duplicates


### Duplicates
def count_duplicates(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(gather_duplicates(text))


def count_characters_excluding_spaces(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(text) - count_spaces(text)


def count_chars(text: str) -> int:
    if not isinstance(text, str):
        return NOT_APPLICABLE

    return len(text)
