---
id: "tbx-pyocd-debugger-stdio"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `stdio:`"
summary: "pyOCD integrates a standard I/O service for character I/O functions via Semihosting or SEGGER RTT. Each processor that runs an independent application can be controlled individually."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#stdio"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

pyOCD integrates a standard I/O service for character I/O functions via Semihosting or [SEGGER RTT](#rtt). Each processor that runs an independent application can be controlled individually.

(figure: Standard I/O Modes)

The `stdio:` node configures:

- Server port for connecting remote tools, for example the [Serial Monitor VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-serial-monitor).
- Redirect the output to a `file`, `console`, `server`, or `monitor`. The setting `monitor` connects a Telnet server `port` to the Serial Monitor in VS Code. The default output file and location is derived from the [`cbuild-run.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#run-and-debug-management) and uses the extension `<pname>.out`, format: `<solution-name>+<target-type>.<pname>.out`

`stdio:`                       |              | Description
:------------------------------|:-------------|:------------------------------------
`- mode:`                      | **Required** | Redirect output: `off` (default), `server`, `file`, `console`, `monitor`.
    `pname:`    |   Optional   | Identifies the processor (not required for single core system).
    `port:`     |   Optional   | Set TCP/IP port number of Telnet Server (default: 4444, 4445, ... incremented for each processor).
    `file-in:`  |   Optional   | Explicit path and name of the input file. Default: `./out/\<solution-name\>+\<target-type\>.\<pname\>.in`
    `file-out:` |   Optional   | Explicit path and name of the output file. Default: `./out/\<solution-name\>+\<target-type\>.\<pname\>.out`

Standard I/O Mode              | Description
:------------------------------|:--------------------------------------
`server`                       | Serial I/O to Telnet server port.
`file`                         | Serial I/O to text files. Default: `./out/\<solution-name\>+\<target-type\>.\<pname\>.{in \| out}`
`console`                      | Serial output to console (Debug console in VS Code).
`monitor`                      | Serial I/O via TCP/IP port to VS Code Serial Monitor.
`off`                          | Serial I/O disabled.

!!! Note
    - When no `stdio` node is applied, Serial I/O to all processors is disabled.

!!! Info
    - Use `stdio:` for new configurations. The legacy `telnet:` node remains supported as an alias for backward compatibility.

The [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension for VS Code simplifies the configuration and the examples below show the setup in a `*.csolution.yml` file.

(figure: Standard I/O Configuration Dialog)

**Examples:**

Enable standard I/O service for a single core system.

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  stdio:
    - mode: monitor          # Output via TCP/IP port to VS Code Serial Monitor
```

Enable standard I/O service for a single core system.

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  stdio:
    - mode: server
```

Enable standard I/O service for a multi core system.

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  stdio:
    - pname: Core0          # enable standard I/O service with default settings
      mode: server
      port: 4444
    - pname: Core1
      mode: console         # route standard I/O to console
    - pname: Core2
      mode: file            # route standard I/O to files
      file-in: Blinky+MyTarget.Core2.in
      file-out: Blinky+MyTarget.Core2.out
```
