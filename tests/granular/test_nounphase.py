import pytest

from nlp_profiler.granular_features.noun_phase_count import count_noun_phase, gather_nouns

sentence = "European authorities fined Google a record $5.1 billion on Wednesday \
            for abusing its power in the mobile phone market and ordered the company \
            to alter its practices"

text_to_return_value_mapping = [
    (sentence, [('european', 'JJ'), ('authorities', 'NNS'), ('record', 'NN'),
                ('wednesday', 'NN'), ('power', 'NN'), ('mobile', 'JJ'),
                ('phone', 'NN'), ('market', 'NN'), ('company', 'NN'),
                ('practices', 'NNS')]),
    ("I love ⚽ very much 😁 ", [('i', 'NN'), ('much', 'JJ'), ('beaming_face_with_smiling_eyes', 'NNS')]),
    ("", [])
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_gather_noun(text: str, expected_result: str):
    
    actual_result = gather_nouns(text)

    assert actual_result == expected_result, \
        f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_failed_gather_noun(text: str, expected_result: str):

    actual_result = gather_nouns(text)

    assert actual_result == expected_result, \
        f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"


text_to_return_value_mapping = [
    (sentence, 10),
    ("I love ⚽ very much 😁 ", 3),
    ("", 0)
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_count_noun(text: str, expected_result: str): 

    actual_result = count_noun_phase(text)

    assert actual_result == expected_result, \
        f"Expected Result: {expected_result} \
    Actual Result: {actual_result}"
