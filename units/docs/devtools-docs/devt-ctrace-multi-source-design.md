---
id: "devt-ctrace-multi-source-design"
type: "concept"
domain: "trace"
title: "ctrace multi-source design"
summary: "This record explains the September 2026 migration from a single unformatted ITM input to formatted CoreSight input with multiple Trace Bus IDs. It preserves the design decisions and migration strategy from the original implementation plan."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md"
license: "Apache-2.0"
mode: "V"
---

This record explains the September 2026 migration from a single unformatted ITM input to formatted CoreSight input
with multiple Trace Bus IDs. It preserves the design decisions and migration strategy from the original implementation
plan. Current behavior is defined by the [architecture](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md), [constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md), and
[CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/ctf-format.md); later changes to the original assumptions are summarized below.
