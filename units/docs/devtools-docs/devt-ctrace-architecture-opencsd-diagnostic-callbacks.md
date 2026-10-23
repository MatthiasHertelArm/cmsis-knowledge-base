---
id: "devt-ctrace-architecture-opencsd-diagnostic-callbacks"
type: "concept"
domain: "trace"
title: "ctrace Architecture: OpenCSD diagnostic callbacks"
summary: "The callbacks remain complementary; no single callback reports every damaged-input condition."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/architecture.md#opencsd-diagnostic-callbacks"
license: "Apache-2.0"
mode: "V"
---

The callbacks remain complementary; no single callback reports every damaged-input condition.

| Input | Use in ctrace |
| --- | --- |
| `LogError` | Native code, severity, message, optional index and source ID. |
| `RawPacketDataMon` | Hardware SYNC, overflow, NOTSYNC, malformed packets, and incomplete EOT packets. |
| `TraceElemIn` | ITM software, DWT, and timestamp semantics. |
| `TraceRawFrameIn` | Route attribution and accounting for unassigned, NULL, reserved, or unconfigured source IDs. |
| Root response and consumed count | Continue/wait/fatal handling, progress validation, and warning fallback. |

Recovery is decided after the root operation returns. Packet previews copy at most 16 bytes. A warning response
without a warning/error callback emits one non-discontinuous warning; generic no-sync/EOT elements do not duplicate
the packet-monitor diagnostics.

OpenCSD logs an ITM packet error before invoking the raw-packet monitor. Ctrace
therefore joins their observations after the operation using the normalized route
and exact OpenCSD packet index. The copied context survives transaction rollback
until that operation's logger diagnostics have been emitted; a new operation
clears it. No pointer into the producer's buffer is retained. Typed message data and packet
context survive until output formatting. Verbose CLI preserves native detail and the bounded
packet preview; normal CLI and CSV use the same compact category, cause and meaningful counts from the shared
[message catalog](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/message-system-design.md).

Packet context renders stable `packet`, `packet_size`, `packet_bytes`, and `packet_bytes_truncated` fields. The preview
contains at most 16 hexadecimal bytes with truncation marked outside the brackets. Unavailable bytes remain explicit.
The input-scoped sink identifies their domain with `packet_bytes_kind=file` for unformatted input or `deformatted`
for formatted ITM payload. Formatted preview bytes need not be contiguous in the original raw file.

The current ITM decoder and formatter do not emit `LogMessage` diagnostics or
warning-only root responses themselves. The latter are handled defensively.
`LogMessage` is not promoted into protocol errors: it has no packet index or
source-ID contract and cannot justify resetting a decoder. Unsupported generic
trace families remain outside this ITM-only profile. Existing SYNC, overflow,
NOTSYNC, and EOT reporting is not duplicated by extra callback hooks.

Formatted recovery diagnostics distinguish later synchronization from no SYNC before EOT. Compact text reports
the number of raw bytes affected; verbose text also reports OpenCSD's next hardware-SYNC index or unresolved span.
Their raw interval is a
source-position span, including formatter control and interleaved streams, not an
exact count of discarded protocol bytes. A formatted packet index can identify a
deformatter output group rather than the exact physical position of its first
byte. Packet rollback remains separate from the fatal-input output policy described above.
