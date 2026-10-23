---
id: "sds-utilities-sdsio-control-file-sdsio-yml"
type: "concept"
domain: "test"
title: "Utilities: SDSIO Control File: `*.sdsio.yml`"
summary: "The SDSIO control file .sdsio.yml configures:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-control-file-sdsio-yml"
license: "Apache-2.0"
mode: "V"
---

The SDSIO control file `*.sdsio.yml` configures:

- For the [SDSIO-Server](#sdsio-server), the interface, workdir and steps for playback mode.
- For the [FVP simulation models (VSI3)](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_fvp), the interface, workdir, and steps for playback.
- For the [SDS extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-sds), it configures the SDSIO-Server and the user interface.

### `sdsio:`

`sdsio:`                                                    |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
    [`interface:`](#interface)               |   Optional   | SDSIO-Server only: specifies the interface used to connect to the target firmware (default: `usb`).
    `workdir:`                               |   Optional   | Directory containing `*.sds` files (default: current working directory). Relative paths are interpreted relative to the location of the `*.sdsio.yml` file. In AVH FVP simulations, the `*.sdsio.yml` file must reside in the simulator working directory.
    `write-flush-records:`                   |   Optional   | Force recorded SDS data to disk after this many records (`0` = after every record; default: disabled). The SDSIO-Server `--write-flush-records` command-line option overrides this setting.
    `metadir:`                               |   Optional   | Directory for metadata files (default: `workdir`). This key is used by the [SDS extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-sds).
    [`streams:`](#streams)                   |   Optional   | Data stream information used by the [SDS extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-sds).
    [`play:`](#play)                         |   Optional   | Playback step list that defines how `*.sds` files are played back (used in playback mode).
    [`flag-info:`](#flag-info)               |   Optional   | Human readable labels for user flags. This key is currently not used by SDSIO-Server or the VSI3 simulation interface.

### `interface:`

!!! Note
    - The `interface:` settings are used by SDSIO-Server. The AVH FVP VSI3 simulation interface ignores `interface:`.

`interface:`                                                |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
    [`usb:`](#usb)                           |   Optional   | Configure USB bulk interface.
    [`serial:`](#serial)                     |   Optional   | Configure serial (UART) interface.
    [`socket:`](#socket)                     |   Optional   | Configure TCP socket interface.

#### `usb:`

`usb:`                                                      |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
    `high_priority:`                         |   Optional   | SDSIO-Server only: increase process priority (default: `false`).

**Example:**

```yml
sdsio:
  interface:
    usb:                # configure for USB interface
```

#### `serial:`

`serial:`                                                   |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
    `port:`                                  | **Required** | Port name (examples: `COM3`, `ttyS0`, `ttyUSB1`, ...).
    `baudrate:`                              |   Optional   | Baudrate (default: `115200`).
    `parity:`                                |   Optional   | Parity bit: `none`, `even`, `odd`, `mark`, `space` (default: `none`).
    `stopbits:`                              |   Optional   | Stop bits: `1`, `1.5`, `2` (default: `1`).

**Example:**

```yml
sdsio:
  interface:
    serial:             # configure for Serial interface with baudrate 230400 bps.
      baudrate: 230400
```

#### `socket:`

`socket:`                                                   |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
    `ipaddr:`                                |   Optional   | IPv4 address to bind to in listen mode, or host address when using `connect:` (example: `192.168.0.100`); default for `connect:` is localhost `127.0.0.1`.
    `netif:`                                 |   Optional   | Network interface name (example: `eth0`); cannot be used with `ipaddr`.
    `port:`                                  |   Optional   | TCP port number (default: `5050`).
    `connect:`                               |   Optional   | When present, connect to `ipaddr` instead of listening; optional value is a message sent to the host when the connection is established (default: none).
    `connect-time:`                          |   Optional   | Duration in milliseconds to discard incoming data after the connection is established (default: `50`).

!!! Note
    - The `ipaddr:` and `netif:` options are mutually exclusive.
    - `connect:` requires `ipaddr:` and cannot be used with `netif:`.
    - `netif:` cannot be used in combination with `connect:`.

**Example:**

Configure for Network interface.

```yml
sdsio:
  interface:
    socket:             # configure for Network interface with default port
```

Configure for RTT interface via J-Link debug adapter.

```yml
sdsio:
  interface:
    socket:             # configure for RTT interface
      connect: "$$SEGGER_TELNET_ConfigStr=RTTCh;1$$"
      port: 19021
```

### `streams:`

The `streams:` node provides additional information about the SDS data streams to the [SDS extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-sds). It provides the context between the data streams and the display format.

`streams:`                                                  |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
`- name:`                                                   | **Required** | Name of the data stream.
    `view:`                                  |   Optional   | Format of the data stream for the viewer (signal, wav, image, heatmap, csv, csv2)

### `play:`

The `play:` node specifies one or more playback steps.
Each playback step defines the list of labels to play back for each opened SDS stream.
Playback steps are numbered from `0` in the order in which they appear in the `play:` list.

For one playback step, all files of the `labels:` list are concatenated and appear as one data stream for the firmware.
A pause (where the data stream needs to be closed and opened again by the firmware) is created with another `- step:` section.

`play:`                                                     |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
`- step:`                                                   |   Optional   | Descriptive text for the playback step.
    `recdir:`                                |   Optional   | Recording directory for generated `*.p.sds` files during playback; relative paths are relative to `workdir:`.
    `setflags:`                              |   Optional   | Set user flags (bitmask); example: `0x01`.
    `clearflags:`                            |   Optional   | Clear user flags (bitmask); example: `0x01`.
    `labels:`                                |   Optional   | List of label names that define the playback sequence.

**Example:**

```yml
sdsio:
  interface:
    usb:
  workdir: ./algorithm/SDS Recordings
  metadir: ./algorithm/SDS Recordings

  play:             # Playback script
    - step: "Playback: ML_In.0"
      labels: [ 0 ]
    - step: "Playback: ML_In.rock.1.sds + ML_In.rock.2.sds + ML_In.rock.3.sds"
      setflags: 0x02
      clearflags: 0x01
      labels: 
        - rock.1
        - rock.2
        - rock.3
```

### `flag-info:`

The `flag-info:` node provides human readable labels for the user flags 0..7.
This information is currently not used by SDSIO-Server; it is intended for UI tooling.

`flag-info:`                                                |              | Content
:-----------------------------------------------------------|:-------------|:------------------------------------
`- <flag-bit>:`                                             | **Required** | Maps the user flag bit position `0..23` to a human readable label.

**Example:**

```yml
sdsio:
  flag-info:
    - 0: Skip Algorithm A
    - 1: Inject fault condition
    - 7: Reserved
```
