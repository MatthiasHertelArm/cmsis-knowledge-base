---
id: "pyocd-adding-a-new-built-in-target"
type: "concept"
domain: "debug"
title: "Adding a new built-in target"
summary: "This guide describes how to manually add support for a new target and/or board to pyOCD. In most cases you do not need to add a builtin target anymore, and can use pyOCD's support for CMSIS Device Family Packs."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/adding_new_targets.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/adding_new_targets.md"
license: "Apache-2.0"
mode: "V"
---

This guide describes how to manually add support for a new target and/or board to pyOCD. In most
cases you do not need to add a builtin target anymore, and can use pyOCD's support for CMSIS
Device Family Packs.

For background information, review the [architecture overview]({% link _docs/architecture.md %}) document first. The
[CMSIS Pack documentation](https://arm-software.github.io/CMSIS_5/Pack/html/index.html) may also be helpful.
