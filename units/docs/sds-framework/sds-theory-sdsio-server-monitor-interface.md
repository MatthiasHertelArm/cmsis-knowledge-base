---
id: "sds-theory-sdsio-server-monitor-interface"
type: "concept"
domain: "test"
title: "theory: SDSIO-Server Monitor Interface"
summary: "The SDSIO-Server provides an additional TCP socket that may be used by a monitor program to observe SDS file activity and control sdsFlags in the firmware. The monitor interface is enabled with command line option --mon-port <port>."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#sdsio-server-monitor-interface"
license: "Apache-2.0"
mode: "V"
---

The [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-server) provides an additional TCP socket that may be used by a monitor program to observe
SDS file activity and control `sdsFlags` in the firmware.
The monitor interface is enabled with command line option `--mon-port <port>`.

The following conventions describe the **command and message semantics** used in the following documentation:

Symbol     | Description
:----------|:----------------------
\>         | Prefix indicating the direction: Command sent from the Monitor program to the SDSIO-Server.
<          | Prefix indicating the direction: Response or asynchronous message sent from the SDSIO-Server to the Monitor program.
WORD       | 32-bit value (low byte first).
****       | The field above has exactly one occurrence.
++++       | The field above has a variable length.

**Commands and Messages:**

Commands are sent to the SDSIO-Server which replies with a response (depending on command).
SDSIO-Server can also send asynchronous messages at any time when not processing a command.

ID  | Name               | Description
:--:|:-------------------|:------------------------
1   | SDSIO_MON_OPEN     | Information about the SDS file open operation (message)
2   | SDSIO_MON_CLOSE    | Information about the SDS file close operation (message)
6   | SDSIO_MON_FLAGS    | Monitor program request to the SDSIO-Server to update SDS control flags in the firmware and optionally select a play step
7   | SDSIO_MON_INFO     | Information update received from the firmware and forwarded to the Monitor program (message)
8   | SDSIO_MON_SHUTDOWN | Monitor program request to the SDSIO-Server to complete current tasks and shut down gracefully

Each **Command or Message** starts with a **Header (4 Words = 16 bytes)** followed by **optional data** of variable length.
Depending on the Command, the SDSIO-Server replies with a **Response** that includes a **Header** with the same ID
as the Command and may contain **additional data**.

**SDSIO_MON_OPEN**

The Message with ID = **1** (SDSIO_MON_OPEN) is sent whenever an SDS data file is opened by the SDSIO-Server.
`Mode` defines `read` (value = 0) or `write` (value = 1) operation. `Filename Len` is the size of the string in bytes and `Filename` is the name of the file (including path).

```txt
| WORD | WORD | WORD | WORD | WORD ********|++++++++++|
<  1   |  0   | Mode |  0   | Filename Len | Filename |
|******|******|******|******|**************|++++++++++|
```

**SDSIO_MON_CLOSE**

The Message with ID = **2** (SDSIO_MON_CLOSE) is sent whenever an SDS data file is closed by the SDSIO-Server.
`Filename Len` is the size of the string in bytes and `Filename` is the name of the file (including path).

```txt
| WORD | WORD | WORD | WORD | WORD ********|++++++++++|
<  2   |  0   |  0   |  0   | Filename Len | Filename |
|******|******|******|******|**************|++++++++++|
```

**SDSIO_MON_FLAGS**

The Command with ID = **6** (SDSIO_MON_FLAGS) is used by the Monitor program to request an update of the SDS control flags in the firmware.
The `Set Mask` specifies the bits to set in the `sdsFlags` and the `Clear Mask` specifies the bits to clear in the `sdsFlags`.
The `Play Step` value selects a `play:` step from the `*.sdsio.yml` file before the flag update is applied.
This command does not generate a response from the SDSIO-Server.

```txt
| WORD | WORD     | WORD       | WORD      |
>  6   | Set Mask | Clear Mask | Play Step |
|******|**********|************|***********|
```

The `Play Step` field accepts a zero-based step number or the special all-steps value:

- `0` to `N - 1`: select one of the `N` configured `play:` steps (`0` selects the first step).
- `0xFFFFFFFF`: select all configured `play:` steps.

Selecting a `Play Step` does not start playback by itself. To select and start a play step, set the `SDS_FLAG_START` and `SDS_FLAG_PLAYBACK` bits in `Set Mask` together with the desired `Play Step` value.
When `Play Step` is `0xFFFFFFFF`, the SDSIO-Server automatically starts each subsequent step after the previous step completes.

**SDSIO_MON_INFO**

The Message with ID = **7** (SDSIO_MON_INFO) contains status information received by the SDSIO-Server from the firmware,
including sdsFlags, sdsIdleRate, and error information.
The message is sent to the Monitor program whenever the SDSIO-Server receives updated information from the firmware,
as well as upon the initial connection to the Monitor program.

- `sdsFlags` is the current value of that global variable in the firmware.
- `sdsIdleRate` is the current value of that global variable in the firmware, value 0xFFFFFFFF indicates that idle rate information is not valid.
- `Error Len` specifies the size of the `Error Data`, value 0 indicates that no error occurred in the firmware.

```txt
| WORD | WORD     | WORD        | WORD      |++++++++++++|
<  7   | sdsFlags | sdsIdleRate | Error Len | Error Data |
|******|**********|*************|***********|++++++++++++|
```

`Error Data` contains the information from `sdsError` global structure and has the following format.

```txt
| WORD   | WORD |+++++++++++++++++++|
| Status | Line | Filename (string) |
|********|******|+++++++++++++++++++|
```

**SDSIO_MON_SHUTDOWN**

The Command with ID = **8** (SDSIO_MON_SHUTDOWN) is used by the Monitor program to request the SDSIO-Server to complete any ongoing operations,
signal to the firmware that it will stop operating, and shut down gracefully.

```txt
| WORD | WORD | WORD | WORD |
>  8   |  0   |  0   |  0   |
|******|******|******|******|
```

!!! Note
    When shutdown is initiated, all data streams will be closed by the SDSIO-Server. Ideally it should be initiated when the user application has completed playback or recording and closed all data streams.
