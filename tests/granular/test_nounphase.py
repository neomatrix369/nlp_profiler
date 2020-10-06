import pytest
import numpy as np

from nlp_profiler.granular_features.noun_phase_count import count_phase, gather_nouns
from nlp_profiler.constants import NaN


sentence = "European authorities fined Google a record $5.1 billion on Wednesday \
            for abusing its power in the mobile phone market and ordered the company \
            to alter its practices"

text_to_return_value_mapping = [
    (sentence, [('European', 'NORP'), ('Google', 'ORG'), ('$5.1 billion', 'MONEY'), ('Wednesday', 'DATE')])
]

@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_gather_noun(text: str, expected_result: str):
    
    actual_result = gather_nouns(text)
    
    assert actual_result == expected_result, \
    f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"


text_to_return_value_mapping = [
    ("", [])
]

@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_failed_gather_noun(text: str, expected_result: str):

    actual_result = gather_nouns(text)

    assert actual_result == expected_result, \
    f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"


text_to_return_value_mapping = [
    (sentence, 4)
]

@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_count_noun(text: str, expected_result: str): 

    actual_result = count_noun_phase(text)
    
    assert actual_result == expected_result, \
    f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"

text_to_return_value_mapping = [
    ("", 0)
]

@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_failed_count_noun(text: str, expected_result: str): 

    actual_result = count_noun_phase(text)
    
    assert actual_result == expected_result, \
    f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"
