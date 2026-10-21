---
id: "x-add-board-layer-2"
type: "concept"
domain: "project"
title: "Enable only the I-cache during bring-up"
status: "draft"
extracted_from: "proc-add-board-layer"
source: "add-board-layer/SKILL.md"
license: "Apache-2.0"
---

During bring-up enable **I-cache only**; a write-back D-cache makes halted-mode debugger reads stale and poisons the very validation you are about to do.
