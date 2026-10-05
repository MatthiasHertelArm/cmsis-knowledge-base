---
id: "devt-ctrace-architecture"
type: "concept"
domain: "trace"
title: "ctrace Architecture"
summary: "This document describes the internal structure of ctrace, the runtime data flow, and the intended extension points. For command-line usage and build instructions, see the project README. The verified constraints record preserved contracts; the compact TODO list tracks remaining work."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md"
license: "Apache-2.0"
mode: "V"
---

This document describes the internal structure of `ctrace`, the runtime data flow, and the intended extension points.
For command-line usage and build instructions, see the [project README](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/../README.md). The [verified
constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md) record preserved contracts; the compact [TODO list](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/todo.md) tracks remaining work.
The [multi-source design record](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md) explains the migration from single-source SWO to routed
CoreSight input and the decisions behind the current structure.

(figure: ctrace architecture)
