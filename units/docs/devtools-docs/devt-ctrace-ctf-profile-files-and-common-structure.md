---
id: "devt-ctrace-ctf-profile-files-and-common-structure"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Files and common structure"
summary: "Each raw input writes an independent <solution-set>.<channel>.ctf bundle, where <channel> is SWO, TB, or TB<name>. The channel is always included, even when only one input exists. Inputs are processed sequentially; their metadata, stream IDs, clocks, and output cleanup are independent."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#files-and-common-structure"
license: "Apache-2.0"
mode: "V"
---

Each raw input writes an independent `<solution-set>.<channel>.ctf` bundle, where `<channel>` is `SWO`, `TB`, or
`TB_<name>`. The channel is always included, even when only one input exists. Inputs are processed sequentially;
their metadata, stream IDs, clocks, and output cleanup are independent. Existing `<solution-set>.ctf` directories
are not reused, migrated, or removed. This intentional pathname change differs from the published
[file layout](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#directory-and-file-structure),
which still names `<solution-set>.ctf`; specification alignment remains outstanding.

Every CTF bundle contains a `metadata` file and zero or more binary stream files. When selected, unformatted
single-source input preserves the established layout: stream class `0` is written eagerly to `stream_0` and references
`swo_clock`. That clock now has an explicit UUID without changing the legacy binary layout. Formatted input uses
the generalized layout: each emitted Trace Bus route has its own stream class,
binary `stream_<id>` file, and explicit clock-domain reference. Formatted streams without emitted records are omitted
from the final bundle and metadata; a stream filter that selects no route therefore produces a metadata-only bundle.

Every event has this common header and public context:

```text
uint32_t id
uint64_t timestamp
uint8_t  cmsis_trace_bus_id
```

Generalized streams add one private display context after `cmsis_trace_bus_id`:

```text
cmsis_stream_<id>_route_t ctrace_route
```

`timestamp` is a cycle count in the clock domain referenced by its stream class. CTF preflight requires a non-zero
`timestamps.clock` for every configured route selected by the stream filter, before ctrace knows which routes will
emit records. A stream filter that selects no configured route requires no clock. Timestamps never decrease within
one binary stream; independent routes are not clamped against each other. All clock domains receive random UUIDs,
including legacy `swo_clock`. Independent captures and routes have distinct identities even when their configured
frequencies are equal, because equal frequency alone does not establish synchronization.

`cmsis_trace_bus_id` identifies the CoreSight Trace Bus route. Value `0` denotes unformatted single-source input;
formatted IDs use values `1` through `111`. It is routing context, not a CPU identity. `ctrace_route` is a private
enum carrying the resolved processor name for display, or the numeric stream-class ID as an internal fallback. The
optional processor name is also stored in the generalized environment as
`cmsis_stream_<id>_processor_name`. Generated XML uses the public Trace Bus ID and clock identity, not the private
`ctrace_route` display enum.

The packet context has this exact field order:

```text
uint32_t packet_size
uint32_t content_size
uint64_t timestamp_begin
uint64_t timestamp_end
uint32_t events_discarded
uint32_t packet_seq_num
```

The timestamp fields use the stream class's clock mapping. Route-bound trace loss is represented by `TRACE_STATUS`
events rather than the CTF `events_discarded` counter, which is currently zero. Formatter skips and initial ITM
synchronization skips are separate byte-accounting Info annotations in CLI/CSV only. Their optional formatter ID
identifies observed input, not a decoded CTF route or clock; this includes NULL and reserved IDs. Ctrace does not
invent a CTF stream, timestamp, or `resync` event for these annotations.

One optional `<solution-set>.traceanalysis.xml` is stored beside the target's bundles. It collects graphical views
from eligible bundles completed in the current invocation, not from existing CTF files found on disk. Each bundle
must retain graphical data and exactly one clock domain. A multi-clock bundle is excluded with a warning; eligible
single-clock bundles still contribute. These restrictions affect only visualization; metadata-only, point-event-only,
and multi-clock CTF bundles remain valid. Historical per-channel XML files are neither migrated nor deleted.

A fatal OpenCSD decode abort removes the incomplete CTF bundle, including data already written for healthy routes,
and excludes it from target XML. If CSV output remains healthy, ctrace retains its selected rows and appends one
input-wide `error` row stating `Decode aborted; trace incomplete`, with a compact structured cause when available.
Normal CLI uses the same text; `--verbose` adds the processed-byte count and detailed abort reason. That final row has
no cycle timestamp, stream, or index and bypasses type and stream filters. A recoverable route-local error allows
normal output completion, as described
under [`TRACE_STATUS`](#trace_status-event-id-3). Both kinds of Error produce a failing command exit status. Remaining
raw inputs are still processed, and their completed bundles and XML contributions are unaffected by another input's
failure. Target XML preparation and finalization have their own lifecycle; an XML failure leaves completed CTF and
CSV outputs intact.
