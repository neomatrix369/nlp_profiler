import language_tool_python

language_tool = language_tool_python.LanguageTool('en-GB')
import pandas as pd
import math

from nlp_profiler.constants import NOT_APPLICABLE, NaN, DEFAULT_PARALLEL_METHOD, \
    GRAMMAR_CHECK_SCORE_COL, GRAMMAR_CHECK_COL
from nlp_profiler.generate_features import generate_features


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


### Grammar check: this is a very slow process
### take a lot of time per text it analysis
def grammar_check_score(text: str) -> int:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NaN

    matches = language_tool.check(text)
    return len(matches)


def grammar_quality(score: int) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    if score == 1:
        return "1 issue"
    elif score > 1:
        return f"{int(score)} issues"

    return "No issues"
