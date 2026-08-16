from pathlib import Path

import pandas as pd

from backend.app.etl.readers import read_csv
from backend.app.etl.transformers import (
    clean_column_names,
    remove_empty_rows,
    transform_employee_records,
)
from backend.app.etl.validators import (
    validate_not_empty,
    validate_required_columns,
)


EMPLOYEE_COLUMNS = [
    "employee_id",
    "full_name",
    "email",
    "department_id",
    "job_title",
    "location",
    "employment_type",
    "hire_date",
    "annual_salary",
]


def process_csv(
    file_path: str | Path,
) -> pd.DataFrame:

    df = read_csv(file_path)

    validate_not_empty(df)

    df = clean_column_names(df)

    df = remove_empty_rows(df)

    return df


def process_employee_csv(
    file_path: str | Path,
) -> list[dict]:

    df = process_csv(file_path)

    validate_required_columns(
        df,
        EMPLOYEE_COLUMNS,
    )

    return transform_employee_records(df)