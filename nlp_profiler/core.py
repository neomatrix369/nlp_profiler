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
import string
from itertools import groupby
from tqdm import tqdm
import pandas as pd

import emoji
# Grammar Check
import language_tool_python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Sentiment Analysis
from textblob import TextBlob
from textblob import Word

nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

nltk.download('punkt')

NOT_APPLICABLE = "N/A"


def apply_text_profiling(dataframe: pd.DataFrame,
                         text_column: str,
                         params: dict = {}) -> pd.DataFrame:
    columns_to_drop = list(set(dataframe.columns) - set([text_column]))
    new_dataframe = dataframe.drop(columns=columns_to_drop, axis=1).copy()

    default_params = {
        'high_level': True,
        'granular': True,
        'grammar_check': False
    }

    default_params.update(params)

    print(f"final params: {default_params}")
    steps_mappings = [
        ("Applying Granular features", apply_granular_features),
        ("Generating High-level features", apply_high_level_features),
        ("Performing grammar checks", apply_grammar_check)
    ]

    first_level = tqdm(steps_mappings)
    for step_description, step in first_level:
        first_level.set_description(step_description)
        step(default_params, new_dataframe, text_column)

    return new_dataframe


def apply_granular_features(default_params: dict,
                            new_dataframe: pd.DataFrame,
                            text_column: dict):
    if default_params['granular']:
        granular_features_steps = [
            ('sentences_count', count_sentences),
            ('characters_count', len),
            ('spaces_count', count_spaces),
            ('words_count', words_count),
            ('duplicates_count', count_duplicates),
            ('chars_excl_spaces_count', count_characters_excluding_spaces),
            ('emoji_count', count_emojis),
            ('whole_numbers_count', count_whole_numbers),
            ('alpha_numeric_count', count_alpha_numeric),
            ('non_alpha_numeric_count', count_non_alpha_numeric),
            ('punctuations_count', count_punctuations),
            ('stop_words_count', count_stop_words),
            ('dates_count', count_dates),
        ]
        source_field = new_dataframe[text_column]
        second_level = tqdm(granular_features_steps)
        for (new_column, transformation) in second_level:
            second_level.set_description(f'Generating {new_column} using {text_column}')
            new_dataframe[new_column] = source_field.apply(transformation)


def apply_high_level_features(default_params: dict,
                              new_dataframe: pd.DataFrame,
                              text_column: dict):
    if default_params['high_level']:
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
        second_level = tqdm(high_level_features_steps)
        for (new_column, source_column, transformation) in second_level:
            source_field = new_dataframe[source_column]
            second_level.set_description(f'Generating {new_column} using {source_column}')
            new_dataframe[new_column] = source_field.apply(transformation)


def apply_grammar_check(default_params: dict,
                        new_dataframe: pd.DataFrame,
                        text_column: dict):
    if default_params['grammar_check']:
        grammar_checks_steps = [
            ('grammar_check_score', text_column, grammar_check_score),
            ('grammar_check', 'grammar_check_score', grammar_quality),
        ]
        second_level = tqdm(grammar_checks_steps)
        for (new_column, source_column, transformation) in second_level:
            source_field = new_dataframe[source_column]
            second_level.set_description(f'Generating {new_column} using {source_column}')
            new_dataframe[new_column] = source_field.apply(transformation)


### Sentiment analysis

def sentiment_polarity_summarised(polarity: str) -> str:
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
    for each_slab in sentiment_polarity_to_words_mapping:  # pragma: no cover
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_polarity_score(text: str) -> float:
    if (not text) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    return TextBlob(text).sentiment.polarity


### Sentiment Subjectivity

def sentiment_subjectivity_summarised(sentiment_subjectivity: str) -> str:
    if '/' in sentiment_subjectivity:
        return sentiment_subjectivity
    elif 'subjective' in sentiment_subjectivity.lower():
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

    for each_slab in sentiment_subjectivity_to_words_mapping:  # pragma: no cover
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


def sentiment_subjectivity_score(text: str) -> float:
    if (not text) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    return TextBlob(text).sentiment.subjectivity


### Spell check
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
spelling_quality_score_to_words_mapping = [
    ["Very good", 99, 100],  # Very good: Certain: 100%: Give or take 0%
    ["Quite good", 90, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Good", 87, 90],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Pretty good", 63, 87],  # Pretty: Good: Probable: 75%: Give or take about 12%
    ["Bad", 40, 63],  # So/so: Chances About Even: 50%: Give or take about 10%
    ["Pretty bad", 12, 40],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    ["Quite bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
    ["Very bad", 0, 2]  # Impossible 0%: Give or take 0%
]


def spelling_quality_summarised(spelling_quality: str) -> str:
    if 'good' in spelling_quality.lower():
        return 'Good'

    return 'Bad'


def spelling_quality_score(text: str) -> float:
    if (not text) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    tokenized_text = word_tokenize(text.lower())

    misspelt_words_count = 0
    total_words_checks = 0
    for each_word in tokenized_text:
        if each_word not in string.punctuation:
            spellchecked_word = Word(each_word).spellcheck()
            _, score = spellchecked_word[0]
            if score != 1:
                misspelt_words_count += 1
            total_words_checks += 1
    num_of_sentences = count_sentences(text)
    avg_words_per_sentence = \
        total_words_checks / num_of_sentences
    result = (avg_words_per_sentence - \
              misspelt_words_count) / avg_words_per_sentence
    return result if result >= 0.0 else 0.0


def spelling_quality(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    score = float(score) * 100
    for each_slab in spelling_quality_score_to_words_mapping:  # pragma: no cover
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]


### Grammar check: this is a very slow process
### take a lot of time per text it analysis

def grammar_check_score(text: str) -> int:
    tool = language_tool_python.LanguageTool('en-GB')
    matches = tool.check(text)
    return len(matches)


def grammar_quality(score: float) -> str:
    if score == 1:
        return "1 issue"
    elif score > 1:
        return f"{score} issues"

    return "No issues"


### Emojis

def gather_emojis(text: str) -> list:
    emoji_expaned_text = emoji.demojize(text)
    return re.findall(r'\:(.*?)\:', emoji_expaned_text)


def count_emojis(text: str) -> int:
    list_of_emojis = gather_emojis(text)
    return len(list_of_emojis)


### Numbers
def gather_whole_numbers(text: str) -> list:
    line = re.findall(r'[0-9]+', text)
    return line


def count_whole_numbers(text: str) -> int:
    list_of_numbers = gather_whole_numbers(text)
    return len(list_of_numbers)


### Alphanumeric
def gather_alpha_numeric(text: str) -> list:
    return re.findall('[A-Za-z0-9]', text)


def count_alpha_numeric(text: str) -> int:
    return len(gather_alpha_numeric(text))


### Non-alphanumeric
def gather_non_alpha_numeric(text: str) -> list:
    return re.findall('[^A-Za-z0-9]', text)


def count_non_alpha_numeric(text: str) -> int:
    return len(gather_non_alpha_numeric(text))


### Punctuations
def gather_punctuations(text: str) -> list:
    line = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string = "".join(line)
    return list(string)


def count_punctuations(text: str) -> int:
    return len(gather_punctuations(text))


### Stop words
def gather_stop_words(text: str) -> list:
    word_tokens = word_tokenize(text)
    found_stop_words = [word for word in word_tokens
                        if word in STOP_WORDS]
    return found_stop_words


def count_stop_words(text: str) -> int:
    return len(gather_stop_words(text))


### Dates
def gather_dates(text: str, date_format: str = 'dd/mm/yyyy') -> list:
    ddmmyyyy = r'\b(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/([0-9]{4})\b'
    mmddyyyy = r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b'
    regex_list = {
        'dd/mm/yyyy': ddmmyyyy, 'mm/dd/yyyy': mmddyyyy
    }
    return re.findall(regex_list[date_format], text)


def count_dates(text: str) -> int:
    return len(gather_dates(text))


### Words count
def gather_words(text: str) -> list:
    return re.findall(r'\b[^\d\W]+\b', text)


def words_count(text: str) -> int:
    return len(gather_words(text))


### Sentences
def gather_sentences(text: str) -> list:
    lines = re.findall(r'([^.]*[^.]*)', text)
    for index, each in enumerate(lines):
        if each == '':
            del lines[index]

    return lines


### Number of spaces
def count_spaces(text: str) -> int:
    spaces = re.findall(r' ', text)
    return len(spaces)


### Number of characters without spaces
def gather_duplicates(text: str) -> dict:
    tokenized_text = word_tokenize(text.lower())
    sorted_tokenized_text = sorted(tokenized_text)
    duplicates = {}
    for value, group in groupby(sorted_tokenized_text):
        frequency = len(list(group))
        if frequency > 1:
            duplicates.update({value: frequency})

    return duplicates


### Duplicates
def count_duplicates(text: str) -> int:
    return len(gather_duplicates(text))


def count_characters_excluding_spaces(text: str) -> int:
    return len(text) - count_spaces(text)


def count_sentences(text: str) -> int:
    return len(gather_sentences(text))
