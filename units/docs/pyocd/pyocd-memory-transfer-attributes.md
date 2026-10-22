---
id: "pyocd-memory-transfer-attributes"
type: "concept"
domain: "debug"
title: "Memory transfer attributes"
summary: "By default, pyOCD (and most other debuggers) will show the current memory contents regardless of the presence of a data and/or instruction cache. Yet, sometimes it is desirable to view the cache contents in the debugger."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/memory_attributes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/memory_attributes.md"
license: "Apache-2.0"
mode: "V"
---

By default, pyOCD (and most other debuggers) will show the current memory contents regardless of the presence of a data and/or instruction cache. Yet, sometimes it is desirable to view the cache contents in the debugger. That is, to see the CPU's view of memory through the cache. Other memory transfer attributes can also be useful to control is certain, complex debugging scenarios.
