---
id: "tbx-experimental-features-etm-synchronization"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / ETM Synchronization"
summary: "The ETM synchronization range 0, 256, ... , 1M is not generally configurable on the listed Cortex-M processors."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#etm-synchronization"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

The ETM synchronization range `0`, `256`, ... , `1M` is not generally configurable on the listed Cortex-M processors.

- Cortex-M3, Cortex-M4, and Cortex-M23 ETMv3 implementations use a read-only `ETMSYNCFR` fixed at `1024` trace bytes.
- Cortex-M33, Cortex-M52, Cortex-M55, and Cortex-M85 use a read-only `TRCSYNCPR` fixed at `1024` trace bytes.
- Cortex-M7 instruction-only ETM uses a read-only `TRCSYNCPR` fixed at `1024` trace bytes.
- Cortex-M7 instruction-and-data ETM has a programmable `TRCSYNCPR`. The requested period must use an implemented power-of-two encoding.

Among the listed Arm ETM implementations, an `ETM\<period>` override is therefore configurable only for the Cortex-M7 instruction-and-data ETM. For other implementations, the tool should accept a fixed or default setting and diagnose attempts to override it.

The ETM synchronization unit is **trace bytes**, not processor cycles.
