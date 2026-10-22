---
id: "tbx-theory-of-operation-user-interface"
type: "concept"
domain: "project"
title: "Theory of Operation: Debug Adapter Integration / User Interface"
summary: "The file debug-adapters.yml also contains the information for the user interface that is available in the VS Code CMSIS Solution extension. The options are added"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#user-interface"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debug Adapter Integration_

The file `debug-adapters.yml` also contains the information for the user interface that is available in the VS Code CMSIS Solution extension.
The options are added 

`user-interface:`                                       |            | Content
:-------------------------------------------------------|:-----------|:------------------------------------
`- section:`                                            |**Required**| Label text for configuration section.
    `description:`                       |  Optional  | Hover over text.
    `yml-node:`                          |  Optional  | If present, options are under this group node in the `debugger:` section. 
    `select:`                            |  Optional  | If present, the section can be enabled. Applies to all options. 
    `options:`                           |  Optional  | List of available options.
    `pname-options:`                     |  Optional  | List of available options that are repeated for each pname.

!!! Note
    When a `section:` is disabled all nodes are removed from the `csolution.yml` file.

`options:`                                              |            | Content
:-------------------------------------------------------|:-----------|:------------------------------------
`- name:`                                               |**Required**| Label text for the option in the user interface.
    `description:`                       |  Optional  | Hover over text.
    `yml-node:`                          |**Required**| Name of the node in the csolution file under `debugger:` section.
    `type:`                              |**Required**| Type (enum: value list, number: value, string: name, file: name).
    `range:`                             |  Optional  | Value range for type int.
    `values:`                            |  Optional  | Value list for type enum.
    `path-type:`                         |  Optional  | Only valid if `type:` is `file`. Possible values: `absolute` or `relative` (default).
    `default:`                           |  Optional  | Default value (or enum name) for user interface when no value given in csolution.yml.
    `scale:`                             |  Optional  | The value in csolution.yml value is multiplied by the scale factor.

`values:`                                               |            | Content
:-------------------------------------------------------|:-----------|:------------------------------------
`- name:`                                               |**Required**| Label text for the option in the user interface.
    `value:`                             |  Optional  | Value used for the enum name in csolution.yml file. If empty, `name` is used as `value`.
    `description:`                       |  Optional  | Descriptive text (hover over or sub-text in dialog).

**Example**

(figure: Debug Adapter User Interface)

```yml
solution:
   :
      target-set:
        - set:
          debugger:
            name: CMSIS-DAP@pyOCD
            protocol: swd
            clock: 10000000             # SWD clock = 10MHz
            trace:
              - swo-uart:               # Trace mode is SWO UART
                input-clock: 120000000  # Trace clock = 120 MHz
            stdio:                      # Enable standard I/O with defaults
```
 
**Example `debug-adapters.yml`**

```yml
debug-adapters:
  - name: "CMSIS-DAP@pyOCD"
    alias-name: ["CMSIS-DAP", "DAP-Link"] # alternative names that map to this debug adapter
    template: CMSIS-DAP-pyOCD.adapter.json # template file
    gdbserver: # add gdbserver: node under debugger: in cbuild-run.yml
    defaults: # this section is only used by csolution to provide default values when settings are missing
      port: 3333 # default value of first gdbserver port
      protocol: swd
      clock: 1000
    user-interface:  # this section is only used by the UI to display and edit settings
      - section: Debug Interface
        description: Interface configuration for the debug port
        options:
        - name: Clock (kHz)       # UI display
          description: Trace configuration   # hover over text
          yml-node: clock          # node entry in csolution.yml
          type: int                # type of value
          range: [10, 5000]        # valid range
          default: 1000            # default value if not specified anywhere
        - name: Protocol
          yml-node: protocol
          type: enum
          values: 
            - name: JTAG
              value: jtag
            - name: SWD
              value: swd
          default: SWD
      - section: Trace
        description: Trace configuration   # hover over text
        yml-node: trace                    # when a yml node is given options are under this section
        select: off
        options:
          - name: Clock (kHz)
            yml-node: trace-clock
            type: number
            range: [10, 200000] # 10 kHz .. 200 MHz
            default: 12000
          - name: Mode
            yml-node: trace-port
            type: enum
            values: 
              - name: UART                 # UART is also used as value
                description: SWO configured for UART protocol
              - name: Manchester
                value: Man
                description: SWO configured for Manchester protocol
              - name: Trace Port 4
                value: TP4
                description: Connection via 4-bit Trace port
            default: UART
      - section: Standard I/O
        description: Serial input/output via semihosting or RTT channel 0
        yml-node: stdio
        select: on
        pname-options:
        options:
          - name: Standard I/O Mode
            description: Configure Serial I/O redirect
            yml-node: mode
            type: enum
            default: monitor
            values:
              - name: Telnet Server
                value: server
                description:  Serial I/O to Telnet server port
              - name: Debug Console
                value: console
                description:  Serial output to console (Debug console in VS Code)
              - name: Serial Monitor
                value: monitor
                description:  Serial I/O via TCP/IP port to VS Code Serial Monitor
              - name: Text File
                value: file
                description:  Serial output to file (default ./out/<solution-name>+<target-type>.<pname>.out)
              - name: Disabled
                value: off
                description:  Serial I/O disabled
 
  - name: "J-Link Server"
      - section: Debug Interface
        description: Interface configuration for the debug port
        options:
        - name: Clock (kHz)       # UI display
          description: JTAG/SWO clock frequency   # hover over text
          yml-node: clock          # node entry in csolution.yml
          type: number             # type of value
          range: [10, 5000]        # valid range
          default: 4000            # default value if not specified anywhere
        - name: Protocol
          yml-node: protocol
          type: enum
          values: 
            - name: SWD
              value: swd
          default: SWD
      - section: Trace
        description: Trace configuration   # hover over text
        yml-node: trace                    # only on/off option
        select: off
        options:
          - name: Mode
            yml-node: trace-port
            type: enum
            values:
              name: UART
            default: UART

  - name: "Keil uVision"
    template: uVision.adapter.json # template file
    defaults:
      uv4: "C:\\Keil_v5\\UV4\\UV4.exe"
      args: []
    user-interface:  # this section is only used by the UI to display and edit settings
      - section: Setup
        description: Configure uVision settings
        options:
        - name: Path
          description: Absolute path to uVision executable
          yml-node: uv4            # node entry in csolution.yml
          type: file               # type of value
          default: "C:\\Keil_v5\\UV4\\UV4.exe"
```
