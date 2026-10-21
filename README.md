# CMSIS Knowledge Base for the CMSIS Developer Assistant (prototype)

A knowledge base with a small knowledge graph that adds the *how, when and why* to the *what* of the CMSIS Pack Docs. It is served to coding agents through three MCP tools and is built to work with small local models: summaries first, full text only on request.

Status: working prototype, built 4 Oct 2026 against live sources. All knowledge units are `status: draft`. See [HANDOVER.md](HANDOVER.md) for decisions, known issues and open points.

## Quick start (5 minutes)

```bash
scripts/setup.sh                       # venv + dependencies
. .venv/bin/activate
scripts/build_core.sh                  # the core index in about 10 s: licence gate, build/knowledge.core.db, 28 checks
python tools/kb_server.py build/knowledge.core.db   # MCP server on stdio
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
| `tools/errcat_merge.py` | Cause, fix, note and evidence of each message, read from the devtools source (`stage2/errcat-out`), into the troubleshooting units |
| `tools/review_csv.py` | `messages-to-review.csv`: every draft message unit, least certain first, with columns for reviewer and comment |
| `tools/doc2ku.py` | Documentation of open-licence repositories → one concept unit per section. Markdown, doxygen (`*.txt`, doxygen Markdown), reStructuredText and Hugo pages; HTML tables become Markdown tables |
| `tools/issues2ku.py` | Digests of closed GitHub issues (`stage2/issues-out`, written after `stage2/issues_prompt.md`) → troubleshooting units in `units/issues/<repo>`: own words, mode S, a link to the issue, tool output as the only verbatim text |
| `scripts/build_pack.sh` | One local pack from named book collections (refined units preferred, generic units included, scope exclusions applied, edges into the core allowed), installed into the pack root: `scripts/build_pack.sh CPP_Architecture softwarearchitecturewithcplusplusseconde` |
| `tools/pdf2ku.py`, `scripts/build_books.sh` | Test scenario for pack-carried knowledge: books in PDF form (poppler's `pdftohtml` outline and `pdftotext`) → one concept unit per section into `units/books/<book>`, built into the local pack `packs/Local.CPP_Books` and copied into the pack root (`Local/CPP_Books/<version>/`). The books are copyrighted: units and index are git-ignored and never part of `build/knowledge*.db` |
| `tools/stage3_books.py`, `tools/books_generic.py` | Stage 3 for the books (Claude Haiku 5.5 as reader agents or through the Message Batches API): type, summary, triggers and Markdown per section, every answer gated by a script (`stage2/books_prompt.md`); then generic knowledge in own words with a verbatim evidence quote, checked against the core indexes for duplicates and contradictions (`stage2/books_generic_prompt.md`, `stage2/books_conflict_prompt.md`), into `units/books-refined` and `units/books-generic`; `classify-*` with `stage2/books_scope_prompt.md` keeps coding and design knowledge only (`stage2/books-exclusions.json`, read by `build_index.py --exclude`). `tests/eval_conflicts.py` measures what an agent gets for CMSIS and generic requests once a pack is read next to the core |
| `sources/docs.yml`, `sources/docs-ccbysa.yml` | The documentation sources, their licence, domain and published URL; the second holds the CC BY-SA ones |
| `tools/build_index.py` | Lint, resolve `applies_to`, FTS5, sqlite-vec, edges, the `info` table → `knowledge.db`; `--drop`, `--exclude` and `--known` shape a build |
| `tools/check_licences.py` | The licence gate: every unit of the given folders declares an allowed licence and none is `mode: P` |
| `tools/kb_lib.py`, `tools/kb_server.py` | Retrieval and MCP server |
| `tools/overlay.py` | Workspace entities for unreleased devices |
| `units/` | Generated knowledge units (all draft). `units/cda-skills` and `units/cda-routes` come from a checkout of the extension: `CDA=<checkout> scripts/rebuild.sh`. `units/docs/<source>` from `sources/docs.yml`; `units/docs-ccbysa/<source>` is built but left out of the index unless `CCBYSA=1` |
| `build/` | `entities/*.jsonl` (tracked); the indexes `knowledge*.db` are built, never tracked |
| `tests/` | `test_kb.py` and fixtures (incl. a workspace with a local DFP and a docs-only device). `golden.json`: 58 questions and tool outputs with the units that answer them; `node tests/eval_search.js build/knowledge.db <CDA checkout>` runs them through the extension's own search and prints hit@1, hit@5 and MRR |
| `scripts/` | `setup.sh`, `fetch_sources.py`, `rebuild.sh`, `build_core.sh` (the shipped core index), `build_split.sh` (the core without documentation plus a documentation pack) |
| `docs/design/` | Design documents 00 to 05 (German): concept and schema, migration findings, domains, source list with licenses, status |
| `docs/kickoff/` | Team kickoff deck (English) and its generator |

## Full rebuild from live sources

```bash
scripts/rebuild.sh            # 4 to 7 minutes; NO_VEC=1 skips the embeddings (about 3 minutes)
```

Fetches the Keil pack index and all active PDSC files (via the keil.com/pack mirror), clones cmsis-skills and devtools, clones the documentation sources into `.work/docs` (shallow, sparse for Zephyr, ExecuTorch, TF-M and the Learning Paths), runs the whole pipeline and the tests. `CCBYSA=1` adds the CC BY-SA documentation to the index. Inputs of the shipped build: cmsis-skills@25c2085, devtools@30f5e81, pack index of 4 Oct 2026.

## The shipped core index

The CMSIS Developer Assistant ships `resources/knowledge/core.db`. One script builds it, offline, from the committed units and `build/entities`:

```bash
scripts/build_core.sh [out]      # default build/knowledge.core.db; needs requirements-build.txt (PyYAML) and sqlite3
```

The recipe: `tools/check_licences.py` over the eight unit folders of the core (`units/skills`, `canonical`, `extracted`, `troubleshooting`, `cda-skills`, `cda-routes`, `docs`, `issues`); then `build_index.py --no-vec --recipe core --drop confidence=low,cause_origin=issue-digest` with `build/entities`, which leaves out the 54 issue digests the readers were least sure of until a human has reviewed them; then `tests/test_kb.py` against the result. `units/docs-ccbysa` and the book units never enter. The same commit gives the same index, and the index says which commit:

| `info` key | Value |
|---|---|
| `schema_version` | `1` |
| `built_at` | The commit time of HEAD when the inputs match the commit, so two builds of one commit agree; the build time otherwise |
| `kb_commit`, `kb_dirty` | The commit the units came from; `1` when a unit folder, `build/entities`, an exclusion list or `build_index.py` differed from it, untracked files included |
| `recipe` | `core` for `build_core.sh`; what `--recipe` says, else `custom` |
| `units`, `nodes`, `edges`, `dropped`, `drop` | Knowledge units, all nodes, edges, the units `--drop` left out and the rule |
| `license_<id>` | Units per licence: `Apache-2.0`, `MIT`, `BSD-3-Clause`, `own summary of a GitHub issue` |
| `embed_model` | Only in a build with vectors; the one key `kb_lib.py` reads |

The licence gate exits 1 and lists the files when a unit has no `license` field, a licence other than those four (CC BY-SA included) or `mode: P`; a folder without units fails as well, so a recipe cannot lose one unnoticed. Every converter writes the field.

`scripts/release_core.sh <version>` (version = the date, `2026.10.21`) publishes that index for the extension: it builds with `build_core.sh` at a clean, pushed HEAD, writes `build/knowledge-core-<version>.db`, its `.sha256` (`shasum -a 256` format) and `knowledge-core-<version>.json` (the `info` table plus `file`, `sha256`, `size`), and creates the GitHub release `core-<version>` with the three assets and notes that name the unit count, the licence counts and the commit. The extension pins a release in `resources/knowledge/core.lock.json` (`npm run knowledge:update -- <version>`) and `npm run knowledge:fetch` downloads it before packaging, hash checked.

## Licensing of content

Code in `tools/` and `scripts/`: licence to be decided (HANDOVER.md, decision 6); all rights reserved until then. Generated units carry `source`, `license` and `mode` in their frontmatter. The default index is derived from Apache-2.0, MIT and BSD-3-Clause sources only (cmsis-skills, devtools, Open-CMSIS-Pack PDSC metadata, and the documentation in `sources/docs.yml`, each unit with its own `license`, enforced by `tools/check_licences.py` on every core build). The CC BY-SA 4.0 documentation (FreeRTOS Kernel Book, Arm Learning Paths and install guides, the Arm ABI documents, Memfault's Interrupt blog) is converted into `units/docs-ccbysa` but stays out of the default index until the legal review (HANDOVER.md, decision 4); `build/knowledge.ccbysa.db` is a local build with it. Issue digests (`units/issues`) are own summaries with a link to the thread (mode S). Repositories without a licence file, such as the CMSIS Solution extension's documentation, are not used. `docs/design/04_quellenliste.md` lists further sources per domain with mode V (full text), S (own summary + link) or R (reference only); Arm documents, Keil KB and Learning Paths (CC BY-SA 4.0) need legal review before use.
