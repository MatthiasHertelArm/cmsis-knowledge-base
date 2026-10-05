#!/usr/bin/env python3
"""kb_server: MCP-Server mit knowledge_search, knowledge_get, knowledge_expand.

Aufruf (stdio): python kb_server.py <knowledge.db>
Umgebungsvariablen: KB_NO_VEC=1 schaltet Embeddings ab (nur BM25, fuer schwache Rechner).
"""
import json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kb_lib import KB  # noqa: E402
from mcp.server.mcpserver import MCPServer  # noqa: E402

kb = KB(sys.argv[1] if len(sys.argv) > 1 else "knowledge.db", use_vec=not os.environ.get("KB_NO_VEC"))
srv = MCPServer("cmsis-knowledge", instructions=(
    "CMSIS knowledge base. Call knowledge_search first; it returns summaries only. "
    "Call knowledge_get for the full unit before acting. Procedures are returned complete and "
    "must be followed including their stop conditions. Use knowledge_expand to find prerequisites."))


@srv.tool()
def knowledge_search(query: str, domain: str | None = None, types: list[str] | None = None,
                     cbuild: str | None = None, device: str | None = None,
                     components: list[str] | None = None, compiler: str | None = None,
                     tools: list[str] | None = None,
                     k: int = 8, budget_tokens: int = 800) -> str:
    """Hybrid search (BM25 + embeddings) over CMSIS knowledge units.
    Paste exact error messages as query to hit troubleshooting units.
    Pass cbuild (path to *.cbuild.yml) and/or device/components/compiler/tools (e.g. ['packchk']) to filter by project context."""
    ctx, ov = None, None
    if cbuild:
        ov = kb.use_workspace(cbuild)          # lokale DFPs und kb-entities.yml des Workspace
        c = KB.parse_cbuild(cbuild)
        ctx = kb.context_entities(c["device"], c["components"], c["compiler"], c["board"])
    if device or components or compiler or tools:
        extra = kb.context_entities(device, components or [], compiler, tools=tools or [])
        ctx = (ctx or set()) | extra
    res = kb.search(query, domain, types, ctx, k, budget_tokens)
    if ov and ov.get("nodes"):
        res["local_entities"] = {"workspace": ov["workspace"], "nodes": ov["nodes"], "devices": ov["devices"]}
    return json.dumps(res, ensure_ascii=False)


@srv.tool()
def knowledge_get(id: str) -> str:
    """Full knowledge unit with body and metadata. Never truncated."""
    return json.dumps(kb.get(id), ensure_ascii=False)


@srv.tool()
def knowledge_expand(id: str, relation: str | None = None) -> str:
    """One hop in the graph: requires, refines, constrains, produces, consumes, references,
    applies_to, part_of, documents. Returns neighbor titles and summaries."""
    return json.dumps(kb.expand(id, relation), ensure_ascii=False)


if __name__ == "__main__":
    srv.run("stdio")
