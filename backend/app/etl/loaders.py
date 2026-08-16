import pandas as pd


def prepare_for_database(
    df: pd.DataFrame,
) -> list[dict]:

    return df.to_dict(
        orient="records"
    )