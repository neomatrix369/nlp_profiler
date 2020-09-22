import re

import emoji

from nlp_profiler.constants import NaN


### Emojis

def gather_emojis(text: str) -> list:
    if (not isinstance(text, str)) or (len(text.strip()) == 0):
        return []

    emoji_expaned_text = emoji.demojize(text)
    return re.findall(r'\:(.*?)\:', emoji_expaned_text)


def count_emojis(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    list_of_emojis = gather_emojis(text)
    return len(list_of_emojis)
