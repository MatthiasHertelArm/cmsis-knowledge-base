# CMSIS Knowledge Base for the CMSIS Developer Assistant (prototype)

A knowledge base with a small knowledge graph that adds the *how, when and why* to the *what* of the CMSIS Pack Docs. It is served to coding agents through three MCP tools and is built to work with small local models: summaries first, full text only on request.

Status: working prototype. All knowledge units are `status: draft`. See [HANDOVER.md](HANDOVER.md) for the current build, decisions, known issues and open points.

## Quick start (5 minutes)

```bash
scripts/setup.sh                       # venv + dependencies
. .venv/bin/activate
scripts/build_core.sh                  # the core index in about 10 s: licence gate, build/knowledge.core.db, tests
python tools/kb_server.py build/knowledge.core.db   # MCP server on stdio
```

The agents reach the knowledge through the CMSIS Developer Assistant's MCP tools; this repository no longer ships agent configuration files.

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

Examples with real data: `units/troubleshooting/ts-packchk-m302.md`, `units/skills/procedure/proc-generate-debug-sequences.md`, `units/skills/rule/rule-no-fabrication-generate-debug-sequences.md`.

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
| `tools/issues2ku.py` | Digests of GitHub issues and answered discussions (`stage2/issues-out`, written after `stage2/issues_prompt.md`) → troubleshooting units in `units/issues/<repo>`: own words, mode S, a link to the thread, tool output as the only verbatim text |
| `scripts/build_pack.sh` | One local pack from named book collections (refined units preferred, generic units included, scope exclusions applied, edges into the core allowed), installed into the pack root: `scripts/build_pack.sh CPP_Architecture softwarearchitecturewithcplusplusseconde` |
| `tools/pdf2ku.py`, `scripts/build_books.sh` | Test scenario for pack-carried knowledge: books in PDF form (poppler's `pdftohtml` outline and `pdftotext`) → one concept unit per section into `units/books/<book>`, built into the local pack `packs/Local.CPP_Books` and copied into the pack root (`Local/CPP_Books/<version>/`). The books are copyrighted: units and index are git-ignored and never part of `build/knowledge*.db` |
| `tools/stage3_books.py`, `tools/books_generic.py` | Stage 3 for the books (Claude Haiku 5.5 as reader agents or through the Message Batches API): type, summary, triggers and Markdown per section, every answer gated by a script (`stage2/books_prompt.md`); then generic knowledge in own words with a verbatim evidence quote, checked against the core indexes for duplicates and contradictions (`stage2/books_generic_prompt.md`, `stage2/books_conflict_prompt.md`), into `units/books-refined` and `units/books-generic`; `classify-*` with `stage2/books_scope_prompt.md` keeps coding and design knowledge only (`stage2/books-exclusions.json`, read by `build_index.py --exclude`). `tests/eval_conflicts.py` measures what an agent gets for CMSIS and generic requests once a pack is read next to the core |
| `sources/docs.yml`, `sources/docs-ccbysa.yml` | The documentation sources, their licence, domain and published URL; the second holds the CC BY-SA ones |
| `sources/licenses.yml` | Per repository the units come from: the licence identifier read from its licence file, the file's name, its copyright lines, its NOTICE text; written by `tools/sources_md.py --fetch`, read by every build |
| `tools/build_index.py` | Lint, resolve `applies_to`, FTS5, sqlite-vec, edges, the `info` table → `knowledge.db`; `--drop`, `--exclude` and `--known` shape a build |
| `tools/check_licences.py` | The licence gate: every unit of the given folders declares an allowed licence and none is `mode: P` |
| `tools/sources_md.py` | `SOURCES.md` of an index: every source with repository, licence and what was taken, the copyright lines and licence texts of the MIT and BSD-3-Clause sources, the NOTICE files of the Apache-2.0 ones, the issue repositories |
| `tools/kb_lib.py`, `tools/kb_server.py` | Retrieval and MCP server |
| `tools/overlay.py` | Workspace entities for unreleased devices |
| `units/` | Generated knowledge units (all draft). `units/cda-skills` and `units/cda-routes` come from a checkout of the extension: `CDA=<checkout> scripts/rebuild.sh`. `units/docs/<source>` from `sources/docs.yml`; `units/docs-ccbysa/<source>` is built but left out of the index unless `CCBYSA=1` |
| `build/` | `entities/*.jsonl` (tracked); the indexes `knowledge*.db` are built, never tracked |
| `tests/` | `test_kb.py` and fixtures (incl. a workspace with a local DFP and a docs-only device). `golden.json` holds questions and tool outputs with the units that answer them; `node tests/eval_search.js build/knowledge.db <CDA checkout>` runs them through the extension's own search and prints hit@1, hit@5 and MRR |
| `scripts/` | Setup, source fetch, rebuild, core and split builds, local pack builds and core release; see [docs/implementation.md](docs/implementation.md#scripts) for each script |
| `docs/README.md` | Index of the documentation, with the pipeline and the reading order |
| `docs/concept.md` | The concept: why the knowledge base exists, the node and edge types, applicability, retrieval, domains |
| `docs/implementation.md` | The implementation reference: unit frontmatter, entity ids, the tables of `knowledge.db`, the exchange files of the model stages, every script with its inputs and outputs, how a search runs |

## Full rebuild from live sources

```bash
scripts/rebuild.sh            # 4 to 7 minutes; NO_VEC=1 skips the embeddings (about 3 minutes)
```

Fetches the Keil pack index and all active PDSC files (via the keil.com/pack mirror), clones cmsis-skills and devtools, clones the documentation sources into `.work/docs` (shallow, sparse for Zephyr, ExecuTorch, TF-M and the Learning Paths), runs the whole pipeline and the tests. `CCBYSA=1` adds the CC BY-SA documentation to the index. Inputs of the shipped build: cmsis-skills@25c2085, devtools@30f5e81, pack index of 4 Oct 2026.

## Continuous integration

`.github/workflows/ci.yml` builds the core index from the committed units on every push and pull request
and gates it: the licence gate, `tests/test_kb.py`, the golden set (hit@5 at least 0.85, MRR at least
0.65). `rebuild.yml`, by hand or on the first of the month, runs `scripts/rebuild.sh` with the
model-assisted stages through the Claude API (`tools/model_run.py`, key in the `ANTHROPIC_KEY` secret;
only items whose input changed are sent, the manifests next to the `stage2/` folders say which) and
opens a pull request with the regenerated units and the review lists. `release.yml` publishes the core
index as a release for a version. Details in [docs/implementation.md](docs/implementation.md).

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

Next to the index the build writes `build/SOURCES.md`, the attribution of its content (`tools/sources_md.py`): what the index is and that every unit names its source and licence in its frontmatter; a table of every source with repository link, licence and what was taken (skills, tool messages, documentation, issue digests in own words) and the unit count; for each MIT and BSD-3-Clause source its copyright lines and the full licence text (the SPDX text with the copyright lines of the repository's licence file); for the Apache-2.0 sources one reference block with the copyright lines their licence files carry and the text of every NOTICE file a source ships; and the issue repositories, whose digests are own summaries. The units are the authority for what is in (their `source`, `license`, `collection`), `sources/docs.yml` names the documentation sources, and `sources/licenses.yml` holds what was read from the licence files, so a clean checkout regenerates the file without network. A new repository among the sources needs `tools/sources_md.py --units … --fetch` once: it reads the licence and NOTICE files from the clone in `.work/docs`, else from GitHub (`gh` when logged in) or gitlab.arm.com, caches them under `.work/licenses/` and extends `sources/licenses.yml`; commit that file. `--refresh` reads every repository again. The script warns on stderr when a licence file cannot be identified, reads as another licence than the units declare, or an MIT or BSD source has no copyright line; it never guesses.

`scripts/release_core.sh <version>` (version = the date, `2026.10.21`) publishes that index for the extension: it builds with `build_core.sh` at a clean, pushed HEAD, writes `build/knowledge-core-<version>.db`, its `.sha256` (`shasum -a 256` format) and `knowledge-core-<version>.json` (the `info` table plus `file`, `sha256`, `size`), and creates the GitHub release `core-<version>` with those three assets, `SOURCES.md` as the fourth (its name and sha256 are in the JSON as `sources` and `sources_sha256`), and notes that name the unit count, the licence counts and the commit. The extension pins a release in `resources/knowledge/core.lock.json` (`npm run knowledge:update -- <version>`) and `npm run knowledge:fetch` downloads it before packaging, hash checked.

## Licensing of content

Code in `tools/` and `scripts/`: licence to be decided (HANDOVER.md, decision 6); all rights reserved until then. Generated units carry `source`, `license` and `mode` in their frontmatter. The default index is derived from Apache-2.0, MIT and BSD-3-Clause sources only (cmsis-skills, devtools, Open-CMSIS-Pack PDSC metadata, and the documentation in `sources/docs.yml`, each unit with its own `license`, enforced by `tools/check_licences.py` on every core build). The CC BY-SA 4.0 documentation (FreeRTOS Kernel Book, Arm Learning Paths and install guides, the Arm ABI documents, Memfault's Interrupt blog) is converted into `units/docs-ccbysa` but stays out of the default index until the legal review (HANDOVER.md, decision 4); `build/knowledge.ccbysa.db` is a local build with it. Issue digests (`units/issues`) are own summaries with a link to the thread (mode S). `build/SOURCES.md`, written by every core build, is the attribution of the shipped index: every source with its licence, the copyright lines and licence texts the MIT and BSD-3-Clause licences require, the NOTICE files of the Apache-2.0 sources; the extension ships it as `resources/knowledge/SOURCES.md`. Repositories without a licence file, such as the CMSIS Solution extension's documentation, are not used. `sources/docs.yml`, `sources/docs-ccbysa.yml` and `sources/sources-review.csv` record configured and reviewed sources; they do not contain the full future-source backlog from the former German design documents. That candidate list, including modes V (full text), S (own summary + link) and R (reference only), is archived in Git at `f1bb74ff:docs/design/04_quellenliste.md`. Arm documents, Keil KB and Learning Paths (CC BY-SA 4.0) need legal review before use.
