---
id: "tbx-experimental-features-instruction-trace-start-and-stop"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / Instruction Trace Start and Stop"
summary: "The generic start: and stop: condition syntax cannot always map directly to every trace component."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#instruction-trace-start-and-stop"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

The generic `start:` and `stop:` condition syntax cannot always map directly to every trace component.

- Cortex-M3, Cortex-M4, and Cortex-M23 ETMv3 implementations and Cortex-M7, Cortex-M33, Cortex-M52, Cortex-M55, and Cortex-M85 ETMv4 implementations use DWT or processor comparator inputs for stateful start/stop control. ETMv4 can additionally use resource selectors for event-based trace filtering; single-shot control is needed only when a transient comparator match must be latched.
- Cortex-M7 instruction-and-data ETM additionally provides local address comparators, data-value comparators, counters, and a sequencer.
- Cortex-M0+ MTB uses `TSTART` and `TSTOP` integration inputs. These can be driven by optional MTB_DWT comparators in an SoC implementation.
- Cortex-M23 and Cortex-M33 MTB implementations can use DWT comparator matches for start and stop control.
- Available start and stop conditions are constrained by DWT comparators shared with watchpoints and data trace.

The requested `X`, `R`, `W`, `RW`, value-match, and range conditions are not supported by every ETM or MTB trigger path. The resolver should report when a condition is syntactically valid but cannot be represented by the selected component.
