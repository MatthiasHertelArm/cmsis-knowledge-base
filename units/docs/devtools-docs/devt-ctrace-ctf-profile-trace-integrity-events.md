---
id: "devt-ctrace-ctf-profile-trace-integrity-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Trace-integrity events"
summary: "An overflow or data-loss boundary closes active exception and sleep visualization state. The unknown interval is therefore visible as a gap instead of being attributed to the previously active state."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/ctf-format.md#trace-integrity-events"
license: "Apache-2.0"
mode: "V"
---

### TRACE_STATUS (event ID 3)

```text
cmsis_trace_status_reason_t cmsis_trace_status_reason
uint32_t                    cmsis_overflow_count
```

The status reason is:

| Value | Name | Meaning |
| ---: | --- | --- |
| 0 | `trace_start` | Start of generated CTF output for the route |
| 1 | `resync` | Hardware synchronization observed |
| 2 | `overflow` | Trace source reported an overflow |
| 3 | `decode_error` | Decoder reported an invalid or unsupported trace item |
| 4 | `data_loss` | An input interval could not be decoded reliably |

An overflow or data-loss boundary closes active exception and sleep visualization state. The unknown interval is
therefore visible as a gap instead of being attributed to the previously active state. Status records remain point
events in the standard CTF event table; the generated XML does not create a status timeline.

Route-local decoder errors and data-loss records follow the normal `error` type and stream filters in CSV and CTF.
CLI trace diagnostics remain visible independently of those filters. Normal CLI and CSV use compact categories,
causes and meaningful counts. Native decoder codes and descriptions, raw positions/ranges, cycle intervals, packet
types and bounded byte previews appear only with `--verbose`. The CTF profile stores the status reason and overflow
epoch, without those strings or raw bytes; verbosity changes neither CSV nor CTF content.
Successful formatted-route recovery emits a separate data-loss diagnostic and a `resync` when a real hardware ITM
sync is committed. An unresolved interval at end of input emits data loss without a
`resync`.

A configured formatted route that receives payload but never commits a real ITM hardware sync reports a decoder
Error at end of input. When selected for output, it follows the normal route-bound `decode_error` status path; it
does not generate a `resync`. The command fails, but valid CTF output from healthy routes and selected diagnostic
records is retained. A configured route with no received payload does not produce this error.
