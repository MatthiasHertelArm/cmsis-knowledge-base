---
id: "tbx-experimental-features-dwt-synchronization"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / DWT Synchronization"
summary: "DWT synchronization is controlled through DWT_CTRL.SYNCTAP."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#dwt-synchronization"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

DWT synchronization is controlled through `DWT_CTRL.SYNCTAP`.

- Architecturally encoded periods are `16M`, `64M`, and `256M` processor cycles.
- All listed Cortex-M DWT implementations that support DWT trace provide a read/write `SYNCTAP` field.
- Processors or debug configurations marked as having no DWT trace cannot emit DWT synchronization packets and do not provide a functional `SYNCTAP` field.
- `SYNCTAP` selects the synchronization period; synchronization packet generation is enabled or disabled through `ITM_TCR.SYNCENA`.
- `DWT\0` should therefore disable DWT synchronization packets through `ITM_TCR.SYNCENA`, not attempt to encode zero in `SYNCTAP`.

For the listed Cortex-M processors, the configuration generator can treat DWT trace support as implying a writable `SYNCTAP`. It must still discover whether DWT trace and the associated ITM are implemented and accessible.
