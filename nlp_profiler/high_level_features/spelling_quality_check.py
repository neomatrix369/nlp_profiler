import math
import tempfile

import pandas as pd
from joblib import Memory

#alternative for textblob spell checker
from symspellpy import SymSpell, Verbosity
import pkg_resources

# load a dictionary (this one consists of 82,765 English words)
#there are other dictionaries as well look at https://www.kaggle.com/code/muhammetfaik/spellcheckingbenchmark
#link to the used frequency dictionary https://raw.githubusercontent.com/wolfgarbe/SymSpell/master/SymSpell/frequency_dictionary_en_82_765.txt
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
# term_index: column of the term 
# count_index: column of the term's frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

#importing fuzzy matching for scoring purposes
from fuzzywuzzy import fuzz,process

from nlp_profiler.constants import \
    DEFAULT_PARALLEL_METHOD
from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.constants import \
    SPELLING_QUALITY_SCORE_COL, SPELLING_QUALITY_COL, SPELLING_QUALITY_SUMMARISED_COL
from nlp_profiler.generate_features import generate_features

memory = Memory(tempfile.gettempdir(), compress=9, verbose=0)


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


### Spell check
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
### The General Area of Possibility
spelling_quality_score_to_words_mapping = [
    ["Very good", 99, 100],  # Very good: Certain: 100%: Give or take 0%
    ["Quite good", 97, 99],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Good", 95, 97],  # Quite Good: Almost Certain: 93%: Give or take 6%
    ["Pretty good", 90, 95],  # Pretty: Good: Probable: 75%: Give or take about 12%
    ["Bad", 60, 90],  # So/so: Chances About Even: 50%: Give or take about 10%
    ["Pretty bad", 12, 60],  # Pretty bad: Probably Not: 30%: Give or take about 10%
    ["Quite bad", 2, 12],  # Quite bad: Almost Certainly Not 7%: Give or take about 5%
    ["Very bad", 0, 2]  # Impossible 0%: Give or take 0%
]

##additional function for spelling check and alternative building. Here the chekcs take punctuations into account as well.
##For instance,"badrestaurant" is converted to "bad restaurant" and the score is affected due to the same 
def symspell_corrector(input_term: str) -> str:
  # look up suggestions for multi-word input strings 
    suggestions = sym_spell.lookup_compound( 
        phrase=input_term,  
        max_edit_distance=2,  
        transfer_casing=True,  
        ignore_term_with_digits=True, 
        ignore_non_words=True, 
        split_by_space=True 
    ) 
    # display the correction
    for suggestion in suggestions: 
      if suggestion.term:
        return suggestion.term
    return input_term

def spelling_quality_summarised(quality: str) -> str:
    if (not quality) or (quality == NOT_APPLICABLE):
        return NOT_APPLICABLE

    if 'good' in quality.lower():
        return 'Good'

    return 'Bad'


def spelling_quality_score(text: str) -> float:
    result=0.0
    if not isinstance(text, str) or len(text.strip()) == 0:
        return NaN

    corrected_text = symspell_corrector(text) 
    if corrected_text is not None:
      result = fuzz.token_sort_ratio(corrected_text,text)/100

    return result if result >= 0.0 else 0.0


@memory.cache
def spelling_quality(score: float) -> str:
    if math.isnan(score):
        return NOT_APPLICABLE

    score = float(score) * 100
    for _, each_slab in enumerate(spelling_quality_score_to_words_mapping):  # pragma: no cover
        # pragma: no cover => early termination leads to loss of test coverage info
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]
