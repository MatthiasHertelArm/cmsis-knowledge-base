---
id: "tbx-experimental-features-dwt-feature-variants"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants"
summary: "The DWT comparator count alone does not describe the implemented feature set. Data-value matching normally uses an address comparator together with a value comparator, so enabling it also allocates one or more address comparators."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#dwt-feature-variants"
license: "Apache-2.0"
mode: "V"
---

The DWT comparator count alone does not describe the implemented feature set. Data-value matching normally uses an address comparator together with a value comparator, so enabling it also allocates one or more address comparators. For Armv8-M and Armv8.1-M implementations, comparator capabilities can differ within the same DWT. Software must read each `DWT_FUNCTIONn` before allocating it.

Processor | DWT variants | Cycle counter | Profiling counters | Address and PC matching | Data-value matching | Range matching | DWT trace and trigger features
:---------|:-------------|:--------------|:-------------------|:------------------------|:--------------------|:---------------|:------------------------------
Cortex-M0 | `0-2` comparators | - | - | Watchpoint and debug-event matching | - | `DWT_MASKn` | -
Cortex-M0+ | `0-2` comparators | - | - | Watchpoint and debug-event matching | - | `DWT_MASKn` | Optional MTB_DWT matches can drive the MTB `TSTART` and `TSTOP` integration inputs
Cortex-M1 | *Reduced* `1`; *full* `2` comparators | - | - | Watchpoint and debug-event matching | - | `DWT_MASKn` | -
Cortex-M3 | *Reduced* `1`; *full* `4` comparators | `DWT_CYCCNT` | `5` DWT counters | Watchpoint, PC match, and data-address match | *Reduced*: -; *full*: `COMP1` only, using address comparator references | `DWT_MASKn` | PC, data-address, and data-value trace; cycle, exception, and event trace triggers
Cortex-M4 | *Reduced* `1`; *full* `4` comparators | `DWT_CYCCNT` | `5` DWT counters | Watchpoint, PC match, and data-address match | *Reduced*: -; *full*: `COMP1` only, using address comparator references | `DWT_MASKn` | PC, data-address, and data-value trace; cycle, exception, and event trace triggers
Cortex-M7 | *Reduced* `2`; *full* `4` comparators | `DWT_CYCCNT` | `5` DWT counters | All comparators: watchpoint, PC match, and data-address match; `COMP0`: cycle matching | *Reduced* and *full*: `COMP1` only, using address comparator references | `DWT_MASKn` | All implemented comparators support triggers and, when ITM/DWT trace is included, trace packets
Cortex-M23 | *Reduced* `2`; *full* `4` comparators | - | - | All comparators: watchpoint, instruction-address match, and data-address match | - | *Reduced*: linked `COMP0-1`; *full*: linked `COMP0-1` or `COMP2-3` | Debug and trigger events; no cycle matching or DWT trace packets
Cortex-M33 | *Reduced* `2`; *full* `4` comparators | `DWT_CYCCNT` | `5` DWT counters | All comparators: watchpoint, instruction-address match, and data-address match; `COMP0`: cycle matching; *reduced* `COMP1`, *full* `COMP1` and `COMP3`: linked or limit matching | *Reduced*: `COMP1`; *full*: `COMP1` and `COMP3` | *Reduced*: linked `COMP0-1`; *full*: linked `COMP0-1` or `COMP2-3` | All implemented comparators support triggers and, when ITM is included, trace packets
Cortex-M52 | *Reduced* `2`; *mid* `4`; *full* `8` comparators | `DWT_CYCCNT` | `5` DWT counters | *Reduced* `COMP0-1`, *mid* `COMP0-3`, *full* `COMP0-7`: instruction-address and data-address matching; `COMP0`: cycle matching; *reduced* `COMP1`, *mid* `COMP1` and `COMP3`, *full* `COMP1`, `COMP3`, `COMP5`, and `COMP7`: linking | *Reduced*: `COMP1`; *mid* and *full*: `COMP1` and `COMP3` | *Reduced*: linked `COMP0-1`; *mid*: linked `COMP0-1` or `COMP2-3`; *full*: linked `COMP0-1`, `COMP2-3`, `COMP4-5`, or `COMP6-7` | *Reduced* `COMP0-1` and *mid* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP4-7`: watchpoints and triggers only
Cortex-M55 | *Reduced* `2`; *mid* `4`; *full* `8` comparators | `DWT_CYCCNT` | `5` DWT counters | *Reduced* `COMP0-1`, *mid* `COMP0-3`, *full* `COMP0-7`: instruction-address and data-address matching; `COMP0`: cycle matching; *reduced* `COMP1`, *mid* `COMP1` and `COMP3`, *full* `COMP1`, `COMP3`, `COMP5`, and `COMP7`: linking | *Reduced*: `COMP1`; *mid* and *full*: `COMP1` and `COMP3` | *Reduced*: linked `COMP0-1`; *mid*: linked `COMP0-1` or `COMP2-3`; *full*: linked `COMP0-1`, `COMP2-3`, `COMP4-5`, or `COMP6-7` | *Reduced* `COMP0-1` and *mid* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP4-7`: watchpoints and triggers only
Cortex-M85 | *Reduced* `4`; *full* `8` comparators | `DWT_CYCCNT` | `5` DWT counters | *Reduced* `COMP0-3`, *full* `COMP0-7`: instruction-address and data-address matching; `COMP0`: cycle matching; *reduced* `COMP1` and `COMP3`, *full* `COMP1`, `COMP3`, `COMP5`, and `COMP7`: linking | *Reduced* and *full*: `COMP1` and `COMP3` | *Reduced*: linked `COMP0-1` or `COMP2-3`; *full*: linked `COMP0-1`, `COMP2-3`, `COMP4-5`, or `COMP6-7` | *Reduced* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP0-3`: watchpoints, triggers, and trace; *full* `COMP4-7`: watchpoints and triggers only

The five DWT profiling counters are `DWT_CPICNT`, `DWT_EXCCNT`, `DWT_SLEEPCNT`, `DWT_LSUCNT`, and `DWT_FOLDCNT`. Their presence is reported by `DWT_CTRL.NOPRFCNT`.

Here, data-value matching means comparing an observed load or store value. It does not by itself imply that the implementation can emit a data-value trace packet; that capability is listed separately in the final column.
