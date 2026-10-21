---
id: "x-identify-cmsis-board-support-2"
type: "concept"
domain: "project"
title: "A CMSIS device identity is the exact Dname"
status: "draft"
extracted_from: "proc-identify-cmsis-board-support"
source: "project/identify-cmsis-board-support/SKILL.md"
license: "Apache-2.0"
---

Normalize and de-duplicate device candidates by exact CMSIS `Dname`. Multiple processor `Pname` entries belonging to the same `Dname` are one device identity unless the requested target must select a processor.
