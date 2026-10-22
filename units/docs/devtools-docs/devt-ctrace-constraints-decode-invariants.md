---
id: "devt-ctrace-constraints-decode-invariants"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Decode invariants"
summary: "ctrace Constraints: Decode invariants"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/constraints.md#decode-invariants"
license: "Apache-2.0"
mode: "V"
---

- Both unformatted and formatted inputs use an OpenCSD `DecodeTree`: `SINGLE` for the synthetic route and
  `FRAME_FORMATTED` with one decoder per configured ITM Trace Bus ID. There is no direct-ITM fallback path.
- Only one tree may be live and fed at a time. Its session owns the process-global OpenCSD logger lease, destroys the
  tree before releasing callback state, and restores the previously installed logger on every exit path.
- Raw trace bytes are passed to the decoder unchanged; ctrace never injects synthetic synchronization. Recovery
  resumes only at synchronization present in the input.
- Payload skipped before a source ID is known or assigned to NULL, reserved, or unconfigured IDs is accounted as
  non-failing Info. Bounded accounting counts deformatted payload bytes, not raw/control bytes, and records the first
  formatter output group's raw offset, not an exact discarded-byte position. The source ID is unknown only before
  its first assignment: formatted decoding neither resets the frontend nor enables reset-on-FSYNC.
- On a known formatted route, initial `NOTSYNC` payload is counted in deformatted ITM bytes, never inferred from
  differences between raw offsets. If real synchronization is later committed, a byte-skip Info annotation precedes
  that first sync. An existing route error/recovery interval suppresses duplicate initial-loss accounting. If no
  real sync is committed by end of input, the skipped-byte Info and the separate missing-sync Error below apply.
  These annotations do not replace the existing accounting for general SWO or malformed-packet recovery.
- File-read chunks are not packet boundaries. Decoder state must survive arbitrary read boundaries.
- Error callbacks collect complete stable batches; they do not reset, roll back, emit output, or throw through
  OpenCSD. Classification and recovery happen only after the current synchronous data-path operation returns.
- A recoverable error assigned to a known ITM route discards only that route's failed transaction suffix and resets
  only its packet-processor/full-decoder chain. The frame deformatter, current formatter ID, partially delivered
  frame, and unaffected routes remain intact. A bounded root flush drains pending frame segments before new input.
- The DecodeTree-reported processed-byte count is the only formatted-input cursor. Bytes reported as consumed are
  never re-fed. Only the affected route remains in data loss until a real hardware sync; unresolved loss is closed at
  end of input.
- At formatted end of input, each configured route with received ITM payload but no committed real hardware sync
  reports one route-bound `OpenCsdMissingSync` Error. Rolled-back sync callbacks do not establish synchronization;
  configured routes without received bytes are not errors. This failure returns non-zero while retaining completed
  outputs and healthy routes, instead of silently producing an apparently successful empty conversion.
- A channel-less or deformatter error, failed route reset, incomplete formatted framing/input, unrecoverable response,
  exhausted wait, or repeated lack of progress is input-fatal and stops decoding. Outputs follow the fatal-abort policy
  below: CSV retains committed rows with an abort marker; incomplete CTF is removed and excluded from target XML.
  An incomplete packet at
  the end of an unformatted ITM stream retains the legacy recoverable behavior: it is published as a decoder issue and
  does not by itself abort otherwise valid output.
- Discontinuities flush or clear pending route-local DWT state and invalidate timestamp quality before decoding
  continues. Timestamp prescalers default to `1`, accept only `1`, `4`, `16`, or `64`, and are applied exactly once
  after OpenCSD exposes raw ITM ticks.
