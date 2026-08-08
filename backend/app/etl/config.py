from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

DATASETS_DIR = BASE_DIR / "datasets"

RAW_DATA_DIR = DATASETS_DIR / "raw"
PROCESSED_DATA_DIR = DATASETS_DIR / "processed"
EXTERNAL_DATA_DIR = DATASETS_DIR / "external"


EMPLOYEE_RAW_FILE = RAW_DATA_DIR / "employees.csv"