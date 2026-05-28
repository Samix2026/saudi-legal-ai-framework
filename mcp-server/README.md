# Saudi Legal AI — MCP Server

MCP server exposing the Saudi Legal AI Framework as tools for Claude Desktop.

## Tools

| Tool | Description |
|------|-------------|
| `get_legal_skill` | Returns a full skill file (8 domains) as AI context |
| `get_legal_source` | Returns an official Saudi regulation reference (13 sources) |
| `search_contract_risks` | Queries the contract risk dataset by type / level / category |

## Claude Desktop Setup

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "saudi-legal-ai": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "/Users/samialmohaimeed/saudi-legal-ai-framework:/repo:ro",
        "-e", "REPO_PATH=/repo",
        "saudi-legal-mcp"
      ]
    }
  }
}
```

Then restart Claude Desktop. Claude will automatically call the tools when you ask legal questions.

## Build

```bash
cd mcp-server
docker build -t saudi-legal-mcp .
```

## Local Development (no Docker)

```bash
cd mcp-server
pip install -r requirements.txt
REPO_PATH=/Users/samialmohaimeed/saudi-legal-ai-framework python server.py
```

## Example Queries

Once connected in Claude Desktop:

- "راجع هذا العقد وحدد البنود المخالفة لنظام العمل السعودي"
- "ما شروط التحكيم في المملكة؟"
- "ما مخاطر عقود الـ SaaS من الدرجة الحرجة؟"
- "أعطني نص نظام المحاكم التجارية م/93"

## Notes

- The repo is mounted read-only — the server reads live files, nothing is copied into the image.
- Uses `stdio` transport (default), compatible with Claude Desktop's MCP client.
- Requires Docker to be running when Claude Desktop starts.
