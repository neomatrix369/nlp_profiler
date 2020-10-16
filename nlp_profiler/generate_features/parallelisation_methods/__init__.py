import sys
import tempfile

import pandas as pd
import swifter  # noqa
from joblib import Memory, Parallel, delayed
from tqdm.auto import tqdm

memory = Memory(tempfile.gettempdir(), compress=9, verbose=0)


def is_running_from_ipython():
    return sys.argv[-1].endswith('json')


PROGRESS_BAR_WIDTH = 900 if is_running_from_ipython() else None


def get_progress_bar(values: list) -> tqdm:
    cached_tqdm = memory.cache(tqdm)
    return cached_tqdm(values, ncols=PROGRESS_BAR_WIDTH)


def run_task(task_function, value: str):  # pragma: no cover
    # pragma: no cover => multiprocessing leads to loss of test coverage info
    cached_task_function = memory.cache(task_function)
    return cached_task_function(value)


def using_joblib_parallel(
        source_field, apply_function, new_column: str,
) -> pd.DataFrame:
    source_values_to_transform = get_progress_bar(source_field.values)
    source_values_to_transform.set_description(new_column)

    result = Parallel(n_jobs=-1)(
        delayed(run_task)(
            apply_function, each_value
        ) for _, each_value in enumerate(source_values_to_transform)
    )
    source_values_to_transform.update()
    return result


def using_swifter(
        source_field, apply_function, new_column: str = None
) -> pd.DataFrame:
    return source_field \
        .swifter \
        .set_dask_scheduler(scheduler="processes") \
        .allow_dask_on_strings(enable=True) \
        .progress_bar(enable=True, desc=new_column) \
        .apply(apply_function, axis=1)
