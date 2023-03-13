import os
import shutil
import tempfile
from contextlib import redirect_stdout
from datetime import datetime
from time import time

import git
import pandas as pd
from line_profiler import LineProfiler

from nlp_profiler.granular_features.punctuations import ADDITIONAL_SYMBOLS

CURRENT_SOURCE_FILEPATH = os.path.abspath(__file__)
EXPECTED_DATA_PATH = f"{os.path.dirname(CURRENT_SOURCE_FILEPATH)}/data"
TARGET_PROFILE_REPORT_FOLDER = ".cprofile/"


def internal_assert_benchmark(
    expected_execution_time: float,
    target_function,
    profile_filename_prefix: str,
    commit_id: str,
    custom_processing_function,
):
    # given
    if not os.path.exists(TARGET_PROFILE_REPORT_FOLDER):
        os.makedirs(TARGET_PROFILE_REPORT_FOLDER)

    remove_joblib_cache()

    profile = LineProfiler()
    source_data = generate_data()

    # when: using default method (joblib Parallel) for parallelisation
    start_execution_time = time()
    profile_wrapper = profile(target_function)
    custom_processing_function(source_data, profile_wrapper)
    actual_execution_time = time() - start_execution_time
    output_filename = (
        f"{TARGET_PROFILE_REPORT_FOLDER}/{profile_filename_prefix}-"
        f'{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}-'
        f"{shorten_sha(git_current_head_sha())}"
    )
    with open(f"{output_filename}.txt", "w") as file:
        with redirect_stdout(file):
            profile.print_stats()
    profile.dump_stats(f"{output_filename}.lprof")

    # then
    assert actual_execution_time <= expected_execution_time, (
        f"Expected duration: {expected_execution_time}, Actual duration: {actual_execution_time}. "
        f"Slow down by: {abs(actual_execution_time - expected_execution_time)} seconds. "
        f"We have crossed the benchmark limit after a speed up via commit {commit_id}."
    )


def assert_benchmark(expected_execution_time: float, target_function, profile_filename_prefix: str, commit_id: str):
    def custom_processing_function(source_data, profile_wrapper):
        for each in source_data:
            profile_wrapper(each)

    internal_assert_benchmark(
        expected_execution_time, target_function, profile_filename_prefix, commit_id, custom_processing_function
    )


def assert_benchmark_multiple_features(
    expected_execution_time: float,
    target_function,
    heading: str,
    parallelisation_method: str,
    profile_filename_prefix: str,
    commit_id: str,
):
    def custom_processing_function(source_data, profile_wrapper):
        dataframe = pd.DataFrame(source_data, columns=["text"])
        profile_wrapper(heading, dataframe, "text", parallelisation_method)

    internal_assert_benchmark(
        expected_execution_time, target_function, profile_filename_prefix, commit_id, custom_processing_function
    )


def shorten_sha(long_sha):
    return long_sha[:7]


def git_current_head_sha():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.commit.hexsha


def generate_data() -> list:
    repeated_symbols = ADDITIONAL_SYMBOLS[0] + ADDITIONAL_SYMBOLS[0]
    text_with_emojis = "I love ⚽ very much 😁."
    text_with_a_number = "2833047 people live in this area. It is not a good area."
    text_with_two_numbers = "2833047 and 1111 people live in this area."
    text_with_punctuations = "This sentence does not seem to have too many commas, periods or semicolons (;)."
    text_with_a_date = "The date today is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."
    text_with_dates = "The date today is 28/04/2020 and tomorrow's date is 29/04/2020."
    text_with_duplicates = "Everyone here works so hard. People work hard. " "I think they have a good trait."
    text_with_repeated_letters = "Harrington PPPPPPpppppeople work hard." " I think they have a goodd traittttt."
    text_with_repeated_digits = "283047 people live in this area3333 22224444"
    text_with_repeated_punctuations = "283047 people live in this area[[[ ]]] :::;;;;" + repeated_symbols
    text_with_repeated_spaces = "283047   people live in this  area"
    text_with_whitespaces = "2833047 pe\nople li\tve i\rn this area"
    text_with_repeated_whitespaces = "2833047   \r\rpeople\n\n   live in   th\nis are\t\ta"
    text_with_english_chars = "±§£ABCDEabcdef0123456789\nis are\t\n" + r"""!#$%&()*+-./:;<=>?@[\]^_`{|}~"""
    text_with_non_english_chars = (
        "2833047 pe\nople li\tve i\rn this area"
        '‚ƒ„…†‡ˆ‰Š‹ŒŽ•™š›œžŸ¡¢¤¥¦¨©ª«¬­®¯°²³´"'
        "µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
        "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
        "This sentence is in japanese (kana) ろぬふうえおやゆゆわほへへて"
        "This sentence is in japanese (kana compact) おっあこおおがおんわお"
        "فصصصشببلااتنخمككك This sentence is in arabic"
    )
    return [
        text_with_emojis,
        text_with_a_number,
        text_with_two_numbers,
        text_with_repeated_letters,
        text_with_repeated_digits,
        text_with_punctuations,
        text_with_repeated_punctuations,
        text_with_a_date,
        text_with_dates,
        text_with_duplicates,
        text_with_repeated_spaces,
        text_with_whitespaces,
        text_with_repeated_whitespaces,
        text_with_english_chars,
        text_with_non_english_chars,
    ]


def remove_joblib_cache():
    if os_temp_dir := tempfile.gettempdir():
        cache_folder = f"{os_temp_dir}/joblib/nlp_profiler"
        print()
        if os.path.exists(cache_folder):
            print(f"~~~ Found the NLP Profiler cache folder at {cache_folder}, will be removed.")
            shutil.rmtree(cache_folder)
            print(f"~~~ Successfully deleted the NLP Profiler cache folder at {cache_folder}.")
        else:
            print(f"~~~ The NLP Profiler cache folder {cache_folder} was NOT found. Nothing to remove.")
        print()
