import re

import emoji
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

from nlp_profiler.constants import NaN

nltk.download('averaged_perceptron_tagger')


def gather_nouns(sentence: str):
    if not isinstance(sentence, str) or len(sentence) == 0:
        return []
    emoji_decoded = emoji.demojize(sentence, delimiters=("", "")).lower().strip()  # Decoding Emoji's
    # import pdb; pdb.set_trace();
    token = word_tokenize(emoji_decoded)
    tags = list(
        filter(lambda x: re.match(r"(JJ|NN|NNP)", x[1]), pos_tag(token)))  # using RegEx to to check for Noun Phases.
    return tags


def count_noun_phase(text: str):
    if not isinstance(text, str):
        return NaN

    return len(gather_nouns(text))
