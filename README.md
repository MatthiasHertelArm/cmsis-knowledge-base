# CMSIS Knowledge Base for the CMSIS Developer Assistant (prototype)

A knowledge base with a small knowledge graph that adds the *how, when and why* to the *what* of the CMSIS Pack Docs. It is served to coding agents through three MCP tools and is built to work with small local models: summaries first, full text only on request.

Status: working prototype, built 4 Oct 2026 against live sources. All knowledge units are `status: draft`. See [HANDOVER.md](HANDOVER.md) for decisions, known issues and open points.

## Quick start (5 minutes, prebuilt index included)

```bash
scripts/setup.sh                       # venv + dependencies
. .venv/bin/activate
python tests/test_kb.py                # 28 checks, incl. an MCP round trip
python tools/kb_server.py build/knowledge.db   # MCP server on stdio
```

Connect an agent: [agent-setup/vscode/mcp.json](agent-setup/vscode/mcp.json) for VS Code / Copilot, [agent-setup/claude-code](agent-setup/claude-code/README.md) for Claude Code. Add [copilot-instructions.md](agent-setup/vscode/copilot-instructions.md) to the project so the agent actually uses the tools.

The embedding model (BAAI/bge-small-en-v1.5, about 130 MB) is downloaded on first start. Without network, or with `KB_NO_VEC=1`, the server falls back to keyword search (BM25) only.

## MCP tools

| Tool | Purpose |
|---|---|
| `knowledge_search(query, cbuild?, device?, components?, compiler?, tools?, domain?, types?, k=8, budget_tokens=800)` | Hybrid search (BM25 + embeddings, rank fusion). Exact error text is pinned to the top. With `cbuild` the results are filtered to the project's device, core, components and compiler. Returns id, title, summary only. |
| `knowledge_get(id)` | Full unit. Never truncated. |
| `knowledge_expand(id, relation?)` | One hop in the graph: requires, constrains, refines, applies_to, part_of, documents ... |

Response extras: `exact_symptom`, `applies: "unverified"` (context says nothing about a dimension the unit targets), `context_unresolved` (device not known to the graph), `local_entities` (workspace overlay in use).

## Data model in one picture

```
Entities (generated from pack index + PDSC, never edited)          Knowledge units (Markdown + YAML in Git)
board:STMicroelectronics::B-U585I-IOT02A                           procedure | rule | concept | pattern | troubleshooting
  └ mounted_on → device:STM32U585AIIx                                   │
                   ├ has_core → core:Cortex-M33   ◄──── applies_to ─────┤  e.g. applies_to: {core: [Cortex-M33], toolchain: [AC6]}
                   └ part_of → subfamily → family → pack                 ├ requires / refines / constrains / produces / consumes
```

* A unit with empty `applies_to` is universal. Validity inherits along `part_of`.
* Filtering is AND across dimensions (core, toolchain, family ...) and OR within one.
* A more specific unit (`refines`) replaces the general one when both match.
* `build_index.py --strict` fails if an `applies_to` target no longer exists (stale detection for CI).

Examples with real data: `units/troubleshooting/ts-packchk-m302.md`, `units/skills/procedure/proc-generate-debug-sequences.md`, `units/skills/rule/rule-no-fabrication-generate-debug-sequences.md`. The kickoff deck in `docs/kickoff/` walks through five examples.

## Devices that are not public yet

`tools/overlay.py` adds entities from the developer's workspace at run time, on top of the index:

1. packs with `path:` in `*.csolution.yml` / `*.cbuild.yml`
2. any `*.pdsc` in the workspace (pack repo under construction)
3. `$CMSIS_PACK_ROOT/.Local/local_repository.pidx`
4. `kb-entities.yml` (workspace root or `.cmsis/`) for devices that only have documentation, and for manually maintained cores. Format: `tests/fixtures/workspace/.cmsis/kb-entities.yml`

The server loads it when `knowledge_search` gets a `cbuild` path and reloads on change. The index file is never modified. As a CLI (`python tools/overlay.py <workspace> <out>`) it produces entity files for a vendor pack's CI; `build_index.py` accepts several `--entities` folders.

## Repository layout

| Path | Content |
|---|---|
| `tools/entities.py` | Pack index + PDSC → entity nodes and edges |
| `tools/skill2ku.py` | Stage 1: cmsis-skills → procedures, rules, concepts, artifacts (deterministic). Also the CMSIS Developer Assistant's own skills (`<checkout>/skills`, chosen through its `catalog.json`). The text files a skill ships (templates, scripts) become `asset` entities with the file as body |
| `tools/routes2ku.py` | One routing unit per domain (`route-project`, …): which procedure for which task and the usual order, from the extension's `scripts/skills.config.json` |
| `stage2/` | Stage 2: LLM refinement prompt v2, inputs and outputs of the test runs (`out` = v1, `out_v2` = v2) |
| `tools/stage2_merge.py` | Writes stage 2 JSON into frontmatter, canonical rules, extracted units |
| `tools/errcat.py` | devtools message tables and csolution log calls → troubleshooting units |
| `tools/build_index.py` | Lint, resolve `applies_to`, FTS5, sqlite-vec, edges → `knowledge.db` |
| `tools/kb_lib.py`, `tools/kb_server.py` | Retrieval and MCP server |
| `tools/overlay.py` | Workspace entities for unreleased devices |
| `units/` | Generated knowledge units (all draft). `units/cda-skills` and `units/cda-routes` come from a checkout of the extension: `CDA=<checkout> scripts/rebuild.sh` |
| `build/` | `entities/*.jsonl` and prebuilt `knowledge.db` |
| `tests/` | `test_kb.py` and fixtures (incl. a workspace with a local DFP and a docs-only device) |
| `scripts/` | `setup.sh`, `fetch_sources.py`, `rebuild.sh` |
| `docs/design/` | Design documents 00 to 05 (German): concept and schema, migration findings, domains, source list with licenses, status |
| `docs/kickoff/` | Team kickoff deck (English) and its generator |

## Full rebuild from live sources

```bash
scripts/rebuild.sh            # 4 to 7 minutes; NO_VEC=1 skips the embeddings (about 3 minutes)
```

Fetches the Keil pack index and all active PDSC files (via the keil.com/pack mirror), clones cmsis-skills and devtools, runs the whole pipeline and the tests. Inputs of the shipped build: cmsis-skills@25c2085, devtools@30f5e81, pack index of 4 Oct 2026.

## Licensing of content

Code in `tools/` and `scripts/`: Arm internal prototype, license to be decided. Generated units carry `source`, `license` and `mode` in their frontmatter. Everything shipped here is derived from Apache-2.0 sources (cmsis-skills, devtools, Open-CMSIS-Pack PDSC metadata). `docs/design/04_quellenliste.md` lists further sources per domain with mode V (full text), S (own summary + link) or R (reference only); Arm documents, Keil KB and Learning Paths (CC BY-SA 4.0) need legal review before use.
