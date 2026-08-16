from pathlib import Path

import pandas as pd


def read_csv(file_path: str | Path) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    if path.suffix.lower() != ".csv":
        raise ValueError(
            "Only CSV files are supported."
        )

    return pd.read_csv(path)