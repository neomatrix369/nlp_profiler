from textstat import flesch_reading_ease
import pandas as pd
import math

from nlp_profiler.constants import NOT_APPLICABLE, NaN, DEFAULT_PARALLEL_METHOD, \
    EASE_OF_READING_SCORE_COL, EASE_OF_READING_COL
from nlp_profiler.generate_features import generate_features


def apply_ease_of_reading_check(heading: str,
                        new_dataframe: pd.DataFrame,
                        text_column: dict,
                        parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    ease_of_reading_steps = [
        (EASE_OF_READING_SCORE_COL, text_column, EASE_OF_READING_SCORE),
        (EASE_OF_READING_COL, EASE_OF_READING_SCORE_COL, ease_of_reading),
        (EASE_OF_READING_SUMMARISED_COL, EASE_OF_READING_COL, ease_of_reading_summarised),
    ]
    generate_features(
        heading, ease_of_reading_steps,
        new_dataframe, parallelisation_method
    )

ease_of_reading_to_summarised_words_mapping = {
    "Very Easy": "Easy",
    "Easy": "Easy",
    "Fairly Easy": "Easy",
    "Standard": "Standard",
    "Fairly Difficult": "Difficult",
    "Difficult": "Difficult" ,
    "Very Confusing": "Confusing" 
}
def ease_of_reading_summarised(text: str) -> str:
    if text in ease_of_reading_to_summarised_words_mapping:        
        return ease_of_reading_to_summarised_words_mapping[text]
    return "N/A"


def ease_of_reading_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    return float(flesch_reading_ease(text))

# Docs: https://textblob.readthedocs.io/en/dev/quickstart.html
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
ease_of_reading_to_words_mapping = [
    ["Very Easy", 90, 100],  
    ["Easy", 80, 89],  
    ["Fairly Easy", 70, 79], 
    ["Standard", 60, 69],  
    ["Fairly Difficult", 50, 59],  
    ["Difficult", 30, 49],
    ["Very Confusing", 0, 29]
]
def ease_of_reading(score: int) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    if math.isnan(score):
        return NOT_APPLICABLE

    score = float(score)
    for _, each_slab in enumerate(ease_of_reading_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if ((score <= 0) and (each_slab[1] == 0)) or \
           ((score >= 100) and (each_slab[2] == 100)):
            return each_slab[0]
        elif (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]