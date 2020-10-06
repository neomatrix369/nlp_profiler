import en_core_web_sm
from nlp_profiler.constants import NaN
nlp = en_core_web_sm.load()


def gather_nouns(sentence: str):

    if not isinstance(sentence, str) or len(sentence) == 0:
        return []
    
    doc = nlp(sentence)
    return [(x.text, x.label_) for x in doc.ents]


def count_noun_phase(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_nouns(text))