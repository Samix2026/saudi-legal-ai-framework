import csv
import json
from pathlib import Path
from typing import Optional
from tools import get_repo_path

_DATASET = "datasets/saudi-contract-risk-dataset.csv"

_KEEP_FIELDS = (
    "id",
    "contract_type",
    "clause_category",
    "clause_text",
    "risk_level",
    "risk_reason",
    "saudi_legal_note",
    "recommended_revision",
    "related_regulation",
)


def find_risks(
    contract_type: Optional[str] = None,
    risk_level: Optional[str] = None,
    category: Optional[str] = None,
) -> str:
    csv_path: Path = get_repo_path() / _DATASET
    if not csv_path.exists():
        return json.dumps(
            {"error": f"Dataset not found: {csv_path}"}, ensure_ascii=False
        )

    results = []
    with open(csv_path, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if contract_type and row.get("contract_type") != contract_type:
                continue
            if risk_level and row.get("risk_level") != risk_level:
                continue
            if category and row.get("clause_category") != category:
                continue
            results.append({k: row.get(k, "") for k in _KEEP_FIELDS})

    if not results:
        return json.dumps(
            {
                "message": "No matching risk patterns found",
                "filters": {
                    "contract_type": contract_type,
                    "risk_level": risk_level,
                    "category": category,
                },
            },
            ensure_ascii=False,
            indent=2,
        )

    return json.dumps(
        {"count": len(results), "results": results},
        ensure_ascii=False,
        indent=2,
    )
