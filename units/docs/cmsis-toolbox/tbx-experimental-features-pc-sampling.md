---
id: "tbx-experimental-features-pc-sampling"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / PC Sampling"
summary: "The supported periods are the following discrete values:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#pc-sampling"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

DWT PC sampling uses two fields:

- `CYCTAP` selects bit 6 or bit 10 of `CYCCNT`.
- `POSTPRESET` provides a four-bit post-scaler reload value.

The supported periods are the following discrete values:

- `64 * (1..16)` processor cycles.
- `1024 * (1..16)` processor cycles.

PC sampling additionally requires:

- An implemented cycle counter, reported by `DWT_CTRL.NOCYCCNT == 0`.
- PC sampling support in the DWT implementation.
- An enabled cycle counter.
- A trace-capable DWT and ITM implementation.

The schema should validate the discrete supported values rather than accept an arbitrary cycle count.
