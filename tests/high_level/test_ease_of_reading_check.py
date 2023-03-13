import numpy as np
import pytest

from nlp_profiler.constants import NaN, NOT_APPLICABLE
from nlp_profiler.high_level_features.ease_of_reading_check import (
    ease_of_reading_score,
    ease_of_reading,
    ease_of_reading_summarised,
)  # noqa

# textstat.flesch_reading_ease() returned a score of -133.6 (previously -175.9)
very_confusing_text1 = '...asasdasdasdasdasd  djas;ODLaskjdf.'

# textstat.flesch_reading_ease() returned a score of -24.64 (previously -50.02)
very_confusing_text2 = '. a323# asdft asdlkassdsdsd'

# textstat.flesch_reading_ease() returned a score of 53.88
fairly_difficult = (
    "Everyone here is so hardworking. Hardworking people. "
    "I think hardworking people are a good trait in our company."
)

# textstat.flesch_reading_ease() returned a score of 36.62
difficult_text = "asfl;a089v"

# textstat.flesch_reading_ease() returned a score of 57.27
fairly_difficult_latin_text = (
    "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
)

# textstat.flesch_reading_ease() returned a score of 66.4
standard_text = "Python is a programming language."

# textstat.flesch_reading_ease() returned a score of 84.34 (previously 80.28)
easy_text = 'يح going to.. asfl;as ๑۞๑ asdlkas Kadv as'

# textstat.flesch_reading_ease() returned a score of 75.88
fairly_easy_text = "Im going to.. asfl;a089v"

# textstat.flesch_reading_ease() returned a score of 119.19
very_easy_arabic_text = "لوحة المفاتيح العربية"

# textstat.flesch_reading_ease() returned a score of 114.12
very_easy_emoji_text = "๑۞๑,¸¸,ø¤º°`°๑۩ ℍ𝑒ˡ𝔩σ ϻⓨ ⓝα𝕞𝕖 ί𝔰 α𝓀ί𝓿𝕒𝕤𝔥𝓐 ๑۩ ,¸¸,ø¤º°`°๑۞๑"

# textstat.flesch_reading_ease() returned a score of 120.21
very_easy_unicode_text = "乇乂丅尺卂 丅卄工匚匚"

# textstat.flesch_reading_ease() returned a score of 99.23 (previously 89.xx)
text_with_punctuations = '283047 people live [[[ ]]] in this area[[[ ]]] :::;;;;££'

text_with_non_english_chars = (
    "2833047 pe\nople li\tve i\rn this area"
    '‚ƒ„…†‡ˆ‰Š‹ŒŽ•™š›œžŸ¡¢¤¥¦¨©ª«¬­®¯°²³´"'
    "µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
    "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    "This sentence is in japanese (kana) ろぬふうえおやゆゆわほへへて"
    "This sentence is in japanese (kana compact) おっあこおおがおんわお"
    "فصصصشببلااتنخمككك This sentence is in arabic"
)

text_to_return_value_mapping = [
    (np.nan, NaN, NOT_APPLICABLE),
    (float("nan"), NaN, NOT_APPLICABLE),
    (None, NaN, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE),
    (very_confusing_text1, -133.6, 'Very Confusing'),
    (very_confusing_text2, -24.64, 'Very Confusing'),
    (difficult_text, 36.62, 'Difficult'),
    (fairly_difficult_latin_text, 57.27, "Fairly Difficult"),
    (fairly_difficult, 53.88, "Fairly Difficult"),
    (standard_text, 66.40, "Standard"),
    (text_with_non_english_chars, 69.45, 'Standard'),
    (easy_text, 84.34, 'Easy'),
    (fairly_easy_text, 75.88, 'Fairly Easy'),
    (text_with_punctuations, 99.23, 'Very Easy'),
    (very_easy_arabic_text, 119.19, 'Very Easy'),
    (very_easy_emoji_text, 114.12, 'Very Easy'),
    (very_easy_unicode_text, 120.21, 'Very Easy')
]


### These tests are in place to ring-fench the functionality provided by textstat.
### They do not validate if these are right or wrong, that discussion is best to be taken up with the maintainer of the library.


@pytest.mark.parametrize("text,expected_score,expected_quality", text_to_return_value_mapping)
def test_given_a_correct_text_when_ease_of_reading_check_is_applied_then_respective_scores_are_returned(
    text: str, expected_score: float, expected_quality: str
):
    # given, when: text is as in the dictionary
    actual_score = ease_of_reading_score(text)

    # then
    assert (actual_score == expected_score) or (actual_score is expected_score), (
        f"Ease of reading score should NOT " f"have been returned, expected {expected_score}"
    )

    # given, when
    actual_quality = ease_of_reading(actual_score)

    # then
    assert actual_quality == expected_quality, (
        f"Ease of reading should NOT " f"have been returned, expected {expected_quality}"
    )


ease_of_reading_check_score_to_words_mapping = [
    (NaN, NOT_APPLICABLE),
    (0, "Very Confusing"),
    (15, "Very Confusing"),
    (40, "Difficult"),
    (55, "Fairly Difficult"),
    (65, "Standard"),
    (75, "Fairly Easy"),
    (85, "Easy"),
    (87.5, "Easy"),
    (95, "Very Easy"),
    (100, "Very Easy"),
]


@pytest.mark.parametrize("score,expected_result", ease_of_reading_check_score_to_words_mapping)
def test_given_ease_of_reading_score_when_converted_to_words_then_return_right_words(
    score: float, expected_result: str
):
    # given, when
    actual_result = ease_of_reading(score)

    # then
    assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"


ease_of_reading_to_summarised_mapping = [
    (NaN, NOT_APPLICABLE),
    ("Very Confusing", "Confusing"),
    ("Difficult", "Difficult"),
    ("Fairly Difficult", "Difficult"),
    ("Standard", "Standard"),
    ("Fairly Easy", "Easy"),
    ("Easy", "Easy"),
    ("Very Easy", "Easy"),
]


@pytest.mark.parametrize("reading,expected_result", ease_of_reading_to_summarised_mapping)
def test_given_ease_of_reading_score_when_converted_to_words_then_return_right_word(reading: str, expected_result: str):
    # given, when
    actual_result = ease_of_reading_summarised(reading)

    # then
    assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"
