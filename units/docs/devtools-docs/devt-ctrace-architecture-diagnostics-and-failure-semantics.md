---
id: "devt-ctrace-architecture-diagnostics-and-failure-semantics"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Diagnostics and failure semantics"
summary: "Diagnostics carry a severity, compact message, normal context, optional detailed message, detailed context, typed raw-location data, visibility, and impact. Severity describes the issue, while impact determines whether the current job must fail."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/architecture.md#diagnostics-and-failure-semantics"
license: "Apache-2.0"
mode: "V"
---

Diagnostics carry a severity, compact message, normal context, optional detailed message, detailed context, typed
raw-location data, visibility, and impact. Severity describes the issue, while impact
determines whether the current job must fail. This distinction allows a trace-run generation error to remain visible
without necessarily preventing the decoding of otherwise valid trace input.

`MessageCatalog.inc` owns ctrace's diagnostic templates and generates the central `MessageId` enum. Each entry keeps
its detailed and compact text together. `Messages` substitutes positional arguments; typed `TraceMessages` and
`DiagnosticMessages` adapters select IDs and arguments. Trace records remain structured until output; CLI-only
messages can be formatted at their existing call sites. See the [message-system design](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/message-system-design.md).

`StderrDiagnosticSink` selects normal text or detailed text/context for `--verbose` / `-v`. Normal trace messages match
CSV notes; raw offsets/ranges, cycle intervals, native codes and packet previews remain verbose details. Selected
configuration, metadata, prescalers and run statistics use `Visibility::Verbose`; byte-skip Info, warnings and errors
remain normally visible. Operational file/field/cause details remain actionable without verbosity. The option does
not affect decoding, file outputs, event filtering or failure counts; `DiagnosticSink::report` counts impact before
the sink makes its presentation choice. There is no global mode or text-based context filter.

Typed raw locations preserve zero-based original-file byte offsets, optional exclusive interval ends, and observed
synchronization positions. The input-scoped sink uses file size and effective format to render `raw_offset`,
`position_kind`, and a bounded `read_offset`/`read_length` window. Exact unformatted positions, formatted
source-position hints, and decoder progress are distinguished as `exact`, `formatter_hint`, and `input_progress`.
Inspection windows are at most 128 bytes, include nearby context, and are clipped to EOF; formatted starts are
16-byte frame aligned. The window supports targeted hex inspection without promising independently decodable trace.
Missing `previous_sync_offset` and `next_sync_offset` values remain `unknown`. Verbose context values are quoted and
escaped when needed, keeping paths and control characters unambiguous. Default context rendering stays unchanged.

One verbose `RawInputInspection` Info per input reports its absolute path, size, effective format/framing,
configuration, ctrace version, and the byte-based zero-origin offset convention. The absolute path retains symbolic
links and `..` without lexical rewriting. Size comes from the retained input handle during preflight, so replacing
the path does not substitute an unrelated file's size. Context enrichment computes read
windows from known positions; it does not rescan or copy the capture. CSV and CTF receive no inspection fields.

Decoder issue packets remain part of the event stream. `DecodeConsumers` reports every issue to stderr independently
of output filters and forwards all events to the backends. The backends apply stream and type selection internally;
selected issues become CSV error rows or CTF trace-status events. Repeated issues are not silently collapsed.
Ordinary route-bound CSV warnings and errors both use the `error` selector: an explicit type filter must include
`error`, and the route must pass the stream filter. The published CSV schema has neither a `warning` type nor a
severity column; diagnostic severity remains available in CLI output.

A fatal decode abort adds an input-wide CSV `type=error` record regardless of type or stream selection. Only `type`
and `note` are populated. The note starts with `Decode aborted; trace incomplete` and appends a compact
structured cause when available; normal CLI shares this text, while verbose CLI adds the processed-byte count and
detailed reason. The empty cycle and stream fields avoid
inventing a timestamp or assigning the input-wide termination to one route. This is
a ctrace output contract beyond the published specification, which does not define partial-file retention or
global abort records. It does not turn ordinary route-bound diagnostics into unfiltered CSV rows.

Byte-skip annotations are non-failing Info, not synchronization events. CSV uses `type=info`, `N bytes skipped: reason`,
the observed formatter ID in `stream` when known, and empty `cycles`, `index`, `value`, `pc`, and `address` fields.
The first formatter output group's raw offset is included only in the verbose CLI message.
These rows bypass both type and stream filters; `info` is not a new selectable event type. CTF ignores them instead
of creating routes or clocks, and CLI Info remains visible in CTF-only mode. The existing once-per-ID unsupported
source warning remains separate from byte accounting. A route-bound missing-sync Error follows ordinary output
selection but always contributes to command failure; its text does not repeat the byte count already reported as Info.

Overflow CLI warnings stay aggregated per internal route. Normal wording is `Trace overflow; timestamp discontinuity`, with
`N more occurred` when needed; verbose output also identifies the first known timestamp, first and last raw positions,
up to three position samples and the number omitted. The bounded sample list prevents aggregation from growing with
the capture size. CSV retains one compact overflow note per selected event. Overflow warnings alone are non-failing.

An invocation-wide diagnostic sink aggregates failures while remaining inputs in the same set and other solution
sets continue, then determines the final process status. Errors are rendered as `error` even when their impact causes
a non-zero exit status. Unhandled internal ctrace failures also terminate the command after an error diagnostic.
An input-scoped forwarding sink adds `inputChannel` and `input` context to every file-job diagnostic while preserving
its severity, failure impact, visibility and optional detailed fields, including typed raw locations. Producer reference
annotations are reported once per configuration, before file jobs, and their foreign text remains intact in both CLI modes.
