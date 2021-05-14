from nlp_profiler.constants import NaN
import textstat


# Credits: Gunes Evitan (https://www.kaggle.com/gunesevitan)
#     -- inspired by the discussion on https://www.kaggle.com/c/commonlitreadabilityprize/discussion/238375
def count_syllables(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return textstat.syllable_count(text)
