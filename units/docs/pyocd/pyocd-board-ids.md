---
id: "pyocd-board-ids"
type: "concept"
domain: "debug"
title: "Board IDs"
summary: "New CMSIS-DAP firmware releases should use the CMSIS-DAP v2.1 board and target identification features rather than board IDs."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/developer/board_ids.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/developer/board_ids.md"
license: "Apache-2.0"
mode: "V"
---

New CMSIS-DAP firmware releases should use the CMSIS-DAP v2.1 board and target identification features
rather than board IDs.


This page documents the board IDs reported by certain [debug probes]({% link _docs/debug_probes.md %}) with which pyOCD can automatically identify a board and its target type.
