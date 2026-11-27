# src/config.py
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

SEED = 67

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / "data" / "raw"
INTERIM_DIR = ROOT_DIR / "data" / "interim"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"
DUCKDB_TEMP_DIR = ROOT_DIR / "data" / "duckdb_tmp"

HF_REPO_ID = "openfoodfacts/product-database"
HF_REMOTE_FILENAME = "food.parquet"
HF_REVISION = "e49264ae39d1fb35f7abbc4915dbe715af06345b"
HF_REMOTE_URL = f"hf://datasets/{HF_REPO_ID}@{HF_REVISION}/{HF_REMOTE_FILENAME}"

RAW_PARQUET_NAME = "openfoodfacts_food_raw.parquet"
RAW_PARQUET_PATH = RAW_DIR / HF_REMOTE_FILENAME

PH_RAW_PARQUET_NAME = "openfoodfacts_food_ph_raw.parquet"
PH_RAW_PARQUET_PATH = INTERIM_DIR / PH_RAW_PARQUET_NAME