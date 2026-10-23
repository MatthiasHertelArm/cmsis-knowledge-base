---
id: "devt-ctrace-ctf-profile-profiling-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Profiling events"
summary: "One hardware mask is expanded into one CTF record per set bit, all with the same timestamp and quality fields:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#profiling-events"
license: "Apache-2.0"
mode: "V"
---

### DWT_EVENT (event ID 7)

```text
cmsis_dwt_event_counter_t cmsis_dwt_event_counter
uint8_t                   cmsis_sample_flags
uint32_t                  cmsis_overflow_count
```

One hardware mask is expanded into one CTF record per set bit, all with the same timestamp and quality fields:

| Bit/index | Counter name |
| ---: | --- |
| 0 | `CPICNT` |
| 1 | `EXCCNT` |
| 2 | `SLEEPCNT` |
| 3 | `LSUCNT` |
| 4 | `FOLDCNT` |
| 5 | `CYCCNT` |

### PMU_EVENT (event ID 8)

```text
cmsis_pmu_event_counter_t cmsis_pmu_event_counter
uint8_t                   cmsis_sample_flags
uint32_t                  cmsis_overflow_count
```

The PMU overflow mask is likewise expanded into one CTF record per set bit. Bits 0 through 7 are provisionally named
`Event0` through `Event7`, because the raw packet does not identify the programmable event assigned to the counter.

DWT and PMU counter records are point events without architectural duration. If such records were emitted, their
Trace Compass timelines use named lanes and artificial one-microsecond pulses. Overlapping pulses are stacked so
that a later scheduled close does not hide another occurrence.
