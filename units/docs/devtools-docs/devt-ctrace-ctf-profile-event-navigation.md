---
id: "devt-ctrace-ctf-profile-event-navigation"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Event navigation"
summary: "The profile uses CTF 1.8, little-endian byte order, and the environment identifiers:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#event-navigation"
license: "Apache-2.0"
mode: "V"
---

- Instrumentation: [`ITM`](#itm-event-id-0)
- DWT data trace: [`DWT_VALUE`](#dwt_value-event-id-1), [`DWT_ADDR`](#dwt_addr-event-id-2), and
  [`DWT_MATCH`](#dwt_match-event-id-9)
- Trace integrity: [`TRACE_STATUS`](#trace_status-event-id-3)
- Execution state: [`EXCEPTION`](#exception-event-id-4), [`PC_SAMPLE`](#pc_sample-event-id-6), and
  [`PC_SAMPLE_PROHIBITED`](#pc_sample_prohibited-event-id-10)
- Time correlation: [`GLOBAL_TIMESTAMP`](#global_timestamp-event-id-5)
- Profiling: [`DWT_EVENT`](#dwt_event-event-id-7) and [`PMU_EVENT`](#pmu_event-event-id-8)

The profile uses CTF 1.8, little-endian byte order, and the environment identifiers:

```text
cmsis_ctf_profile = "cmsis.ctf"
cmsis_ctf_profile_version = 1
```
