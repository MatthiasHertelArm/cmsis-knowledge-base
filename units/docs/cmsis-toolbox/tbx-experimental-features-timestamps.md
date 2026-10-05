---
id: "tbx-experimental-features-timestamps"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / Timestamps"
summary: "ITM local timestamps, ETM timestamp packets, and ETM cycle-count timing are distinct facilities. ETM timestamp packets can carry values derived from a shared system or global timestamp source."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#timestamps"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

ITM local timestamps, ETM timestamp packets, and ETM cycle-count timing are distinct facilities. ETM timestamp packets can carry values derived from a shared system or global timestamp source.

- ITM timestamp prescaler values `1`, `4`, `16`, and `64` are architectural.
- ITM timestamps require ITM and a functioning cycle counter.
- ETM timestamp packets correlate trace with the shared system timestamp domain, while ETM cycle counts report elapsed processor cycles within the instruction trace. The system timestamp generator and its distribution infrastructure are optional.
