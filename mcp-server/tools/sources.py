from pathlib import Path
from tools import get_repo_path

VALID_REGULATIONS = {
    "labor-law",
    "companies-law",
    "civil-transactions-law",
    "commercial-courts",
    "pdpl",
    "e-commerce-law",
    "evidence-law",
    "whistleblower-protection",
    "legal-profession-law",
    "bankruptcy-law",
    "regulation-index",
    "saudi-laws",
    "open-data-judicial-sources",
}


def read_source(regulation: str) -> str:
    if regulation not in VALID_REGULATIONS:
        return (
            f"Unknown regulation '{regulation}'. "
            f"Valid options: {', '.join(sorted(VALID_REGULATIONS))}"
        )
    source_path: Path = get_repo_path() / "sources" / f"{regulation}.md"
    if not source_path.exists():
        return f"Source file not found at expected path: {source_path}"
    return source_path.read_text(encoding="utf-8")
