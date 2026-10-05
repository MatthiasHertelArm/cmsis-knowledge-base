---
id: "tbx-experimental-features-dwt-events"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / DWT Events"
summary: "The DWT event selectors are not universally available."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#dwt-events"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

The DWT event selectors are not universally available.

- `CYCCNT` requires an implemented cycle counter.
- `CPICNT`, `EXCCNT`, `SLEEPCNT`, `LSUCNT`, and `FOLDCNT` require the DWT profiling counters.
- `DWT_CTRL.NOPRFCNT` reports whether the profiling counters are absent.
- Newer processors can expose PMU events instead of, or in addition to, the legacy DWT profiling counters.

The generator must discover event-counter presence rather than validate events only by processor name.
