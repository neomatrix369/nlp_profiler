import pandas as pd
import swifter  # noqa

from nlp_profiler.constants import DEFAULT_PARALLEL_METHOD, SWIFTER_METHOD
from nlp_profiler.generate_features.parallelisation_methods \
    import get_progress_bar, using_joblib_parallel, using_swifter


def generate_features(main_header: str,
                      high_level_features_steps: list,
                      new_dataframe: pd.DataFrame,
                      parallelisation_method: str = DEFAULT_PARALLEL_METHOD):
    generate_feature_progress_bar = get_progress_bar(high_level_features_steps)

    # Using swifter or Using joblib Parallel and delay method:
    parallelisation_method_function = using_joblib_parallel
    if parallelisation_method == SWIFTER_METHOD:
        parallelisation_method_function = using_swifter

    for _, (new_column, source_column, transformation_function) in \
            enumerate(generate_feature_progress_bar):
        source_field = new_dataframe[source_column]
        generate_feature_progress_bar.set_description(
            f'{main_header}: {source_column} => {new_column}'
        )

        new_dataframe[new_column] = parallelisation_method_function(
            source_field, transformation_function, new_column
        )
