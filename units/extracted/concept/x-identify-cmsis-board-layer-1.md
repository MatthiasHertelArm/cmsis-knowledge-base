---
id: "x-identify-cmsis-board-layer-1"
type: "concept"
domain: "project"
title: "Compatibility checks for a packaged board-layer candidate"
status: "draft"
extracted_from: "proc-identify-cmsis-board-layer"
source: "project/identify-cmsis-board-layer/SKILL.md"
---

Start with only layers that `csolution` reports as compatible for the selected context. For each candidate, verify:
- `for-board:` or `for-device:` matches the exact target;
- its active `connections.provides` satisfies every applicable project or layer `connections.consumes` entry;
- any candidate `connections.consumes` requirements are also satisfied;
- the reported source pack version, `path`, `file`, and optional `copy-to` exist.

A matching board or device name alone is insufficient; the active required connections must also be satisfied.
