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

1. **Message causes are unreviewed.** Since 5 Oct every message unit has a cause and fix read from the devtools source (see the update below), but none was reproduced with a tool run and none is reviewed. Example of how to confirm one: `board mounted device STM32U585AIIx not found` was reproduced with CMSIS-Toolbox 2.12.0 when the STM32U5 DFP is not installed or `packs:` lists only the BSP.
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

## Update 5 Oct 2026, evening: documentation and the message causes

| Item | State |
|---|---|
| Documentation | 4,415 concept units from 40 sources in `sources/docs.yml` (Apache-2.0 3,310, MIT 636, BSD-3-Clause 469): CMSIS-Toolbox, Open-CMSIS-Pack and SVD specifications, CMSIS-Core, -RTOS2, -Driver (API, implementations, validation), RTX, -View, -Compiler, -DSP, -NN, -Stream, -DAP, -FreeRTOS, -Zephyr, SDS, AVH, pyOCD, CMSIS Debugger, cpackget, gen-pack, csolution-examples, the extension's guides, ThreadX, Zephyr (kernel, devicetree, Kconfig, west, test, debug, logging, shell, Cortex-M), TF-M, MCUboot, Unity, CMock, Ceedling, TFLite Micro, ExecuTorch Arm backend, Vela, ML Embedded Evaluation Kit, LLVM Embedded Toolchain |
| CC BY-SA documentation | 1,076 units in `units/docs-ccbysa`: FreeRTOS Kernel Book 132, Arm Learning Paths for embedded 819 (Linux, container and cloud paths left out), install guides 77, AAPCS32 and semihosting 48. Not in the index; decision 4 |
| Message causes | 383 of 397 message units got cause, fix, evidence and a summary (the cause's first sentence) (file:line in devtools@30f5e817) from a reading of the source; confidence high 178, medium 181, low 24; 14 stay open (codes no code path raises). Units carry `cause_origin: source-analysis`, `confidence`, `evidence`, and `doc_cause` where the README text was replaced. The analysis also found misleading or dead messages; they are in the units' `## Note` |
| Review list | `messages-to-review.csv`, 397 rows, least certain first |
| Index | 4,977 knowledge units, 61.8 MB with embeddings; `build/knowledge.2026-10-05-1526.db` is the build before |
| Search | An exact message on an earlier line of tool output now ranks before one on a later line (the cause before "processing context failed"); the same rule is in the extension |

Golden set: `tests/golden.json`, 47 queries over all domains, run with `tests/eval_search.js` against the extension's search (BM25, no vectors). With it the extension's ranking was tuned: procedure prior halved, none for routing units, question words left out of BM25; hit@1 0.43 → 0.55, hit@5 0.89, MRR 0.643 → 0.713. Weak spots: wording that splits a term ("set up" for setup, "time stamp" for timestamp), and short units with many common words. The error catalog's titles now show the whole message; ids are unchanged.

## Update 5 Oct 2026, later: issues, stage 2 complete, more documentation

| Item | State |
|---|---|
| Issue digests | 583 troubleshooting units in `units/issues/<repo>` from closed issues (519), open issues with a workaround (64, marked open) and answered pyOCD discussions (11) of pyOCD 231, devtools 133, CMSIS Debugger 84, cmsis-toolbox 40, CMSIS Solution 36, cpackget 35, CMSIS_6 17, RTX 6, View 1. Read by eleven parallel readers after `stage2/issues_prompt.md`: title, cause and fix in own words (mode S, link to the thread), tool output as the only verbatim text, 242 with an exact-message pattern. Confidence high 291, medium 247, low 45. A check against the threads found no copied prose. Raw threads stay in `.work/issues` (not committed) |
| Stage 2 | Run on all 24 cmsis-skills procedures and the 7 of the extension (`stage2/out_v2`, `stage2/out_cda`): summaries within 40 words (lint errors 13 → 0), short triggers, verification, stop conditions; 48 procedure rules refined against the canonical ones; 64 extracted units. The skill description of stage 1 stays searchable (`description`, indexed with the triggers): without it the short triggers lost words such as HardFault, and the debug procedure fell out of the top ten |
| Documentation | 45 sources, 4,687 units: Zephyr board and SoC porting, getting started, tracing and pinctrl added; Arm-Examples with a licence: Helium optimization guide, SystemView, AVH VSI, CMSIS MLEK packs, Ethos-U integration |
| Index | 5,893 knowledge units, 67.6 MB with embeddings, lint clean |
| Golden set | 58 queries (11 aim at issue digests): hit@1 0.67, hit@5 0.91, MRR 0.789 |
| Title aliases | The index adds to each unit's trigger column the words of identifiers in its title (EventRecorderInitialize → Event Recorder Initialize, ARM_USART_Send → ARM USART Send) and the other spelling of a few compounds (setup / set up, timestamp / time stamp): MRR 0.760 → 0.789 |

Issue digests get no prior of their own: a negative one helped the documentation questions but hurt the issue questions more. Open points: older issues describe the cbuildgen era (CMSIS-Toolbox 1.x) and say so in `versions`; nothing removes them when a release makes them obsolete. The extracted units are not deduplicated yet; a few repeat each other (unclocked peripheral reads in three procedures).
