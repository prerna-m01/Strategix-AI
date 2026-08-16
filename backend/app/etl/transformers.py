import pandas as pd


def clean_column_names(
    df: pd.DataFrame,
) -> pd.DataFrame:

    result = df.copy()

    result.columns = [
        column.strip().lower().replace(" ", "_")
        for column in result.columns
    ]

    return result


def remove_empty_rows(
    df: pd.DataFrame,
) -> pd.DataFrame:

    return df.dropna(how="all").reset_index(drop=True)