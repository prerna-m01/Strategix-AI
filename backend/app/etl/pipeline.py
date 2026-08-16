from pathlib import Path

import pandas as pd

from backend.app.etl.readers import read_csv
from backend.app.etl.transformers import (
    clean_column_names,
    remove_empty_rows,
)
from backend.app.etl.validators import (
    validate_not_empty,
)


def process_csv(
    file_path: str | Path,
) -> pd.DataFrame:

    df = read_csv(file_path)

    validate_not_empty(df)

    df = clean_column_names(df)

    df = remove_empty_rows(df)

    return df