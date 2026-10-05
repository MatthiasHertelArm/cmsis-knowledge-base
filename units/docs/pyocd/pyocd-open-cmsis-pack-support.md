---
id: "pyocd-open-cmsis-pack-support"
type: "concept"
domain: "debug"
title: "Open-CMSIS-Pack support"
summary: "PyOCD uses device descriptions from Open-CMSIS-Pack Device Family Packs (DFPs) as a primary method for supporting target types. See the target support documentation for how to install and select target types from DFPs."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/open_cmsis_pack_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/open_cmsis_pack_support.md"
license: "Apache-2.0"
mode: "V"
---

PyOCD uses device descriptions from [Open-CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html) Device Family Packs (DFPs) as a primary method for supporting target types. See the [target support documentation]({% link _docs/target_support.md %}) for how to install and select target types from DFPs.

There are three main components to DFP device descriptions used by pyOCD:

- Memory regions
- Debug description
- Debug access sequences
