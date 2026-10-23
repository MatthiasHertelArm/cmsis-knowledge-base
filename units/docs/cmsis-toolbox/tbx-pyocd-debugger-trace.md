---
id: "tbx-pyocd-debugger-trace"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `trace:`"
summary: "CMSIS-DAP supports the SWO trace output of Cortex-M devices. The raw trace data are made available from pyOCD through a TCP connection or a binary file. Device-specific trace capture capabilities are configured using the device-settings node under debugger:."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#trace"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

!!! Note
    The `trace:` feature is under development. This section provides a preview.

CMSIS-DAP supports the SWO trace output of Cortex-M devices. The raw trace data are made available from pyOCD through a TCP connection or a binary file.
Device-specific trace capture capabilities are configured using the [`device-settings`](#device-settings) node under `debugger:`.

The `trace:` node has one child type per supported trace transport mode which offers mode-specific options. Currently, the [`swo-uart`](#swo-uart) type and the [`trace-buffer`](#trace-buffer) type are supported.

The default trace output file and location is derived from the [`cbuild-run.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#run-and-debug-management). It
is located in the solution's `.trace/` sub-folder and uses the format `<solution-name>+<target-type>@<target-set>.<channel>.raw`.
The `<channel>` part is derived from the type node as it follows.

Type node                          | `<channel>` |
:----------------------------------|:------------|
[`- swo-uart:`](#swo-uart)         | SWO         |
[`- trace-buffer:`](#trace-buffer) | TB          |

!!! Note
    The `trace:` node is implemented as a list. However, currently only one node is supported. Additional nodes are ignored.

```yml
trace:
  - swo-uart:                 # Trace mode is SWO UART
    input-clock: 120000000    # Trace clock = 120 MHz
```

#### `swo-uart`

Configuration for the SWO trace output in UART mode.

`trace:`                                 |              | Description
:----------------------------------------|:-------------|:------------------------------------
`- swo-uart:`                            | **Required** | Transport mode is SWO UART. This node does not have a value.
    `mode:`               |   Optional   | Trace: `off` (default), `server`, `file`.
    `server-port:`        |   Optional   | Set TCP/IP port number of trace server in `server` mode (default: 5555).
    `file:`               |   Optional   | Explicit path and name of the trace output file in `file` mode. Default: `<solution-name>+<target-type>@<target-set>.SWO.raw`.
    `input-clock:`        | **Required** | Trace input clock frequency in Hz.
    `output-clock:`       |   Optional   | Trace output clock frequency, i.e. the baudrate, for the SWO output.

#### `trace-buffer`

Configuration for the target device trace buffer. This type covers on-chip trace buffer variants like the Embedded Trace Buffer (ETB),
the Embedded Trace FIFO (ETF, in circular buffer mode), the Embedded Trace Router, and the Micro Trace Buffer (MTB).

Some of the listed on-chip trace buffer solutions provide sophisticated options to configure exact memory placement and bus access setup.
Such settings are often use-case and device specific. They are usually exposed through the device [`<debugvars>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debugvars),
and configured through the `device-settings:` or the `*.dbgconf` file.

`trace:`                                 |              | Description
:----------------------------------------|:-------------|:------------------------------------
`- trace-buffer:`                        | **Required** | Transport mode is (on-chip) trace buffer. See [Selecting Trace Buffers](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/Experimental-Features.md#selecting-trace-buffers) for value rules.
    `mode:`               |   Optional   | Trace: `off` (default), `server`, `file`.
    `server-port:`        |   Optional   | Set TCP/IP port number of trace server in `server` mode (default: 5555).
    `file:`               |   Optional   | Explicit path and name of the trace output file in `file` mode. Default: `<solution-name>+<target-type>@<target-set>.TB.raw`.

#### Trace Clocks

1. Trace `input-clock` is the frequency of the clock signal that goes into the trace port component. It equals the CPU clock frequency for the majority of systems with trace from a single core.
For more complex multi-core systems, the clock is normally derived from the system clock. Refer to the device manual and setup to find the exact value.
2. Trace `output-clock` is the clock frequency of the trace output signal. It is used to configure trace capture of the debug unit, and to calculate trace port prescaler values that need to be programmed. If not provided or if the value is `0`, then a best matching output frequency is automatically calculated based on `input-clock`, supported trace capture frequencies/baudrates of the debug unit, and other potentially known device-specific constraints like pin characteristics.

#### Debug Access Variables

The above configurations are passed to debug sequence implementations through [pre-defined debug access variables](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#DebugVars). The following mapping is expected:

- `input-clock` directly maps to variable [`__traceclockin`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#__traceclockin).
- If `output-clock` is provided and has a value other than `0`, then the value directly maps to variable [`__traceclockout`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#__traceclockout).
- If `output-clock` is not provided or has the value `0`, then the highest achievable output clock frequency supported by the debug unit is written to [`__traceclockout`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#__traceclockout).
- The selected transport mode (currently [`swo-uart`](#swo-uart) or [`trace-buffer`](#trace-buffer)) maps to bits `0..2` of variable [`__traceout`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#__traceout).
