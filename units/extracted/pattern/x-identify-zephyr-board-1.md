---
id: "x-identify-zephyr-board-1"
type: "pattern"
domain: "project"
title: "Query the installed Zephyr board catalog with west"
status: "draft"
extracted_from: "proc-identify-zephyr-board"
source: "project/identify-zephyr-board/SKILL.md"
---

From the verified Zephyr workspace, run the venv-local `west boards` command. Treat this version-matched catalog, generated from the installed `board.yml` files, as authoritative for the installed Zephyr version.

Find candidates with `west boards --fuzzy-match "<candidate>"`. Normalize punctuation and capitalization only for searching; do not confirm a fuzzy result without checking its metadata.

For each candidate, run:

west boards --board <board-name> --cmakeformat "{NAME}|{VENDOR}|{SOCS}|{QUALIFIERS}|{REVISION_DEFAULT}|{REVISIONS}|{DIR}"
