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

## Update 5 Oct 2026, evening: share-alike sources as a separate build; vectors measured

| Item | State |
|---|---|
| CC BY-SA collection | 2,203 units in `units/docs-ccbysa`: Memfault's Interrupt blog 1,127 (Cortex-M faults, GDB, linker scripts, build systems, Zephyr; link roundups, Linux, Python, Rust and Memfault-product posts left out), Arm Learning Paths 819, install guides 77, FreeRTOS Kernel Book 132, AAPCS32 and semihosting 48 |
| Second build | `build/knowledge.ccbysa.db` (87 MB, git-ignored) holds the default units plus the share-alike ones, for trying them before decision 4: point `knowledge.indexPath` at it. On the golden set it scores lower (hit@1 0.60, MRR 0.733) because its units answer the same questions as the expected ones, often well (the Interrupt HardFault article, the TF-M learning path); the golden set has no question aimed at them yet |
| Vectors | `tests/eval_search.py` runs the golden set through the prototype search with and without embeddings: BM25 alone hit@1 0.62, MRR 0.749; with vectors 0.62, 0.727. So the extension's BM25-only search loses nothing today; embeddings are not worth an ONNX runtime in the extension yet |

## Update 5 Oct 2026, last: adapters, middleware, small repositories, browser

| Item | State |
|---|---|
| Debug adapters | `tools/adapters2ku.py`: one unit per adapter of the debug adapter registry (13): the names `debugger: name:` accepts, the defaults cbuild writes into cbuild-run.yml, the options the CMSIS Solution extension offers |
| Documentation | 47 sources: ThreadX middleware (FileX, USBX, NetX Duo, LevelX, TraceX, Modules; descriptive chapters only, the service chapters would have added 2,000 units), the debug adapter registry README, and nine small Open-CMSIS-Pack repositories as one collection `ocp-tools-readmes` (trace setup, RefApp framework layers, taxonomy, sensor example, scalable-software workshop, cbuild, vidx2pidx) |
| Index | 6,346 knowledge units, 72 MB |
| Golden set | 68 queries: hit@1 0.60  hit@5 0.91  MRR 0.742  failures 0 |
| Extension (pr/2.7.0-knowledge, uncommitted) | Search: question words out of BM25, procedure prior 0.001, none for routing units, exact messages ordered by line. Browser: filter and overview by collection. 1138 unit tests pass; installed locally as 2.5.10 (needs a window reload) |

## Update 5 Oct 2026, close: every issue digest checked against its thread

A check of 80 digests found that the readers had added things: invented versions and dates, extra
workarounds, "fixed in release" where the thread only shows a pull request, guesses stated as fact.
So all 583 were checked by seven more readers after `stage2/issues_qa_prompt.md`
(`stage2/issues-qa/*.json`): supported 265, partly 293, unsupported 25; six symptom lines were not
in the thread. `issues2ku.py` applies the results: the corrected cause, fix, versions and resolution,
"The thread gives no confirmed fix" where it has none, symptoms dropped when not in the thread, three
digests dropped, and `checked` in each unit. One reader had also put a wrong issue number on a
digest; `issues2ku.py` now skips a URL that is not among the threads the readers got. Result: 580
issue units, confidence high 159, medium 367, low 54.

More documentation in this last round: Zephyr board pages of 30 boards that also have a CMSIS board
pack (overview, hardware, programming and debugging; the board name from the `zephyr:board`
directive is the page title), CMSIS-Ethos-U, littlefs, the Mbed TLS knowledge base, and READMEs of
smaller ARM-software repositories.

| Item | State |
|---|---|
| Index | 7,117 knowledge units (with the devtools READMEs, the ctrace design notes, and Zephyr's debugging, TF-M and power-management services), 77.5 MB, lint clean, kb tests green |
| Golden set | 72 queries: hit@1 0.60, hit@5 0.90, MRR 0.741 (pages without a title now carry the source name, e.g. "littlefs DESIGN") |
| Review lists | `messages-to-review.csv` (397 error catalog units), `issues-to-review.csv` (580 issue digests, unsupported first) |

Open: a human review of the issue digests, starting with `checked: unsupported` and `confidence:
low`; the error catalog's review list; decision 4 for the share-alike sources; an agent-task
benchmark (HANDOVER next steps, level 2).

## Update 9 Oct 2026: a second local pack with the content of books (test scenario)

`tools/pdf2ku.py` turns the PDF books of a folder into knowledge units, one per section of the
book's outline (chapter intro, sections, sub-headings as split points above 12,000 characters;
running headers, page numbers, index anchors and Packt's promotion boxes dropped; cover, index,
advertising skipped). It handles the three outline shapes Packt uses. `scripts/build_books.sh`
converts `~/Documents/C++` (20 books, 4,177 units), builds `packs/Local.CPP_Books/knowledge.db`
(70 MB, entities pruned as in `build_split.sh`) and copies the pack into
`~/.cache/arm/packs/Local/CPP_Books/1.0.0/`, where the extension found it at once (next to
`Local::CMSIS_Knowledge@1.0.0`). Units carry `domain: cpp`, `collection: <book>`, `book`,
`chapter`, `source: <file>#page=N` and `mode: P` (private): the books are copyrighted, so
`units/books/` and the pack's index are git-ignored and must never reach a published index or pack.

Observation: without a `domain` filter the book units compete with the core index on general
questions (a `std::map` query ranks an issue digest first); with `domain: cpp` the ranking is clean.

## Update 10 Oct 2026: stage 3 for books, pilot on the bare-metal book

The book units of 9 Oct were all `concept` with the section's first sentence as summary.
`tools/stage3_books.py` with `stage2/books_prompt.md` refines them one unit at a time with a small
model (Claude Haiku 5.5): stage A (no model) strips Packt's promotion boxes, reattaches list numbers
and marks boilerplate sections with a `role`; stage B asks for type with the fields of that type,
a 40-word summary, triggers, the body as Markdown, up to three verbatim extracts and `applies_to`
from fixed lists; stage D (no model) checks every answer before it enters a unit: the Markdown body
may add at most 2 % new words and lose at most 10 % (figure captions excepted), extracts must be
verbatim and at least 160 characters, types, domains and `applies_to` values come from the lists,
a failed field falls back to the input and is listed in `report.csv`. `prepare` writes batch files
that either reader agents (as for the issue digests) or the Message Batches API (`submit`/`fetch`,
needs `ANTHROPIC_API_KEY`, none on this Mac) answer; `merge` writes `units/books-refined/<book>`,
which `scripts/build_books.sh` prefers over `units/books/<book>`.

Pilot, Bare-Metal Embedded C Programming, eight Haiku reader agents, 154 units: 28 dropped (all
chapter summaries and intros, the requirements lists, advertising), 29 procedures with steps, 5
patterns, 10 rules, the rest concepts; 37 extracts kept; confidence high 72, medium 36, low 18;
the body gate rejected 2 bodies (6 % and 2 % new words). `applies_to` was set on 4 units only
(Cortex-M4, GCC, gdb): the book names STM32F411, which is no entity of the core index.
Golden set `tests/golden-books.json` (12 questions, `tests/eval_search.py --golden=`), BM25 on the
pack: hit@1 0.50 → 0.67, MRR 0.722 → 0.792, hit@5 1.00 both. Open: the readers drop chapter intros
and summaries, which answer broad questions well (decide: keep with `role`, down-weighted);
stage C (relations) is not built; the C++ books are not refined.

Later the same day: chapter intros and summaries are kept (`role: intro | summary | preface`), the
readers rewrote their summaries and triggers in a second pass (`prepare --roles=intro,summary,preface
--first=9`), and the publisher footer whose URL wraps onto a second line is stripped too. With real
summaries the overviews outranked the sections (MRR 0.660), so the prototype search scales an
overview unit's score by `OVERVIEW_WEIGHT` (0.6, `tools/kb_lib.py`): MRR 0.812, hit@1 0.67, the
weight is not sensitive between 0.4 and 0.8. The extension's search (`src/core/knowledge/search.ts`
on pr/2.7.0-knowledge) does not have this weight yet; until it does, agents see the overviews first
on broad questions. 154 units: 3 dropped, 29 procedures, 2 patterns, 31 extracts.

## Update 10 Oct 2026, later: generic knowledge out of the book, checked against the core

`tools/books_generic.py` with `stage2/books_generic_prompt.md` and `stage2/books_conflict_prompt.md`:
two Haiku passes. Pass 1 reads the refined sections and writes pieces that hold beyond the book, in
own words (mode S), each with a verbatim `evidence` quote; `extract-merge` discards a piece whose
quote is not in its source unit, whose summary or body is outside the limits, or that repeats an
earlier piece of the book (title or title-plus-summary words, Jaccard 0.5 without stop words: the
same rule had come three times under three titles). Pass 2 takes, per piece, the five nearest units
of `build/knowledge.core.db` and the CMSIS_Knowledge pack (BM25) and has a judge mark each as
duplicate, contradicts, complements or unrelated; `check-merge` writes kept pieces to
`units/books-generic/<book>` with `references` to the complemented core units, drops duplicates and
puts contradictions into `stage2/books-review/<book>`. `build_index.py --known <db>` accepts those
cross-index edge targets, and `build_books.sh` keeps them through the entity prune.

Bare-metal book: 225 pieces written, 215 kept (128 concept, 36 rule, 27 procedure, 22 pattern,
2 troubleshooting; 10 repeats), 3 evidence quotes rejected in the readers' own checks before
output. Conflict check: 215 keep, 0 duplicate, 0 contradiction, 182 complement links to 107 core
units. The judges all say the same thing: the BM25 candidates are mostly unrelated (pyOCD issues,
svdconv messages), because the core index has little on register-level programming, so the check
proves the absence of obvious duplicates, not of contradictions; a vector search or a domain filter
on the candidates would make it sharper. Several complement links are loose (the RTC crystal piece
references two Zephyr board pages). Golden set, extended with the generic and chapter-level units
that answer its questions: hit@1 0.75, hit@5 1.00, MRR 0.875. The extension's `knowledge_expand`
follows a `references` edge into the core but shows the target's id only, not its title.

## Update 10 Oct 2026, evening: conflicts on the request side; scope ban on tool and project knowledge

**Request-side conflict test.** `tests/eval_conflicts.py` reads the core index, the documentation pack
and a candidate pack as one set the way the extension does (BM25 lists fused by rank) and runs the
72 golden CMSIS questions and 40 generic agent requests (`tests/agent-requests.json`: new project,
build, flash, debug, startup file, drivers, interrupts, low power ...). It reports shadowing (the
expected core unit outranked by a pack unit) and exposure (pack units in the top 8), and writes
judge batches (`stage2/books_request_conflict_prompt.md`: contradicts / diverts / complements /
unrelated per pack unit, decision fine / demote / exclude per request). Ten Haiku judges on the
unfiltered book pack: 109 requests with pack units in the top 8, 63 fine, 23 demote, 23 exclude;
31 contradictions, almost all from three units that start OpenOCD or a GDB server by hand or
build with a Makefile, and 35 diversions (IDE clicks, vendor headers by hand, register code where
the core has a driver API). `books_generic.py request-merge` applies such judgements (exclusion
list, `caution` in the frontmatter); it is kept as a tool but superseded by the scope ban below.

**Structural finding.** Rank fusion with equal lists puts every index's top two hits into the set's
top 8 whatever their relevance: on the unfiltered pack a book unit appeared in the top 8 for 69 of
72 CMSIS questions and all 40 generic requests ("add a board layer" brought a Logstash chapter). A
weight on the pack's ranks is useless in RRF (0.7 removes the pack entirely). A relevance gate
works: admit a pack hit only when its BM25 score reaches a share of the base indexes' best score
for the query (`--gate`): at 0.7, exposure on CMSIS questions 69 → 11, shadowing 28 → 6, MRR of
the golden set 0.484 → 0.494 (0.498 without the pack), the book questions still reach their units
(6 of 9 in the top 5, unchanged), generic requests still get pack units where the pack has
something (34 of 40). Recommendation for the extension's `KnowledgeSet`: this gate, 0.7.

**Scope ban (decision of 10 Oct).** Books contribute coding and design knowledge only; tool usage
and project management stay out. `books_generic.py classify-prepare / classify-merge` with
`stage2/books_scope_prompt.md`: 15 Haiku readers classified all 4,388 book units (refined and
generic units of the bare-metal book, raw units of the other 19) as coding 2,336, design 806,
tool 518, project 679, other 49; the 1,246 banned ids are in `stage2/books-exclusions.json`,
which `build_index.py --exclude` and both merges honour. The CMake books lose almost everything
(Modern CMake 22 of 262 kept, CMake Best Practices 1 of 190); the bare-metal book keeps 336 of
397. The pack now holds 3,142 units; the book golden set (9 questions left after the tool-usage
ones were dropped) hit@1 0.67, hit@5 1.00, MRR 0.833. With the scope ban the contradictions are
gone (the OpenOCD, GDB-server, Makefile and IDE units are `tool` or `project`); the exposure of
unrelated coding units on CMSIS requests remains until the gate is in the extension.

## Update 10 Oct 2026, night: the bare-metal book parked; a pack from "Software Architecture with C++"

Decision: the bare-metal book overlaps too much with the modern CMSIS practice (own startup file,
register code where a driver API exists, hand-run toolchain), so it is parked: its units stay under
`units/books*`, `Local.CPP_Books` is removed from the pack root and not loaded. The new pack
`Local.CPP_Architecture` holds one book, "Software Architecture with C++, Second Edition" (460
sections): stage 3 refinement, generic design knowledge in own words, conflict check against the
core, scope ban (310 of its raw units were coding or design, 150 tool or project), built by
`scripts/build_pack.sh CPP_Architecture softwarearchitecturewithcplusplusseconde`.

Result, same night. `Local::CPP_Architecture@1.0.0`, 713 units: 323 concepts, 225 rules, 153 patterns,
8 procedures, 4 troubleshooting. Pipeline: 19 Haiku readers refined the 460 sections (two readers
declined to reproduce the full text and delivered type, summary and triggers only; the merge keeps
the source text as body in that case, as it does for the 12 condensed bodies the gate rejected);
13 readers extracted 560 generic pieces in own words with evidence quotes (555 kept, 5 repeats);
19 judges checked them against the core (555 keep, 0 duplicate, 0 contradiction; the candidates
are almost all unrelated, the core has no generic C++ or architecture units); 3 readers classified
all 957 units with the tightened scope prompt (infrastructure products are `tool`): design 400,
coding 313, tool 227, project 17, so 244 units left the pack. Golden set
`tests/golden-architecture.json` (16 design questions; the generic units that answer them count):
hit@1 0.94, hit@5 1.00, MRR 0.969 on the pack alone. Request side (`tests/eval_conflicts.py
--gate=0.7 --book-golden=tests/golden-architecture.json`): pack unit in the top 8 for 5 of 72 CMSIS
questions (69 without the gate), the expected core unit outranked for 2, golden MRR 0.498 → 0.497;
15 of 16 design questions still reach their pack unit through the set; 12 of 40 generic agent
requests get a pack unit. The extension lists the pack and answers a factory-function question with
the book's rule, behind two word-overlap hits of the core, which is the ungated merge at work.

## Update 21 Oct 2026: the shipped index reproducible from a commit; repository on GitHub

The CMSIS Developer Assistant 2.7.0 ships `build/knowledge.core.db` of 16 Oct 13:05 (65 413 120 bytes, sha256
`a54734078376e95f22926b4862abfa80dba5f376d012d11bbd96dc954253e3e9`, 7 064 units, 33 994 nodes) as its core index.
That file came from an uncommitted working tree. This update makes it reproducible.

| Item | State |
|---|---|
| Open work committed | By kind: `e04f87e` ignore rules, `build/knowledge.db` no longer tracked (it was about 70 MB per version; the old versions stay in the history, nothing was rewritten); `390c41a` tools (`build_index --exclude/--known`, the overview weight, `route_refs`, the book tools); `8f43b36` scripts; `e406a2d` units (the extension's skills re-converted, `proc-start-cmsis-project`, routes, hand-overs as unit links); `cae1a7b` tests and evaluation data; `6f6c984` HANDOVER and README of 9 and 10 Oct. One hunk was dropped: `units/skills/graph.json` had a path of this machine in one `portability` field; the procedure file and the index never had it |
| Left uncommitted | `stage2/books-exclusions.json`: 1 490 unit ids, each with the classifier's reason in at most ten words. The reasons name a section's topic, nothing more, but they are not ids alone, so the file waits for a decision. `scripts/build_pack.sh` and `build_books.sh` treat it as optional |
| Licence gate | `tools/check_licences.py` (`cf13385`): every unit declares `license`, allowed are Apache-2.0, MIT, BSD-3-Clause and the issue digests' marker `own summary of a GitHub issue`; anything else, a missing field and `mode: P` fail with the files listed. The 227 units from cmsis-skills and the extension's skills (procedures, rules, concepts, canonical rules, extracted units, routes) had no field; the converters write it now and the files carry it. Over the eight core folders: 7 118 units, Apache-2.0 5 023, MIT 1 022, BSD-3-Clause 493, own summary 580 |
| `info` table | `build_index.py` (`6ee7cbb`) writes it into every index: `schema_version`, `built_at` (the commit time of HEAD while the inputs match the commit, else the build time), `kb_commit`, `kb_dirty`, `recipe`, `units`, `nodes`, `edges`, `dropped`, `drop`, `license_<id>`, and `embed_model` with vectors. `kb_lib.py` reads `embed_model` alone; the extension ignores the table |
| Recipe | `scripts/build_core.sh`: the gate, then `build_index.py --no-vec --recipe core --drop confidence=low,cause_origin=issue-digest` over `units/skills`, `canonical`, `extracted`, `troubleshooting`, `cda-skills`, `cda-routes`, `docs`, `issues` with `build/entities`, then `tests/test_kb.py` on the result; about 10 s, offline, `requirements-build.txt` pins PyYAML 6.0.3. The `--drop` step is what the 16 Oct build had done without a script: the 54 issue digests with `confidence: low` were absent from it, while the 24 low-confidence error-catalog units were in |
| Comparison with the shipped file | Built at `6ee7cbb`: nodes 33 994 with the same counts per kind and type, edges 91 014, `unresolved` 77, FTS rows 7 064. The ordered dumps of nodes (id, kind, type, domain, title, summary, body), edges and `unresolved` hash identically to the shipped file. Differences: `meta` of the 227 units now holds `license`, and the `info` table exists. The new file: 65 429 504 bytes, sha256 `d2bbf54d7eeeb1af4d5c559b350b2638a4b07c64360c1e554371ef452d7d33d8`, `built_at` 2026-10-21T10:35:00+02:00, `kb_dirty` 0. A second build of the same commit is byte-identical; a build at a later commit that changes no input differs in `built_at` and `kb_commit` only |
| Remote | Private repository `MatthiasHertelArm/cmsis-knowledge-base` on GitHub, branch `master`, pushed this day. The book units, the packs and `.work` are ignored and were never tracked |
| Release | `scripts/release_core.sh <version>` builds at a clean, pushed HEAD and publishes `knowledge-core-<version>.db`, `.sha256` and `.json` (the `info` table plus file, hash, size) as the GitHub release `core-<version>`; the extension pins one in `resources/knowledge/core.lock.json` and fetches it with `npm run knowledge:fetch` |

Next: let the extension's CI fetch `knowledge.core.db` by commit and sha256 instead of a local copy; review the 54
low-confidence digests, then drop the `--drop` step; decide on `stage2/books-exclusions.json`.
