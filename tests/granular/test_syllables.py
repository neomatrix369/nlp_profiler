import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.syllables import count_syllables  # noqa

text_with_english_chars1 = "2833047 people live in this area"
text_with_english_chars2 = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."

english_text_to_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_english_chars1, 7),
    (text_with_english_chars2, 18),
]


@pytest.mark.parametrize("text,expected_result", english_text_to_count_mapping)
def test_given_a_text_when_counted_for_syllables_then_return_NaN_or_count_of_syllables(
    text: str, expected_result: float
):
    # given, when
    actual_result = count_syllables(text)

    # then
    assert expected_result is actual_result, "Didn't find the expected number of syllables in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"


text_with_non_english_chars1 = "©2833047 people live in this area"
text_with_non_english_chars2 = "«This sentence doesn't seem to too many commas, periods or semi-colons."
text_with_non_english_chars3 = "¦2833047   \t\tpeople live in th\ris area"
text_with_non_english_chars4 = "½¼¢2833047   \t\tpeople live in th\ris area"
text_with_non_english_chars5 = "¬2833047   people\r\r     live in th\tis area"
text_with_non_english_chars6 = "®2833047 people live in th\nis area "
text_with_non_english_chars7 = "2833047   people\n\n   live in   th\nis area "
text_with_japanese_kana_chars = "This sentence is in japanese (kana) ろぬふうえおやゆゆわほへへて"
text_with_japanese_kana_compact_chars = "This sentence is in japanese (kana compact) おっあこおおがおんわお"
text_without_japanese_kana_chars = "This sentence is in japanese (kana)"
text_with_arabic_chars = "فصصصشببلااتنخمككك This sentence is in arabic"
text_without_arabic_chars = "This sentence is in arabic"

non_english_text_to_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_non_english_chars1, 7),
    (text_with_non_english_chars2, 17),
    (text_with_non_english_chars3, 8),
    (text_with_non_english_chars4, 8),
    (text_with_non_english_chars5, 8),
    (text_with_non_english_chars6, 8),
    (text_with_non_english_chars7, 8),
    (text_with_japanese_kana_chars, 10),
    # why is syllable count for text without japanese (kana) characters
    # NOT the same as with japanese (kana) characters?
    (text_without_japanese_kana_chars, 9),
    (text_with_japanese_kana_compact_chars, 12),
    (text_with_arabic_chars, 8),
    # why is syllable count for text without arabic characters
    # NOT the same as with arabic characters?
    (text_without_arabic_chars, 7),
]


@pytest.mark.parametrize("text,expected_result", non_english_text_to_count_mapping)
def test_given_a_text_with_non_english_chars_when_counted_for_syllables_then_return_NaN_or_count_of_syllables(
    text: str, expected_result: float
):
    # given, when
    actual_result = count_syllables(text)

    # then
    assert expected_result is actual_result, "Didn't find the expected number of syllables in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"
