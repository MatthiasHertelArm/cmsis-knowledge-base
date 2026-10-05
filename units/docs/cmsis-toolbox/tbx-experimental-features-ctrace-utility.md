---
id: "tbx-experimental-features-ctrace-utility"
type: "concept"
domain: "project"
title: "Experimental Features: `ctrace` Utility"
summary: "The ctrace utility reads the raw trace data files in the directory .trace. It can check the raw data trace files for consistency or convert the files into CSV and CTF format."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#ctrace-utility"
license: "Apache-2.0"
mode: "V"
---

The `ctrace` utility reads the raw trace data files in the [directory `.trace`](#directory-and-file-structure). It can check the raw data trace files for consistency or convert the files into CSV and CTF format.

`ctrace` is based on the open source trace decoder [github.com/linaro/opencsd](https://github.com/linaro/opencsd) and adds a CSV and CTF converter. This utility will be part of CMSIS-Toolbox.

```txt
Usage:
  ctrace <trace-dir> [options]

Options:
      --csv                Generate CSV files
      --ctf                Generate CTF files
  -a  --all                Generate both CSV and CTF files
      --type sel [...]     Filter output for specific packet types; repeat to select multiple types (default: all packet types)
      --stream sel [...]   Filter output for specific streams; repeat to select multiple streams (default: all streams)
  -c, --channel arg        Specify <channel> to decode; repeat to decode multiple channels
                           (default: process all channels for specified solution sets in trace-dir)
  -t, --target arg         Specify <solution-set> (default: process all solution sets in trace-dir)
  -v, --verbose            Print detailed diagnostics (default: off)
  -V, --version            Print version
```

`ctrace` processes files in the specified `<trace-dir>`:
- If this directory contains more than one `<solution-set>`, each solution set is processed separately.
- If a solution set contains more than one `<channel>`, each channel is processed separately.

CSV and CTF output files are written to the `<trace-dir>` as explained under [directory and file structure](#directory-and-file-structure).
When no option for generating files is specified, the raw trace data files are validated.

### `--type` option

The `--type` option is applied to the decoded packet type for both CSV and CTF files. Only the specified packet types are contained in the generated files.

Accepted packet types are: `itm`, `dwt`, `event`, `pmu`, `exception`, `pcsample`, `global_ts`, `overflow`, `error`.

**Example:**

Output only the packet types `dwt` and `event` to the generated CSV and CTF files.

```bash
ctrace .trace --all --type dwt event
```

### `--verbose` option

The `--verbose` option (short form `-v`) enables detailed CLI diagnostics on `stderr`. By default, diagnostics use compact text with the cause and relevant counts.

### CSV Format

The CSV output file uses these columns:

Column         | Description
:--------------|:------------------------------------
`cycles`       | Timestamp in CPU clock cycles, if available.
`stream`       | Stream ID (CoreSight ATB ID) of the trace packet. Empty if no formatting.
`type`         | Packet type: `itm`, `dwt`, `event`, `pmu`, `exception`, `pcsample`, `global_ts`, `overflow`, `error`.
`index`        | Index of the ITM channel, DWT comparator, or exception depending on `type` value.
`value`        | Value in hexadecimal form. For packet type `exception` state transition: `0x1` enter, `0x2` exit, `0x3` return.
`pc`           | Program counter for packet types `dwt` and `pcsample`.
`address`      | Data address for packet type `dwt`.
`note`         | Additional details, used for error notification.

The `value`, `pc`, and `address` columns use hexadecimal form. See [Variable Data Sizes](#variable-data-sizes) for details.

The following table contains details about the packet type. Information is empty when not provided by the trace packet.

`type`      | Description
:-----------|:------------------------------------
`itm`       | `index` = ITM channel.
`dwt`       | `index` = DWT comparator, `value` = data value, `address` = data address, `pc` = program counter.
`event`     | Reserved for profiling/event-counter rows. Detailed semantics will be specified in a future version.
`pmu`       | Reserved for PMU counter rows. Detailed semantics will be specified in a future version.
`exception` | `index` = exception number. `value` = exception state transition.
`pcsample`  | `pc` = program counter.
`global_ts` | Global timestamp for synchronization between streams.
`overflow`  | Marks an overflow, reason can be an overflow packet or an internal decoder overflow.
`error`     | Decode error, for example unexpected trace byte values. `note` field carries details.

!!! Note
    The timestamp packet type information is provided in the `cycles` column.

#### Variable Data Sizes

For the `value`, `pc`, and `address` columns, the number of hex digits represents the payload size: 1 byte: `0x00`, 2 bytes: `0x0000`, 4 bytes: `0x00000000`.

For packet type `dwt`, payload sizes depend on the architecture:

Column      | Armv7-M       | Armv8-M
:-----------|:--------------|:--------------
`value`     | 1, 2, or 4 bytes | 1, 2, or 4 bytes
`pc`        | 4 bytes       | 1, 2, or 4 bytes
`address`   | 2 bytes       | 1, 2, or 4 bytes

`pc` and `address` payloads shorter than 4 bytes replace the corresponding lower bytes of the address programmed into the DWT comparator.

#### PC Sampling Markers

For packet type `pcsample`, raw trace data normally has a 4-byte payload which is shown in the `pc` column. 1 byte payloads are special markers indicating that the program counter value could not be traced. `pc` is empty in these cases, and the corresponding message is written to the `note` column.

Value                 | `note`
:---------------------|:--------------
`0x00`                | `CPU Sleeping`
`0xFF` (Armv8-M only) | `Trace prohibited`

**Exception State Transition:**

Value | State    | Meaning
:-----|:---------|:------------------------------------
`0x0` | reserved | Causes a decode error.
`0x1` | `enter`  | The exception became the active processor context.
`0x2` | `exit`   | The exception context was left or completed; consumers usually close that exception lane.
`0x3` | `return` | Execution returned to, or resumed, the named exception context after another exception.

**Example:**

```csv
cycles,stream,type,index,value,pc,address,note
2518192,,itm,0,0x53,,,
2518404,,itm,0,0x54,,,
2518616,,itm,0,0x4d,,,
949338400,,dwt,2,0xfffffdf9,0x08001234,0xfdf9,
949338400,,dwt,3,0x0000006c,0x08001240,0x006c,
949338400,,dwt,0,0x00,,,
949339000,,pcsample,,,0x08000100,,
949338400,,exception,0,0x3,,,
949338400,,overflow,,,,,
950364820,,exception,11,0x1,,,
950389420,,exception,0,0x3,,,
```

cycles    | stream | type      | index  | value      | pc         | address | note
:---------|:-------|:----------|:-------|:-----------|:-----------|:--------|:-----
2518192   |        | itm       | 0      | 0x53       |            |         |
2518404   |        | itm       | 0      | 0x54       |            |         |
2518616   |        | itm       | 0      | 0x4d       |            |         |
949338400 |        | dwt       | 2      | 0xfffffdf9 | 0x08001234 | 0xfdf9  |
949338400 |        | dwt       | 3      | 0x0000006c | 0x08001240 | 0x006c  |
949338400 |        | dwt       | 0      | 0x00       |            |         |
949339000 |        | pcsample  |        |            | 0x08000100 |         |
949338400 |        | exception | 0      | 0x3        |            |         |
949338400 |        | overflow  |        |            |            |         |
950364820 |        | exception | 11     | 0x1        |            |         |
950389420 |        | exception | 0      | 0x3        |            |         |

#### Loopback Requests

A CSV consumer can request that the **Trace Generation** dialog opens the setting which produced a CSV record. The loopback request uses these parameters:

Parameter      |             | Description
:--------------|:------------|:------------------------------------
`type`         |**Required** | CSV record `type`. Identifies the trace setting in the dialog, e.g. Exceptions or DWT Data Trace.
`stream`       |  Optional   | CSV record `stream` value. Identifies the trace stream the setting belongs to. Implicitly indicates the trace source and processor that generated the trace. An empty value indicates unformatted trace.
`index`        |  Optional   | Depending on CSV record type, `index` may specify a value to narrow down the origin of a record, e.g. the `exception` number, an `itm` channel, or a `dwt` comparator. Where applicable, this may help to identify a child of a setting node.
`solution-set` |  Optional   | `<solution-set>` part of the CSV filename `.trace/<solution-set>.<channel>.csv`. Helps filtering requests if multiple solution-sets store trace data in the `.trace` directory.

Requests are used to look up `ref:` nodes in `.trace/<solution-set>.ctrace-run.yml`. More than one may match.

Types `overflow` and `error` report stream and decoder states and are not associated to a setings entry. Hence they do not resolve to a `ref:` node.

### CTF Format

The generated [Common Trace Format (CTF) v1.8.3](https://diamon.org/ctf/v1.8.3/) is compatible with [Trace Compass](https://eclipse.dev/tracecompass/) and is used by [Trace Viewer for VS Code](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.vscode-trace-extension). It uses the following files that are generated by `ctrace` in the directory `.trace/<solution-set>.ctf/`.

File           | Description
:--------------|:------------------------
`metadata`     | Metadata information for Trace Compass.
`stream_<n>`   | Trace data stream.
