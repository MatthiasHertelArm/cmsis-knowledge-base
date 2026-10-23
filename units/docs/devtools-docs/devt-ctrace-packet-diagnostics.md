---
id: "devt-ctrace-packet-diagnostics"
type: "concept"
domain: "trace"
title: "ctrace: Packet diagnostics"
summary: "CLI trace diagnostics are independent of event filters."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/README.md#packet-diagnostics"
license: "Apache-2.0"
mode: "V"
---

CLI trace diagnostics are independent of event filters. Ordinary route-bound error and warning rows in CSV follow
`--stream` and `--type`: their output type is `error`, so `--type dwt error` retains both DWT data and selected-stream diagnostics,
whereas `--type dwt` omits those diagnostic rows. The global fatal-abort record described above is the exception.
The [published CSV specification](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#csv-format)
defines `error` and its free-text `note`, but no `warning` type or severity column; ctrace adds neither.

CSV notes and normal CLI messages state what happened, retaining the cause and meaningful byte counts. They omit raw
positions, intervals, native error/response codes and packet data. For example, the captured SWO errors produce:

```csv
cycles,stream,type,index,value,pc,address,note
29249610,,error,,,,,Invalid ITM packet sequence
29249610,,error,,,,,2179 raw bytes without usable ITM packets
39449474,,error,,,,,Incomplete ITM packet at EOF
```

Normal CLI adds severity and input/stream identity so diagnostics can be attributed across inputs. `--verbose`
additionally shows native OpenCSD details, the structured `raw_offset` and known recovery timestamps. Raw positions
are zero-based byte offsets in the original input file. `position_kind=exact` identifies an unformatted location,
`formatter_hint` a formatted source-position group, and `input_progress` a progress boundary rather than a packet start.
`read_offset` and `read_length` identify an inspection window of at most 128 bytes, with nearby context and clipping
at the file boundaries. Formatted windows start at a 16-byte frame boundary. For example, a window with `read_offset=0`
and `read_length=64` can be inspected with `xxd -g 1 -s 0 -l 64 capture.SWO.raw`. This is a hex-inspection window;
independent decoding may require earlier synchronization and decoder state.

When the raw-packet callback identifies the failing packet, the verbose CLI diagnostic also
includes `packet=ASYNC, packet_size=2, packet_bytes=[00 fe], packet_bytes_truncated=false`, for example. Sizes count
bytes; previews contain at most 16 bytes, with `packet_bytes_truncated=true` when shortened. Unavailable bytes use
`packet_bytes=unavailable`; this remains distinct from an empty packet. Incomplete packets
at end of input receive the same context even when OpenCSD reports them only
through the packet monitor, without a logger error.

For formatted input, the reported raw index can identify a deformatter output
group rather than the exact physical position of the failing byte. `packet_bytes_kind=deformatted` identifies ITM
payload bytes that need not be contiguous in the file; unformatted previews use `packet_bytes_kind=file`. A recovery
message distinguishes a later hardware SYNC from reaching end of input without resynchronization. Compact wording
reports `N raw bytes affected`; `--verbose` also gives the raw interval and synchronization position. The interval
includes formatter control and potentially other routes: its length is not a count of
zero bytes or discarded ITM payload bytes. `raw_end` is exclusive; unknown `previous_sync_offset` and
`next_sync_offset` values are explicitly `unknown`. Errors still make the invocation
fail even when decoding resumes and completed outputs are retained.

Overflow warnings remain aggregated once per route: `Trace overflow; timestamp discontinuity`, followed by
`N more occurred` when needed. `--verbose` also reports the first known timestamp, first and last raw positions,
up to three sample positions and the number of omitted samples. Overflow alone does not make the command fail.

Each input emits a verbose-only inspection Info with `input_path` (absolute path), `input_size` (bytes), effective
`format`, `framing`, selected `config`, `ctrace_version`, `offset_unit=byte` and `offset_base=0`. Configuration selection,
trace-run metadata, prescalers and processing statistics also appear only with `--verbose`; byte-skip information,
warnings and errors remain visible normally. File and configuration failures retain the file, field and cause needed
to act on them in either mode.

The input size is measured from the retained file handle during preflight. The absolute path keeps symbolic links
and `..` intact.

CSV diagnostic notes and default CLI wording intentionally change. Consumers that compare complete diagnostic
strings must update those expectations. Columns, event types and filters are unchanged. Use `type` and `stream` for
selection and `--verbose` for full diagnostic context. Internal message IDs are not additional CSV fields.
See the [message-system design](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/message-system-design.md) for catalog and parameter handling.
