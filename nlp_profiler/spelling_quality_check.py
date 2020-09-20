import string

from nltk.tokenize import word_tokenize
from textblob import Word

from nlp_profiler.constants import NOT_APPLICABLE
from nlp_profiler.sentences import count_sentences

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

    tokenized_text = word_tokenize(text.lower())

    misspelt_words_count = 0
    total_words_checks = 0
    for each_word in tokenized_text:
        if each_word not in string.punctuation:
            misspelt_words_count, total_words_checks = \
                actual_spell_check(each_word, misspelt_words_count,
                                   total_words_checks)
    num_of_sentences = count_sentences(text)
    avg_words_per_sentence = total_words_checks / num_of_sentences
    result = (avg_words_per_sentence - misspelt_words_count) \
             / avg_words_per_sentence

    return result if result >= 0.0 else 0.0


def actual_spell_check(each_word, misspelt_words_count, total_words_checks):
    spellchecked_word = Word(each_word).spellcheck()
    _, score = spellchecked_word[0]
    if score != 1:
        misspelt_words_count += 1
    total_words_checks += 1
    return misspelt_words_count, total_words_checks


def spelling_quality(score: float) -> str:
    if score == NOT_APPLICABLE:
        return NOT_APPLICABLE

    score = float(score) * 100
    for each_slab in spelling_quality_score_to_words_mapping:  # pragma: no cover
        if (score >= each_slab[1]) and (score <= each_slab[2]):
            return each_slab[0]
