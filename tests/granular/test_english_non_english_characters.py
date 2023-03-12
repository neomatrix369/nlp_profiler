import string as string_module

import numpy as np
import pytest

from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.english_non_english_chars import (
    count_english_chars,
    count_non_english_chars,
    NON_STANDARD_ASCII_CHARS,
)  # noqa

text_with_english_chars1 = "2833047 people live in this area"
text_with_english_chars2 = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
text_with_english_chars3 = "2833047   \t\tpeople live in th\ris area"
text_with_english_chars4 = "2833047   \t\tpeople live in th\ris area"
text_with_english_chars5 = "2833047   people\r\r     live in th\tis area"
text_with_english_chars6 = "2833047 people live in th\nis area " + string_module.whitespace
text_with_english_chars7 = "2833047   people\n\n   live in   th\nis area " + string_module.punctuation

english_text_to_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_english_chars1, 32),
    (text_with_english_chars2, 74),
    (text_with_english_chars3, 37),
    (text_with_english_chars4, 37),
    (text_with_english_chars5, 41),
    (text_with_english_chars6, 40),
    (text_with_english_chars7, 73),
]


@pytest.mark.parametrize("text,expected_result", english_text_to_count_mapping)
def test_given_a_text_when_counted_for_English_chars_then_return_NaN_or_count_of_chars(
    text: str, expected_result: float
):
    # given, when
    actual_result = count_english_chars(text)

    # then
    assert expected_result is actual_result, "Didn't find the expected number of English characters in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"


text_with_non_english_chars1 = "©2833047 people live in this area" + NON_STANDARD_ASCII_CHARS[0:10]
text_with_non_english_chars2 = (
    "«This sentence doesn't seem to too many commas, periods or semi-colons (;)." + NON_STANDARD_ASCII_CHARS[11:20]
)
text_with_non_english_chars3 = "¦2833047   \t\tpeople live in th\ris area" + NON_STANDARD_ASCII_CHARS[21:30]
text_with_non_english_chars4 = "½¼¢2833047   \t\tpeople live in th\ris area" + NON_STANDARD_ASCII_CHARS[31:40]
text_with_non_english_chars5 = "¬2833047   people\r\r     live in th\tis area" + NON_STANDARD_ASCII_CHARS[41:50]
text_with_non_english_chars6 = (
    "®2833047 people live in th\nis area " + string_module.whitespace + NON_STANDARD_ASCII_CHARS[41:50]
)
text_with_non_english_chars7 = (
    NON_STANDARD_ASCII_CHARS[51:] + "2833047   people\n\n   live in   th\nis area " + string_module.punctuation
)
text_with_japanese_kana_chars = "This sentence is in japanese (kana) ろぬふうえおやゆゆわほへへて"
text_with_japanese_kana_compact_chars = "This sentence is in japanese (kana compact) おっあこおおがおんわお"
text_with_arabic_chars = "فصصصشببلااتنخمككك This sentence is in arabic"

non_english_text_to_count_mapping = [
    (np.nan, NaN),
    (float("nan"), NaN),
    (None, NaN),
    (text_with_non_english_chars1, 11),
    (text_with_non_english_chars2, 10),
    (text_with_non_english_chars3, 10),
    (text_with_non_english_chars4, 12),
    (text_with_non_english_chars5, 10),
    (text_with_non_english_chars6, 10),
    (text_with_non_english_chars7, 63),
    (text_with_japanese_kana_chars, 14),
    (text_with_japanese_kana_compact_chars, 11),
    (text_with_arabic_chars, 17),
]


@pytest.mark.parametrize("text,expected_result", non_english_text_to_count_mapping)
def test_given_a_text_when_counted_for_non_english_chars_then_return_NaN_or_count_of_chars(
    text: str, expected_result: float
):
    # given, when
    actual_result = count_non_english_chars(text)

    # then
    assert expected_result is actual_result, "Didn't find the expected number of English characters in the text"
    f"Expected: {expected_result}, Actual: {actual_result}"
