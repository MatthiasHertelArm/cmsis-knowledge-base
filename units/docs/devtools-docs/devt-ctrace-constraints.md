---
id: "devt-ctrace-constraints"
type: "concept"
domain: "trace"
title: "ctrace Constraints"
summary: "This document records contracts that implementation changes must preserve. Runtime design and the supported feature profile belong in the architecture description, working instructions in the README, and unfinished work in the TODO list."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md"
license: "Apache-2.0"
mode: "V"
---

This document records contracts that implementation changes must preserve. Runtime design and the supported feature
profile belong in the [architecture description](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md), working instructions in the [README](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/../README.md),
and unfinished work in the [TODO list](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/todo.md). The CMSIS-Toolbox [trace
specification](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#trace) remains authoritative for
standardized `*.ctrace-run.yml` fields. The `ctrace-run.trace-format` field described below is a ctrace-private,
temporary override, not a normative CMSIS-Toolbox field or a producer-emission requirement. Its standardization is
not assumed: the current [trace proposal](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/pull/699) keeps formatter
configuration with trace communication, separate from trace-source setup.
