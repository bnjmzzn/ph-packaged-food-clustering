# src/retrieve.py
from huggingface_hub import HfApi

from config import HF_REPO_ID


def retrieve_latest_revision():
    api = HfApi()
    info = api.dataset_info(HF_REPO_ID)
    print(f"Repo: {HF_REPO_ID}")
    print(f"Revision SHA: {info.sha}")
    print(f"Last modified: {info.last_modified}")


if __name__ == "__main__":
    retrieve_latest_revision()