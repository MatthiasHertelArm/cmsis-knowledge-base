---
id: "pyocd-debug-probes-auto-target-type-identification"
type: "concept"
domain: "debug"
title: "Debug probes: Auto target type identification"
summary: "Certain types of on-board debug probes can report the type of the target to which they are connected."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/debug_probes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/debug_probes.md#auto-target-type-identification"
license: "Apache-2.0"
mode: "V"
---

Certain types of on-board debug probes can report the type of the target to which they are connected.

Debug probes that support automatic target type reporting:

- CMSIS-DAP probes supporting v2.1 of the protocol and reporting target type info
- CMSIS-DAP probes based on the DAPLink firmware
- STLinkV2-1 and STLinkV3
