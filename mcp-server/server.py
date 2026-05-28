import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from tools.skills import read_skill, VALID_DOMAINS
from tools.sources import read_source, VALID_REGULATIONS
from tools.search import find_risks

REPO_PATH = Path(os.environ.get("REPO_PATH", Path(__file__).parent.parent))

mcp = FastMCP("Saudi Legal AI Framework")


@mcp.tool()
def get_legal_skill(domain: str) -> str:
    """
    Get the legal reasoning skill file for a specific Saudi law domain.

    Use this when the user asks about:
    - contract review → contract-review
    - labor law / employment → labor-law-analysis
    - commercial dispute → commercial-dispute
    - compliance / PDPL / Saudization → compliance-check
    - legal drafting / notices → legal-drafting
    - arbitration → arbitration
    - real estate / lease → real-estate-contracts
    - intellectual property → intellectual-property-law

    Returns the full skill file content to use as AI context.

    Args:
        domain: One of: contract-review, labor-law-analysis, commercial-dispute,
                compliance-check, legal-drafting, arbitration,
                real-estate-contracts, intellectual-property-law
    """
    return read_skill(domain)


@mcp.tool()
def get_legal_source(regulation: str) -> str:
    """
    Get the official Saudi regulation reference for a specific law.

    Use this to retrieve authoritative Saudi legal source content for:
    - labor-law         → نظام العمل م/51
    - companies-law     → نظام الشركات م/132
    - civil-transactions-law → نظام المعاملات المدنية م/191
    - commercial-courts → نظام المحاكم التجارية م/93
    - pdpl              → نظام حماية البيانات الشخصية م/19
    - e-commerce-law    → نظام التجارة الإلكترونية م/126
    - evidence-law      → نظام الإثبات م/43
    - whistleblower-protection → نظام حماية المبلغين م/148
    - legal-profession-law → نظام المحاماة
    - bankruptcy-law    → نظام الإفلاس م/50
    - regulation-index  → فهرس الأنظمة السعودية
    - saudi-laws        → مجموعة الأنظمة السعودية
    - open-data-judicial-sources → المصادر القضائية المفتوحة البيانات

    Args:
        regulation: Regulation name (e.g. 'labor-law', 'pdpl', 'commercial-courts')
    """
    return read_source(regulation)


@mcp.tool()
def search_contract_risks(
    contract_type: str = None,
    risk_level: str = None,
    category: str = None,
) -> str:
    """
    Search the Saudi contract risk database for known legal risk patterns.

    Returns structured risk data including clause text, risk reason,
    Saudi legal note, and recommended revision.

    Use this when:
    - User wants to know risks in a specific contract type
    - User wants to check compliance of a specific clause
    - User wants to understand what makes a clause problematic under Saudi law

    Args:
        contract_type: Optional. One of: Employment Contract, Lease Agreement,
                      NDA, SaaS Agreement, Construction Contract, Supply Agreement,
                      Professional Services Agreement, Commercial Agency Agreement,
                      Shareholder Agreement, Franchise Agreement, Cloud Storage Agreement
        risk_level: Optional. One of: critical, high, medium, low
        category: Optional. One of: Employment & Labor, Saudization, Termination,
                 Liability, Data Protection & Privacy, Jurisdiction & Dispute Resolution,
                 Governing Law, Payment Terms, Confidentiality, Intellectual Property,
                 Force Majeure, Warranties, Indemnification, Corporate Governance
    """
    return find_risks(contract_type, risk_level, category)


if __name__ == "__main__":
    mcp.run()
