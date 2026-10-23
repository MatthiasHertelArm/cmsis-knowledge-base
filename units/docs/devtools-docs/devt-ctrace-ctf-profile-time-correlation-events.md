---
id: "devt-ctrace-ctf-profile-time-correlation-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Time-correlation events"
summary: "The payload preserves the decoded Global Timestamp value and its clock-change indication. The CTF event header still contains the current local timestamp in the stream's referenced clock domain (swo_clock for the legacy layout or cmsis_clock<n> for a generalized stream)."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#time-correlation-events"
license: "Apache-2.0"
mode: "V"
---

### GLOBAL_TIMESTAMP (event ID 5)

```text
uint64_t cmsis_global_timestamp
uint8_t  cmsis_clock_change
```

The payload preserves the decoded Global Timestamp value and its clock-change indication. The CTF event header still
contains the current local timestamp in the stream's referenced clock domain (`swo_clock` for the legacy layout or
`cmsis_clock_<n>` for a generalized stream). Emitting this event does not by itself synchronize independent trace
clock domains or make an unreliable local timestamp reliable.
