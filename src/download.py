# src/download.py
import os
import shutil

from dotenv import load_dotenv
from huggingface_hub import hf_hub_download

from src.config import (
    HF_REMOTE_FILENAME,
    HF_REPO_ID,
    HF_REVISION,
    RAW_DIR,
    RAW_PARQUET_PATH,
)


def download_raw():
    if RAW_PARQUET_PATH.exists():
        print(f"Already downloaded: {RAW_PARQUET_PATH}")
        return RAW_PARQUET_PATH

    load_dotenv()
    token = os.getenv("HF_TOKEN")
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    downloaded_path = hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=HF_REMOTE_FILENAME,
        repo_type="dataset",
        revision=HF_REVISION,
        local_dir=RAW_DIR,
        token=token or None,
    )

    shutil.move(downloaded_path, RAW_PARQUET_PATH)
    print(f"Saved: {RAW_PARQUET_PATH}")
    return RAW_PARQUET_PATH


if __name__ == "__main__":
    download_raw()