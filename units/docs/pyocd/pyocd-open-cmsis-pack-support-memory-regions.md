---
id: "pyocd-open-cmsis-pack-support-memory-regions"
type: "concept"
domain: "debug"
title: "Open-CMSIS-Pack support: Memory regions"
summary: "A Device Family Pack lists memory regions and contains the algorithms used to program flash memories."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/open_cmsis_pack_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/open_cmsis_pack_support.md#memory-regions"
license: "Apache-2.0"
mode: "V"
---

A Device Family Pack lists memory regions and contains the algorithms used to program flash memories.

### Flash algorithms

DFPs can specify whether a flash algorithm is default, that is, whether it should be used without user intervention. Some DFPs use the default flag to include more than one flash algorithm for a given memory region, usually multiple part numbers for external memories such as Quad or Octal SPI flash. PyOCD honours this flag, and only loads flash algorithms marked as default. It currently does not have a standard way to list and enable non-default flash algorithms. If required, a [user script]({% link _docs/user_scripts.md %}) can be used to add additional flash algorithms manually extracted from the DFP.

### Limitations

- DFPs can specify a memory region or flash algorithm to apply only to a specific CPU. However, pyOCD currently only supports a single system memory map for all CPUs. This can result in issues if conflicting or overlapping memory regions are defined for more than one CPU.
- PyOCD always runs flash algorithms from the first CPU, even if the DFP says the algorithm should apply to another CPU. On certain devices, this can result in the algorithm failing to run correctly.
- Flash algorithms are handled as a separate list in CMSIS-Packs, while in pyOCD the flash algorithms are associated with flash memory regions. If a DFP defines multiple algorithms with address ranges corresponding to a single region, only the first listed algorithm will be used. (At the time of this writing, there are no known DFPs with such a configuration.)
