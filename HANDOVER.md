# Handover to the CDA team

From: Matthias Hertel, Embedded Tools Integration. Date: 4 Oct 2026.

## Goal

Turn the skill-based RAG of the CMSIS Developer Assistant into a knowledge base with a knowledge graph. Pack Docs deliver the *what* (APIs, device facts), the knowledge base the *how, when, why* (procedures, rules, troubleshooting, domain knowledge such as RTOS, linker, fault analysis, optimization, test).

## Decisions already taken

1. Pack Docs = what, knowledge base = how, when, why. Join key: CMSIS entities from PDSC and csolution.
2. Knowledge units are Markdown with YAML frontmatter in Git. Types: concept, procedure, rule, pattern, troubleshooting.
3. Index: one SQLite file with FTS5, sqlite-vec and an edge table. No graph database.
4. Access through three MCP tools: `knowledge_search`, `knowledge_get`, `knowledge_expand`.
5. Existing skills become whole procedure nodes and are never shortened at retrieval.
6. Delivery as a CMSIS Pack with a `knowledge/` folder, so vendors can ship their own knowledge.
7. Must work with small local models: summaries first, full text on request.
8. New cores are maintained manually as entities (`kb-entities.yml`). No architecture layer.
9. Devices that only have documentation, or whose pack is assembled in a local repo, are covered by the workspace overlay.
10. Every unit traces back to a listed source or a named author. New units start as `status: draft`; only the domain owner sets `reviewed`.

## What is done

| Item | State |
|---|---|
| Entity graph | 26,903 entities from 1,485 of 1,493 active PDSC files |
| Skills migration, stage 1 | 24 procedures, 117 rules, 7 concepts, 6 artifacts, 45 requires edges. Whole skill body kept (145 kB) |
| Skills migration, stage 2 | Prompt v2 tested on 4 procedures; results merged |
| Error catalog | 397 troubleshooting units: packchk 121, svdconv 142, csolution 134. Cause/fix from READMEs for 214 |
| Index + MCP server | Search about 525 tokens per answer, 11 to 57 ms on CPU |
| Workspace overlay | Local DFPs, `local_repository.pidx`, `kb-entities.yml` |
| Tests | `tests/test_kb.py`, all green |

## Known issues

1. **csolution messages have no cause/fix.** 134 units carry the symptom and the triggering source line only. Example of how to fill them: `board mounted device STM32U585AIIx not found` was reproduced with CMSIS-Toolbox 2.12.0 when the STM32U5 DFP is not installed or `packs:` lists only the BSP.
2. **13 procedure summaries exceed 40 words.** They come from the skill descriptions. Stage 2 fixes this, but has only run on 4 of 24 procedures.
3. **`requires` edges mean "mentions".** Stage 1 creates them from any reference. One cycle exists (check-pyocd-availability, pyocd-detect-debug-topology). Stage 2 should type each mention.
4. **Message codes collide across tools** (M302 in packchk and svdconv). The tool context resolves it; agents should pass `tools`.
5. **No entity for NPUs** (Ethos-U55/U65/U85). Edge AI units cannot target them yet.
6. **Family IDs depend on the vendor name.** A different vendor spelling in a local PDSC and in `kb-entities.yml` creates two families. A CI check is advisable.
7. **Generic `Dcore` values** (ARMV8MML, ARMV8MBL) appear as cores. They are schema placeholders, not real cores.
8. **Three vendor PDSC files** (Geehy G32F031, G32M3101, G32R4xx) were not valid XML in the shipped build. A rebuild later the same day parsed all 1,488 active PDSC files, so counts differ slightly between builds.
9. Docs-only devices: their documents are linked, not full-text indexed. Full text belongs in the existing Pack Docs system.

## Open decisions

| # | Decision | Recommendation |
|---|---|---|
| 1 | Pilot domain | Error catalog: 397 units exist, easy to measure |
| 2 | Interface to the existing Pack Docs system (`packDocs.enabled`, skill `cmsis-pack-docs`) | Share DocSection IDs and project context |
| 3 | Canonical rules for stage 2 | Approve: no-fabrication, tone-and-style, portability, no-install, user-confirmation. The last two were derived from the test runs and need sign-off and hand-written text |
| 4 | Legal review | Keil KB export, Arm compiler guides, AN209, Learning Paths (CC BY-SA 4.0) |
| 5 | Domain maintainers | One owner per domain, MAINTAINERS file evaluated by CI |
| 6 | License of the tooling code | |

## Suggested next steps

1. Run stage 2 (prompt v2 in `stage2/decompose_prompt.md`) on the remaining 20 procedures; human review.
2. Benchmarks, in three levels:
   * **Retrieval** (every index build, blocks on regression): golden set of queries with expected unit IDs; Recall@5, MRR, exact-symptom hit rate, tokens per answer, wrongly filtered units. Generate queries by *fault injection*: take valid projects from csolution-examples / Arm-Examples, break them on purpose (remove a pack, misspell a device or component, drop a layer), run `csolution`/`cbuild`, and use the real output as query. The mutation defines the expected unit, and the same run yields cause and fix for the csolution units.
   * **Agent tasks** (nightly subset): broken project in a sandbox, agent must fix it; success is decided by the tools (`csolution convert` clean, `cbuild` passes, FVP test passes). Compare no help vs. today's skills vs. knowledge base, with a small local model and a frontier model. Measure success rate, tool calls, tokens, time. These numbers decide when skills can be retired.
   * **Real questions**: cmsis-toolbox and devtools issues (question + resolution), later opt-in CDA usage data.
3. Wire `knowledge.db` into the CDA behind a feature flag, parallel to the skills. Router skills (cmsis-project, cmsis-bring-up, cmsis-pack) only point to the tools.
4. Then the next domains from `docs/design/03_wissensdomaenen.md`, each with its own golden set.

## Contacts

Concept and decisions: Matthias Hertel. The design documents in `docs/design/` are in German; identifiers and code comments are partly German as well.

## Update 5 Oct 2026: feature parity with the skills of CDA 2.5

Added so that the knowledge tools can stand in for the skills the extension ships:

| Item | State |
|---|---|
| The extension's own skills | 7 procedures in `units/cda-skills` (add-board-layer, cmsis-bootstrap, cmsis-debug-live, cmsis-debugger-setup, cmsis-pack-docs, debugger-troubleshooting, fvp-debug-setup) and the concept cmsis-embedded-guide. Source stays in the extension repository |
| Files of a skill | 19 `asset` entities (templates, scripts) with the file as body, referenced by their procedure; not in the search index |
| Routing | 4 units `route-<domain>` in `units/cda-routes`, replacing the router skills |
| Index | 562 knowledge units; `build/knowledge.2026-10-04.db` is the build before this change |

Not done: cmsis-help has no unit; the three older own skills got a short description (`agents/openai.yaml`) in the extension so their summaries fit; the 13 long summaries of known issue 2 are unchanged. A stray pair of quotes in one summary (debug-access-knowledge) went away with the frontmatter fix. Building with embeddings needs a Python whose sqlite3 loads extensions: the python.org framework build does not, `uv venv --python 3.12` does.
