import string
import tempfile

from joblib import Memory
from nltk.tokenize import word_tokenize
from textblob import Word

from nlp_profiler.constants import NOT_APPLICABLE
from nlp_profiler.sentences import count_sentences

memory = Memory(tempfile.gettempdir(), compress=9, verbose=0)

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


def spelling_quality_summarised(quality: str) -> str:
    if quality == NOT_APPLICABLE:
        return NOT_APPLICABLE

    if 'good' in quality.lower():
        return 'Good'

    return 'Bad'


def spelling_quality_score(text: str) -> float:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return NOT_APPLICABLE

    tokenized_text = get_tokenized_text(text)

    tokenized_text = [
        token for token in tokenized_text if token not in string.punctuation
    ]
    total_words_checks = len(tokenized_text)
    misspelt_words = [
        each_word for each_word in tokenized_text
        if actual_spell_check(each_word) is not None
    ]
    misspelt_words_count = len(misspelt_words)

    num_of_sentences = get_sentence_count(text)
    avg_words_per_sentence = total_words_checks / num_of_sentences
    result = (avg_words_per_sentence - misspelt_words_count) \
             / avg_words_per_sentence

    return result if result >= 0.0 else 0.0


@memory.cache
def get_sentence_count(text: str) -> int:
    return count_sentences(text)


@memory.cache
def get_tokenized_text(text: str) -> list:
    return word_tokenize(text.lower())


@memory.cache
def actual_spell_check(each_word: str) -> str:
    spellchecked_word = Word(each_word).spellcheck()
    _, score = spellchecked_word[0]
    return each_word if score != 1 else None


def spelling_quality(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    score = float(score) * 100
    for each_slab in spelling_quality_score_to_words_mapping:  # pragma: no cover
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]
