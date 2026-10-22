---
id: "devt-ctrace-ctf-profile-event-catalogue"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Event catalogue"
summary: "ctrace CTF profile: Event catalogue"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#event-catalogue"
license: "Apache-2.0"
mode: "V"
---

| Group | ID | Event name | Purpose |
| --- | ---: | --- | --- |
| Instrumentation | 0 | `ITM` | ITM software stimulus value |
| DWT data trace | 1 | `DWT_VALUE` | DWT data read or write |
| DWT data trace | 2 | `DWT_ADDR` | DWT PC and/or low address bits |
| Trace integrity | 3 | `TRACE_STATUS` | Start, synchronization, overflow, and decoder discontinuities |
| Execution state | 4 | `EXCEPTION` | Exception entry, exit, and return |
| Time correlation | 5 | `GLOBAL_TIMESTAMP` | Global Timestamp packet |
| Execution state | 6 | `PC_SAMPLE` | Periodic PC sample or processor-sleep indication |
| Profiling | 7 | `DWT_EVENT` | Architectural DWT event-counter overflow |
| Profiling | 8 | `PMU_EVENT` | Programmable PMU counter overflow |
| DWT data trace | 9 | `DWT_MATCH` | Comparator match without additional data |
| Execution state | 10 | `PC_SAMPLE_PROHIBITED` | PC sampling reports that trace is prohibited |
