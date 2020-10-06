import en_core_web_sm
import spacy
from nlp_profiler.constants import NaN
nlp = en_core_web_sm.load()


def gather_nouns(sent: str):

    if not isinstance(sent, str) or len(sent) == 0:
        return []
    
    doc = nlp(sent)
    return [(x.text, x.label_) for x in doc.ents]


def count_phase(text: str) -> int:
    print ("Text Type: ", type(text) )
    if not isinstance(text, str):
        return NaN

    return len(gather_nouns(text))