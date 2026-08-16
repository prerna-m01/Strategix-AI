import pandas as pd


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
) -> None:

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def validate_not_empty(df: pd.DataFrame) -> None:

    if df.empty:
        raise ValueError(
            "Dataset cannot be empty."
        )