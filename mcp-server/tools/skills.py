from pathlib import Path
from tools import get_repo_path

VALID_DOMAINS = {
    "contract-review",
    "labor-law-analysis",
    "commercial-dispute",
    "compliance-check",
    "legal-drafting",
    "arbitration",
    "real-estate-contracts",
    "intellectual-property-law",
}


def read_skill(domain: str) -> str:
    if domain not in VALID_DOMAINS:
        return (
            f"Unknown domain '{domain}'. "
            f"Valid domains: {', '.join(sorted(VALID_DOMAINS))}"
        )
    skill_path: Path = get_repo_path() / "skills" / f"{domain}.md"
    if not skill_path.exists():
        return f"Skill file not found at expected path: {skill_path}"
    return skill_path.read_text(encoding="utf-8")
