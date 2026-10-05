---
id: "devt-ctrace-architecture-design-history"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Design history"
summary: "The initial ctrace import introduced the pre-TB architecture and constraints on 2026-07-30. The multi-source design record describes the subsequent migration to a shared DecodeTree, route-local recovery, and multi-stream output."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#design-history"
license: "Apache-2.0"
mode: "V"
---

The [initial ctrace import](https://github.com/Open-CMSIS-Pack/devtools/commit/772c7911e61b8066f09c5cfbfe03fe4fc0ee021e)
introduced the pre-TB architecture and constraints on 2026-07-30. The [multi-source design record](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md)
describes the subsequent migration to a shared DecodeTree, route-local recovery, and multi-stream output. It links
the original planning history and distinguishes later contract changes; the live architecture, constraints, and CTF
profile remain the current implementation references.
