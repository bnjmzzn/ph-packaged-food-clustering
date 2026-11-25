# src/config.py
from pathlib import Path

SEED = 67

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"

HF_REPO_ID = "openfoodfacts/product-database"
HF_REMOTE_FILENAME = "food.parquet"
HF_REVISION = "e49264ae39d1fb35f7abbc4915dbe715af06345b"

RAW_PARQUET_NAME = "off_food_worldwide_raw.parquet"
RAW_PARQUET_PATH = RAW_DIR / RAW_PARQUET_NAME