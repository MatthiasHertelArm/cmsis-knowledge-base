---
id: "tbx-experimental-features-pyts-utility"
type: "concept"
domain: "project"
title: "Experimental Features: `pyTS` Utility"
summary: "The pyTS utility generates the file .trace/<solution-set>.ctrace-run.yml. It performs the following steps:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#pyts-utility"
license: "Apache-2.0"
mode: "V"
---

The `pyTS` utility generates the file `.trace/<solution-set>.ctrace-run.yml`. It performs the following steps:

- Reads the file `<name>.cbuild-run.yml` to provide the solution set, processor names, and ELF output files.
- Converts symbolic names in the file `.cmsis/<solution-set>.ctrace.yml` to physical addresses by using the corresponding ELF output files.
- Uses processor information and implementation details to map the trace generation setup into CoreSight trace register values. See [Processor-Specific Trace Features](#processor-specific-trace-features)
- Generates `ctrace-disable:` with one group per processor that needs disable writes and one write per register, covering every trace feature pyTS can configure on the target, even if not enabled.
- Rejects incompatible configuration settings with user-oriented messages (`info:`, `warning:`, or `error:`) in the `ref:` node of the file `*.ctrace-run.yml`

For a given target, `ctrace-disable:` remains unchanged when feature settings change. pyTS includes disable fields for every trace-eligible DWT comparator. If no writes are needed, it emits `ctrace-disable:` without children, which the debugger treats as no disable writes. The disable-values for supported components are listed in [Trace Component Registers](#trace-component-registers).

The final trace generation setup is written to the file `.trace/<solution-set>.ctrace-run.yml`.

This utility will be part of pyOCD.

```txt
Usage:
  pyts <name>.cbuild-run.yml
```
