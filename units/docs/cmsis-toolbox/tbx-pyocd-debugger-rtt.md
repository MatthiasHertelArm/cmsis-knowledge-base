---
id: "tbx-pyocd-debugger-rtt"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `rtt:`"
summary: "RTT is a software component that implements real-time transfer channels from the target system to the pyOCD Debugger for multiple processors."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#rtt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

[RTT](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/) is a software component that implements real-time transfer channels from the target system to the pyOCD Debugger for multiple processors.

(figure: Standard I/O Modes)

The `rtt:` node configures the RTT features and the RTT channel usage. At least one RTT channel must be configured for each processor to enable the RTT capturing in pyOCD.

!!! Note
    RTT is currently only enabled when using the pyOCD [run command](#run). It will be added in future pyOCD versions to the [gdbserver](#gdbserver).

`rtt:`                                                |              | Description
:-----------------------------------------------------|:-------------|:------------------------------------
`- pname:`                                            |   Optional   | Processor identifier (not required for single-core systems).
&nbsp;&nbsp;&nbsp; [`control-block:`](#control-block) |   Optional   | RTT control block configuration.
&nbsp;&nbsp;&nbsp; [`channel:`](#channel)             | **Required** | Channel configuration.

#### `control-block:`

The `control-block:` node configures the RTT control block discovery in pyOCD.

`control-block:`                                    |              | Description
:---------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `auto-detect:`                   |   Optional   | Scan default memory regions for the RTT control block signature: `true`, `false` (default).
&nbsp;&nbsp;&nbsp; `address:`                       |   Optional   | Explicit control block address; when combined with `size`, acts as scan start address.
&nbsp;&nbsp;&nbsp; `size:`                          |   Optional   | Scan length in bytes when `address` is provided.

pyOCD discovers the RTT control block using the prioritized steps for each core on the target:

1. `control-block:` provides an explicit `address:`:  
    a. `size:` is provided: pyOCD scans that memory range.  
    b. `size:` is not provided: pyOCD checks the provided explicit address.  
2. When `auto-detect: true` pyOCD scans default memory region (RAM) for the RTT control block signature. If multiple regions are marked as default, the region with the lowest start address is selected.
3. When `control-block:` is empty or not specified, pyOCD checks the ELF file for the symbol `_SEGGER_RTT` that specifies the control block location.

If the RTT control block cannot be found, RTT will be disabled for that core.

#### `channel:`

The `channel:` node selects the RTT channel mode.

`channel:`                                          |              | Description
:---------------------------------------------------|:-------------|:------------------------------------
`- number:`                                         | **Required** | Channel number.
&nbsp;&nbsp;&nbsp; `mode:`                          | **Required** | Channel mode selection: `stdio`, `server`, `file`, `systemview`, `systemview-server`.
&nbsp;&nbsp;&nbsp; `port:`                          |   Optional   | TCP port number (required for `server` and `systemview-server`).
&nbsp;&nbsp;&nbsp; `file-out:`                      |   Optional   | Path of the file that receives data from the RTT channel. Applies to `file` mode. Default: `<target>[_core<core>]_ch<channel>.out`.
&nbsp;&nbsp;&nbsp; `file-in:`                       |   Optional   | Path of the file that sends data to the RTT channel. Applies to `file` mode. Default: `<target>[_core<core>]_ch<channel>.in`; input is disabled when the file does not exist.

Channel Mode                  | Description
:-----------------------------|:------------------------------------
`stdio`                       | Connects channel to standard I/O service that is configured via the [`stdio:`](#stdio) node.
`server`                      | Exposes channel over a TCP server port.
`file`                        | Routes RTT channel data to and from files.
`systemview`                  | Saves channel data to *.SVDat file for [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) tool.<br/>Default file: `./out/<solution-name>+<target-type>.SVDat`; see [`systemview:`](#systemview) node.
`systemview-server`           | Streams live data to [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) tool over a "IP Recorder host" TCP port. Refer to the SEGGER SystemView user guide, IP Recorder.

**Examples:**

Enable RTT with standard I/O on channel 0 and configure explicit control block:

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  rtt:
    - pname: Core0
      control-block:
        address: 0x20000000
        size: 0x00020000
      channel:
        - number: 0
          mode: stdio
```

Enable RTT with standard I/O on channel 0 and map RTT channel 2 to a Telnet Server port `4444` and channel 3 to a Telnet Server port `4445`:

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  rtt:
    - pname: Core0
      channel:
        - number: 0
          mode: stdio
        - number: 2
          mode: server
          port: 4444
        - number: 3
          mode: server
          port: 4445
```

Map RTT channel 2 to input and output files:

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  rtt:
    - pname: Core0
      channel:
        - number: 2
          mode: file
          file-out: ./out/Blinky.out
          file-in: ./out/Blinky.in
```
