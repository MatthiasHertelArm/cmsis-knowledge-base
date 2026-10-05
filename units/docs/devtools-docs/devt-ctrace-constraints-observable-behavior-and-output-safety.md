---
id: "devt-ctrace-constraints-observable-behavior-and-output-safety"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Observable behavior and output safety"
summary: "ctrace Constraints: Observable behavior and output safety"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md#observable-behavior-and-output-safety"
license: "Apache-2.0"
mode: "V"
---

- Each raw input has separate `<set>.<channel>.csv` and `<set>.<channel>.ctf` outputs. One optional
  `<set>.traceanalysis.xml` collects the target's eligible completed CTF views. The channel-qualified CTF path applies
  even with one input; legacy `<set>.ctf` bundles and old per-channel XML files are not reused, migrated, or removed.
  Aligning the intentional CTF path change with the published
  CTF specification remains [follow-up work](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/todo.md#inputs-and-time-correlation).
- CSV remains one combined file per input in sink callback order, not a global raw-input or chronological order across
  routes. The unformatted route has an empty `stream` field; formatted routes expose their architectural IDs.
  Type and stream filters affect output, not decoding or diagnostic reporting. The seventh CSV column is `address`,
  matching the published CMSIS-Toolbox
  [CSV schema](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#csv-format).
- Byte-skip annotations are retained in CSV regardless of `--type` or `--stream`: `type` is `info`, `note` contains
  `N bytes skipped: reason`, and `stream` is the observed formatter ID when known, including
  `0` or `127`. All other fields are empty. `info` is an input annotation, not a new CLI type selector. No annotation
  may be represented as a hardware `SYNC`, assigned to a synthetic route, or given an invented time. CTF ignores
  these annotations, so the accounting is CLI/CSV-only. The first formatter-group offset is available with `--verbose`.
  Missing sync at end of input remains a separate route-bound Error that always reaches CLI and contributes to
  command failure, while its CSV row follows ordinary output
  filters; it does not repeat the counted bytes as another loss record.
- PC sampling distinguishes four-byte PC values from the one-byte `0x00` (`CPU Sleeping`) and Armv8-M `0xff`
  (`Trace prohibited`) status markers. CSV leaves `pc` empty for both markers and writes their meaning in `note`;
  all three remain selectable as `pcsample`. Markers preserve route, timestamp, and quality without creating an error
  or data-loss boundary. Unsupported payloads remain errors; arbitrary raw `0xff` bytes are not PC-sampling markers.
- Formatted CTF stream files are created lazily as `stream_<id>` only for routes with selected semantic output. Every
  emitted stream class references an explicit clock domain. When selected, the legacy unformatted path retains eager
  `stream_0` and its binary event layout. Its `swo_clock` now has an explicit random UUID, like generalized clocks.
- Generalized CTF metadata records a bound processor name in the corresponding stream-scoped environment entry.
  Its event context preserves the CMSIS-profile `uint8_t cmsis_trace_bus_id` field and adds the ctrace-private
  `ctrace_route` enum for display. The enum label is the processor name when bound and the decimal CTF stream-class ID
  otherwise; XML does not depend on this private field. XML state paths use `hostId` (the bundle's sole clock UUID),
  architectural `cmsis_trace_bus_id`, and topic. View paths bind those identities explicitly, including ID `0` for
  legacy input. Labels use the input channel and optional processor name, never the numeric ID. Analysis/view IDs
  share a namespace derived from contributing clock UUIDs, preventing cross-target registration collisions.
- XML declares only graphical outputs: DWT values and addresses as XY series; trace-origin exceptions, DWT matches,
  DWT/PMU overflow events, and processor sleep state as time graphs. Each block is emitted only if the completed stream
  contains matching trace data; synthetic exception bootstrap records alone do not enable an exception block, and
  `Processor State` specifically requires a sleep indication. ITM payloads, ordinary sampled
  PCs, trace-prohibited markers, and trace-status records stay available through the CTF event table. Trace Compass XML
  has no data-driven table-view type, so ctrace does not model these point records as artificial timelines.
  If no graphical topic remains after output filtering, no target XML is generated and stale target XML is removed;
  an empty analysis is not a valid Trace Compass configuration. The CTF bundle remains available.
- `timestamps.clock` has no ctrace fallback. For every route selected for CTF, missing, null, invalid, zero, or
  conflicting frequency is accepted for validation-only and CSV operation but prevents CTF generation with an Error.
  A filter selecting no configured route requires no clock because it can emit no CTF stream. With `--all`, valid CSV
  still completes while the invocation returns non-zero.
- Each formatted route has an independent CTF clock domain, even when processor labels or frequencies match.
  A multi-clock CTF bundle remains valid, but ctrace emits one Warning and excludes that bundle from target XML
  because the supported reader cannot establish its combined event order. Separate single-clock bundles can all
  contribute to one XML; their UUID-scoped states remain separate. Neither correlation nor timestamp rebasing is
  inferred between those bundles, even when frequencies or processor labels match.
- CLI decoder warnings and errors remain observable regardless of output filtering. Ordinary route-bound CSV
  diagnostics follow the stream filter and use the `error` type selector, including warning-severity issues. The
  published CSV schema defines no `warning` type or severity column. A recoverable protocol error may be published
  with selected route-bound error/data-loss events even though its Error diagnostic makes the invocation fail.
- A fatal OpenCSD decode abort preserves already committed CSV rows and appends one input-wide `type=error` record
  whose `note` starts with `Decode aborted; trace incomplete`, followed by a compact structured cause when available.
  Normal CLI uses the same text; `--verbose` adds the processed-byte count and full abort reason. All other CSV fields
  are empty.
  This global marker bypasses both type and stream filters; ordinary route-bound errors do not. Partial
  CTF artifacts are removed and contribute no XML views. This retention and global-marker policy is an explicit
  ctrace contract, not a
  requirement of the published CSV specification. Failures before CSV startup create no CSV; CSV write or close
  failures still remove the unreliable file.
- Structured diagnostic impact determines command failure; formatted stderr text and visibility do not.
- Ctrace-owned diagnostic templates share one central message catalog. Typed records preserve trace parameters
  until CLI or CSV rendering. Normal CLI uses the same compact trace text as CSV: what happened, its cause and
  meaningful counts. Raw positions/ranges, cycle intervals, native codes and packet details appear only with
  `--verbose` / `-v`. Recovery-span lengths describe raw bytes affected, not skipped payload. Overflow summaries stay
  aggregated per route; the compact summary omits the first timestamp. Foreign text remains opaque and is never
  parsed to reconstruct parameters. Operational messages remain CLI-only; the catalog does not create new CSV event types.
- Verbosity affects only stderr presentation. CSV/CTF content, event selection, failure counts and exit status are
  unchanged. Selected configuration, metadata, prescalers and run statistics are verbose-only Info. Byte-skip Info,
  warnings and errors remain normally visible, with input/stream attribution and actionable file/field/cause details.
- Target XML is prepared before processing the target's inputs and finalized after all have been attempted. It uses
  only CTF metadata successfully finalized in that invocation, never stale bundles discovered on disk. Recoverable
  decoder errors do not exclude an otherwise completed bundle. An XML failure does not remove completed CTF or CSV;
  an input failure does not remove other inputs' contributions. No per-channel XML is generated or cleaned up.
- CTF timestamps never regress, and a global timestamp does not by itself establish local timestamp quality.
- Validation-only mode creates no output. Unsupported trace channels are diagnosed and skipped.
- Apart from the explicitly retained CSV after a fatal decode abort, cleanup of incomplete output artifacts is
  attempted after failure, and cleanup failures are reported. Incompatible existing output filesystem types are
  rejected before replacement. CTF bundles and target XML use distinct sibling paths derived from the trace-run
  and input names.
