from nlp_profiler.constants import NaN
from nlp_profiler.granular_features.alphanumeric import count_alpha_numeric
from nlp_profiler.granular_features.chars_spaces_and_whitespaces \
    import count_whitespaces, count_chars
from nlp_profiler.granular_features.punctuations import count_punctuations

# Note: '±', '§', '€' and '£' have been removed from the
# below list as it can be found on UK Qwerty Keyboards
# and they have been added to the punctuation list
NON_STANDARD_ASCII_CHARS = "‚ƒ„…†‡ˆ‰Š‹ŒŽ•™š›œžŸ¡¢¤¥¦¨©ª«¬­®¯°²³´" \
                           "µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß" \
                           "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"



# English characters constitutes of
#                    alphanumerics (letters and numbers),
#                    punctuations and
#                    whitespaces (includes spaces)
#                    any additional symbols i.e. €, £, ±, §
# See https://en.wikipedia.org/wiki/ASCII or https://ascii.co.uk/table for standard characters
def count_english_chars(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return count_alpha_numeric(text) + count_whitespaces(text) + count_punctuations(text)


# Non-English or foreign characters constitute of
#             everything else that are not English characters
# See https://en.wikipedia.org/wiki/ASCII or https://ascii.co.uk/table for non-standard characters
def count_non_english_chars(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return count_chars(text) - count_english_chars(text)
