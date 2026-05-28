import os
from pathlib import Path


def get_repo_path() -> Path:
    repo = os.environ.get("REPO_PATH")
    if repo:
        return Path(repo)
    # Two levels up: mcp-server/tools/ -> mcp-server/ -> repo root
    return Path(__file__).parent.parent.parent
