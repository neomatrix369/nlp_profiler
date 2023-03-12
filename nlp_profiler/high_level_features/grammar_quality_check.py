# changing the grammar checker from language tool to gingerit for better results
from gingerit.gingerit import GingerIt

parser = GingerIt()
import pandas as pd
import math

from nlp_profiler.constants import (
    NOT_APPLICABLE,
    NaN,
    DEFAULT_PARALLEL_METHOD,
    GRAMMAR_CHECK_SCORE_COL,
    GRAMMAR_CHECK_COL,
)
from nlp_profiler.generate_features import generate_features


def apply_grammar_check(
    heading: str, new_dataframe: pd.DataFrame, text_column: dict, parallelisation_method: str = DEFAULT_PARALLEL_METHOD
):
    grammar_checks_steps = [
        (GRAMMAR_CHECK_SCORE_COL, text_column, grammar_check_score),
        (GRAMMAR_CHECK_COL, GRAMMAR_CHECK_SCORE_COL, grammar_quality),
    ]
    generate_features(heading, grammar_checks_steps, new_dataframe, parallelisation_method)


### Grammar check: this is a very slow process
### take a lot of time per text it analysis
def grammar_check_score(text: str) -> int:
    if not (isinstance(text, str) or text.strip()):
        return NaN
    # calling the parser function to parse through the text for errors
    matches = parser.parse(text)
    # the corrections is an array of dictionaries containing the position and the word that has been changed
    return len(matches["corrections"])


def grammar_quality(score: int) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    if score == 1:
        return "1 issue"
    elif score > 1:
        return f"{score} issues"

    return "No issues"
