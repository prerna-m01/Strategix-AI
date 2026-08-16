import pandas as pd
import pytest
from backend.app.etl.loaders import load_employees
from backend.app.etl.transformers import (
    clean_column_names,
    remove_empty_rows,
)
from backend.app.etl.validators import (
    validate_not_empty,
    validate_required_columns,
)


def test_clean_column_names():

    df = pd.DataFrame(
        columns=[
            "Employee ID",
            "Full Name",
            "Annual Salary",
        ]
    )

    result = clean_column_names(df)

    assert list(result.columns) == [
        "employee_id",
        "full_name",
        "annual_salary",
    ]


def test_remove_empty_rows():

    df = pd.DataFrame(
        [
            {"name": "Alice", "salary": 50000},
            {"name": None, "salary": None},
        ]
    )

    result = remove_empty_rows(df)

    assert len(result) == 1


def test_validate_required_columns():

    df = pd.DataFrame(
        columns=[
            "employee_id",
            "full_name",
        ]
    )

    validate_required_columns(
        df,
        ["employee_id", "full_name"],
    )


def test_validate_missing_columns():

    df = pd.DataFrame(
        columns=["employee_id"]
    )

    with pytest.raises(ValueError):

        validate_required_columns(
            df,
            [
                "employee_id",
                "full_name",
            ],
        )


def test_validate_not_empty():

    df = pd.DataFrame(
        [{"employee_id": "EMP001"}]
    )

    validate_not_empty(df)


def test_validate_empty_dataset():

    df = pd.DataFrame()

    with pytest.raises(ValueError):

        validate_not_empty(df)

def test_process_employee_records(tmp_path):

    csv_file = tmp_path / "employees.csv"

    csv_file.write_text(
        "employee_id,full_name,email,department_id,"
        "job_title,location,employment_type,hire_date,"
        "annual_salary\n"
        "EMP001,Alice Smith,alice@example.com,1,"
        "Engineer,Delhi,Full-Time,2026-01-15,750000\n"
    )

    from backend.app.etl.pipeline import process_employee_csv

    records = process_employee_csv(csv_file)

    assert len(records) == 1
    assert records[0]["employee_id"] == "EMP001"
    assert records[0]["full_name"] == "Alice Smith"
    assert records[0]["department_id"] == 1
    assert records[0]["annual_salary"] == 750000