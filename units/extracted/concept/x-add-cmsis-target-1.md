---
id: "x-add-cmsis-target-1"
type: "concept"
domain: "project"
title: "Evidence that a CMSIS target uses a board layer"
status: "draft"
extracted_from: "proc-add-cmsis-target"
source: "project/add-cmsis-target/SKILL.md"
---

Evidence includes a project `layers:` entry of `type: Board`, a variable reference such as `$Board-Layer$`, or target-specific variables that bind that reference to a `*.clayer.yml` file. Do not infer a board-layer requirement merely from a directory named `Board`.
