---
id: "devt-ctrace-message-system-design-output-contract"
type: "concept"
domain: "trace"
title: "ctrace message-system design: Output contract"
summary: "--verbose controls stderr presentation only. CSV always uses compact wording; CSV and CTF content, filters, failure counts and overflow aggregation are independent of the option. Reference-file errors retain their explicit non-failing impact."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/message-system-design.md#output-contract"
license: "Apache-2.0"
mode: "V"
---

| Message family | Normal CLI | CLI with `--verbose` / `-v` | CSV |
| --- | --- | --- | --- |
| Decoder issue | Compact warning/error. | Full cause and technical context. | Same compact `error` note. |
| Skipped bytes | Count and cause. | Also formatter offset. | Same compact `info` note. |
| Fatal decoder abort | Incomplete trace and known cause. | Also processed count and full cause. | Final `error` row. |
| Overflow | One compact summary per route. | First timestamp and raw positions. | Compact `overflow` row per event. |
| Operational diagnostic | Actionable diagnostics. | Also technical configuration and run Info. | No additional row. |

`--verbose` controls stderr presentation only. CSV always uses compact wording; CSV and CTF content, filters,
failure counts and overflow aggregation are independent of the option. Reference-file errors retain their explicit
non-failing impact. CSV warning-severity decoder issues still use `type=error`; there is no new severity column.

`DiagnosticSink::Event::message` carries normal text and `context` carries always-visible attribution or actionable
details. Optional `detailedMessage` replaces the text in verbose mode; `detailedContext` adds technical fields such as
raw offsets. Typed raw-location data retains position precision, interval boundaries and known synchronization
positions until the input-scoped sink can add file size and format. `Visibility::Always` and `Visibility::Verbose`
explicitly distinguish normal diagnostics from technical run information. The stderr sink makes this presentation
choice without classifying text or filtering context keys.
`DiagnosticSink::report` still counts failing impact before presentation, and forwarding sinks preserve all fields.

[CsvRowMapper][csv-mapper] continues to escape CSV fields. Source IDs stay in `stream`, including observed null and
reserved IDs in byte-skip records. `CPU Sleeping` and `Trace prohibited` remain compact PC-state notes outside the
diagnostic catalog. CTF keeps its structured status codes and schema; it does not serialize rendered messages.

### Skipped bytes

Compact skipped-byte notes retain the count and cause:

| Cause | Compact note |
| --- | --- |
| Missing source ID | `N bytes skipped: no source ID` |
| Null source ID | `N bytes skipped: null source ID` |
| Reserved source ID | `N bytes skipped: reserved source ID` |
| Unconfigured source ID | `N bytes skipped: unconfigured source ID` |
| Missing synchronization | `N bytes skipped: no SYNC` |

The verbose CLI text also identifies the first formatter output group's raw offset. The compact note omits that
offset; it remains available internally. `TraceByteSkip::byteCount` counts skipped deformatted payload, excluding
formatter control bytes. In contrast, a formatted recovery interval can include control bytes and interleaved routes;
its length is not a skipped-payload count.

Byte-skip rows bypass type and stream filters, have no timestamp, and use the observed source ID only when known.
They do not create decoded routes, hardware synchronization events, or CTF streams.

### Decoder issues

Compact issue text answers what happened: it retains the diagnostic category, cause and meaningful counts. Raw
positions/ranges, cycle intervals, native codes, packet kinds, payload sizes and hexadecimal previews belong to
verbose CLI output. Known semantic issue codes without typed parameters receive category-only compact fallbacks.
CSV retains its existing `cycles` and `stream` columns; the note does not repeat them or append `raw@N`.

Recovery distinguishes consumed undecodable bytes from an affected raw span. Examples include
`2179 raw bytes without usable ITM packets`, `ITM resynced; 32 raw bytes affected`, and
`No ITM resync before EOF; 32 raw bytes affected`. The latter spans can include formatter control and other routes;
they must not be relabelled as skipped payload. Verbose output also identifies the raw span and known timestamp
range. A formatter-group position does not promise an exact physical packet-byte position, and missing timestamps
are not invented.

Ordinary issue and overflow rows retain their existing type/stream selection behavior; CLI reporting is unfiltered.
An overflow event uses the compact note `Trace overflow; timestamp discontinuity`. Its CLI aggregate remains a separate
catalog entry selected by `TraceOverflowSummary`: normal output appends `N more occurred` when needed, while verbose output
also includes the first known timestamp and raw-position information for the internal route. CSV still retains one
overflow row per selected event. Overflow alone remains a non-failing Warning.

### Raw-file inspection context

Verbose diagnostics carry structured locations rather than requiring callers to extract a position from prose.
All offsets are zero-based byte offsets in the original input file, written in decimal. A location includes its
precision: `exact` identifies an unformatted packet or byte boundary, `formatter_hint` identifies a formatted
source-position group, and `input_progress` identifies decoder progress rather than a failing packet start.
In particular, a formatter hint must not be interpreted as an exact physical ITM packet start.

When the input size is known and the position is within the file, a location supplies a bounded read window through
`read_offset` and `read_length`. The window includes
about 64 preceding bytes where possible, is at most 128 bytes long, and is clipped at the file boundaries.
Formatted windows start at a 16-byte frame boundary. The window is a hex-inspection aid; decoding it independently
may require an earlier
hardware SYNC and decoder state. A raw interval uses an exclusive `raw_end` boundary. Decoder locations include
`previous_sync_offset` and `next_sync_offset`; missing positions are explicitly `unknown` instead of inferred
from the window. A consumer can read exactly `read_length` bytes starting at `read_offset` without scanning the file.

Packet context uses stable fields `packet`, `packet_size`, and `packet_bytes`. Sizes count bytes, and the preview
contains at most 16 copied bytes. `packet_bytes_truncated=true` marks a shortened preview, while complete previews
use `false`. `packet_bytes=unavailable` with truncation `false` means that no preview exists; it does not mean an
empty or complete packet. For unformatted input, `packet_bytes_kind=file` identifies bytes directly from the file.
For formatted input, `packet_bytes_kind=deformatted` identifies deformatted ITM payload, which can span frames and
need not occur contiguously at the reported raw offset.
Only hexadecimal bytes appear inside the preview brackets, keeping it usable for people and tools alike.

Overflow aggregates retain `overflow_count`, `first_raw_offset`, `last_raw_offset`, at most three positions in
`sample_raw_offsets`, and `omitted_offsets` for the remaining occurrences. Their primary `raw_offset` and inspection
window describe the first occurrence. This bounds stderr output even for heavily damaged captures while preserving
specific inspection locations. No whole-file scan or additional raw-data read is required to produce these diagnostics.

Each input also emits a verbose-only `RawInputInspection` Info containing its file size, effective format and framing,
selected configuration, and ctrace version:

| Field | Meaning |
| --- | --- |
| `input_path` | Absolute spelling of the opened path; symbolic links and `..` are not rewritten. |
| `input_size` | File size in bytes measured from the retained input handle during preflight. |
| `format` | Effective `unformatted` or `formatted` input format. |
| `framing` | `none` or `memory-aligned-16`. |
| `config` | Selected trace-run configuration path. |
| `ctrace_version` | Version of the decoder that produced the diagnostics. |
| `offset_unit`, `offset_base` | `byte` and `0`. |

Input identity remains attached to every diagnostic. Unsafe verbose context values are quoted and escaped so spaces,
delimiters and control characters in paths cannot be mistaken for additional fields. These fields and the inspection
windows are CLI context; they add no CSV columns or CTF attributes and do not affect failure impact.

### Fatal aborts

The final CSV note and normal CLI error start with `Decode aborted; trace incomplete`. A compact structured cause
follows when available. Arbitrary exception text is not truncated or parsed to manufacture a compact cause. Verbose
CLI output retains the processed-byte count, complete detailed reason and available technical context.

Only `OpenCsdFatalError` becomes a shared terminal abort record. Ordinary input-read exceptions and output-backend
failures retain their CLI-only catch paths. The abort row bypasses event filters and has no route or timestamp.
Previously committed CSV rows remain; incomplete CTF artifacts are removed. A CSV write or close failure still
removes the unreliable file. A failure before CSV startup does not create a CSV file.
