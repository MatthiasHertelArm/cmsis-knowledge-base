---
id: "tbx-experimental-features-configure-trace-generation"
type: "concept"
domain: "project"
title: "Experimental Features: Configure Trace Generation"
summary: "The file .cmsis/<solution-set>.ctrace.yml is the user-facing configuration file for the trace generation. The CMSIS-Debugger implements a graphical user interface that is shown below. Each processor has a separate configuration section."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#configure-trace-generation"
license: "Apache-2.0"
mode: "V"
---

The file [`.cmsis/<solution-set>.ctrace.yml`](#file-structure-of-ctraceyml) is the user-facing configuration file for the trace generation. The CMSIS-Debugger implements a graphical user interface that is shown below. Each processor has a separate configuration section.

(figure: Trace components and data flow)

The available options in the user interface depend on the Cortex-M processor and on the selected [trace stream channel](#trace-stream-channels) that is used to obtain trace. Depending on the processor implemention, option setting may get rejected at the level of pyTS or pyOCD.

Option                 | M0 | M0+, M23 | M3, M4, M7, M33 | M52, M55 | M85
:----------------------|:--:|:--------:|:---------------:|:--------:|:------:
Timestamps             | -  | -        | yes             | yes      | yes
Exceptions             | -  | -        | yes             | yes      | yes
Event Counters         | -  | -        | yes             | yes      | yes
PMU Event              | -  | -        | no              | yes      | yes
Instrumentation Trace  | -  | -        | yes             | yes      | yes
DWT Data Trace         | -  | -        | 4 comparators   | 8 comparators | 8 comparators
Instruction Trace      | -  | with TB  | with TB         | with TB  | with TB
Start, Stop, Halt      | -  | 2 comparators | 4 comparators | 8 comparators | 8 comparators
PC Sampling            | -  | -        | yes             | yes      | yes
Time Synchronization   | -  | -        | yes             | yes      | yes
Stream Synchronization | -  | -        | yes             | yes      | yes

!!! Note
    - The available Event Counters depend on the Cortex-M processor.
    - The DWT comparators available for `DWT Data Trace` and `Start, Stop, Halt` are shared, so the total number of available comparators is not the sum of the values in the two rows.
    - M52, M55, M85 use the first 4 DWT comparators for data trace.

!!! Note
    Trace configuration through `*.ctrace.yml` and the Trace Generation dialog is not designed to coexist with other user-provided programming of target trace registers.
