---
id: "sds-theory-sdsio-server-firmware-protocol"
type: "concept"
domain: "test"
title: "theory: SDSIO-Server Firmware Protocol"
summary: "The SDSIO-Server uses a simple protocol for data exchange between a host computer and the embedded target that integrates an SDSIO Interface."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sdsio-server-firmware-protocol"
license: "Apache-2.0"
mode: "V"
---

The [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-server) uses a simple protocol for data exchange between a host computer and the embedded target that integrates an [SDSIO Interface](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md). The protocol assumes that communication to the SDSIO-Server is ensured by the underlying transport technology (TCP/IP or USB); therefore, no additional checks are implemented.

The following conventions describe the **command semantics** used in the following documentation:

Symbol     | Description
:----------|:----------------------
\>         | Prefix indicating the direction: Command from target firmware to SDSIO-Server on the host computer.
<          | Prefix indicating the direction: Response from SDSIO-Server to target firmware.
WORD       | 32-bit value (low byte first).
****       | The field above has exactly one occurrence.
++++       | The field above has a variable length.

**Commands:**

Commands are sent from the embedded target to the host computer running the SDSIO-Server.

ID  | Name            | Description
:--:|:----------------|:------------------------
1   | SDSIO_CMD_OPEN  | Open an SDS data file
2   | SDSIO_CMD_CLOSE | Close an SDS data file
3   | SDSIO_CMD_WRITE | Write to an SDS data file
4   | SDSIO_CMD_READ  | Read from an SDS data file
5   | SDSIO_CMD_PING  | Ping SDSIO-Server
6   | SDSIO_CMD_FLAGS | SDS control flags update request from host
7   | SDSIO_CMD_INFO  | Send control information to host

Each **Command** starts with a **Header (4 Words = 16 bytes)** followed by **optional data** of variable length.
Depending on the Command, the SDSIO-Server replies with a **Response** that includes a **Header** with the same ID
as the Command and may contain **additional data**.

!!! Note
    - The SDSIO_CMD_FLAGS Response is not a reply to the SDSIO_CMD_FLAGS Command; rather, it is an asynchronous Response sent by the host.

**SDSIO_CMD_OPEN**

The Command with ID = **1** (SDSIO_CMD_OPEN) opens an SDS data file on the host computer.
`Mode` defines `read` (value = 0) or `write` (value = 1) operation. `Len of Stream Name` is the size of the string in bytes.

SDS data filenames use the following file format: `<name>.<label>.sds`, where `<name>` is the stream name used as the base filename
of the SDS data file and `<label>` is a user label or index depending on usage (for details see section [Filenames](#filenames)).

```txt
| WORD |  WORD  | WORD | WORD **************|+++++++++++++|
>  1   |   0    | Mode | Len of Stream Name | Stream Name |
|******|********|******|********************|+++++++++++++|
```

The Response with ID = **1** (SDSIO_CMD_OPEN) provides a `Handle` that is used to identify the file in subsequent Commands.

```txt
| WORD |  WORD  | WORD | WORD *******|
<  1   | Handle | Mode | 0           |
|******|********|******|*************|
```

**SDSIO_CMD_CLOSE**

The Command with ID = **2** (SDSIO_CMD_CLOSE) closes an SDS data file on the host computer.
The `Handle` is the identifier obtained with **SDSIO_CMD_OPEN**.
There is no Response from the SDSIO-Server to this Command.

```txt
| WORD |  WORD  | WORD | WORD |
>  2   | Handle |  0   |  0   |
|******|********|******|******|
```

**SDSIO_CMD_WRITE**

The Command with ID = **3** (SDSIO_CMD_WRITE) writes data to an SDS data file on the host computer.
The `Handle` is the identifier obtained with **SDSIO_CMD_OPEN**.
`Size` specifies the size of `Data` in bytes.
There is no Response from the SDSIO-Server to this Command.

```txt
| WORD |  WORD  | WORD | WORD |++++++|
>  3   | Handle |  0   | Size | Data |
|******|********|******|******|++++++|
```

**SDSIO_CMD_READ**

The Command with ID = **4** (SDSIO_CMD_READ) reads data from an SDS data file on the host computer.
The `Handle` is the identifier obtained with **SDSIO_CMD_OPEN**.
`Size` specifies the number of bytes to read.

```txt
| WORD |  WORD  | WORD | WORD |
>  4   | Handle | Size |  0   |
|******|********|******|******|
```

The Response with ID = **4** (SDSIO_CMD_READ) provides the data read from an SDS data file on the host computer.
`Size` specifies the size of `Data` in bytes that was read and `Status` with nonzero = end of stream, else 0.

```txt
| WORD |  WORD  |  WORD  | WORD |++++++|
<  4   | Handle | Status | Size | Data |
|******|********|********|******|++++++|
```

**SDSIO_CMD_PING**

The Command with ID = **5** (SDSIO_CMD_PING) verifies if the SDSIO-Server is active and reachable on the host.

```txt
| WORD | WORD | WORD | WORD |
>  5   |  0   |  0   |  0   |
|******|******|******|******|
```

The Response with ID = **5** (SDSIO_CMD_PING) returns the `Status` with nonzero = server active, else 0.

```txt
| WORD | WORD |  WORD  | WORD |
<  5   |  0   | Status |  0   |
|******|******|********|******|
```

**SDSIO_CMD_FLAGS**

The asynchronous Response with ID = **6** (SDSIO_CMD_FLAGS) contains the SDS control flags update information from the host.
This Response can arrive at any time when the host wants to update the SDS control flags.
It can also precede a Response to any other command (e.g., SDSIO_CMD_OPEN or SDSIO_CMD_READ), but it cannot be sent by the host
while a Response to another Command is in progress.
The `Set Mask` specifies the bits to set in the `sdsFlags` and the `Clear Mask` specifies the bits to clear in the `sdsFlags`.

```txt
| WORD | WORD     | WORD       | WORD |
<  6   | Set Mask | Clear Mask |  0   |
|******|**********|************|******|
```

**SDSIO_CMD_INFO**

The Command with ID = **7** (SDSIO_CMD_INFO) sends control information (sdsFlags, sdsIdleRate and error information) to the host. There is no Response from the SDSIO-Server to this Command.

- `sdsFlags` is the current value of that global variable.
- `sdsIdleRate` is the current value of that global variable, value 0xFFFFFFFF indicates that idle rate information is not valid.
- `Error Len` specifies the size of the `Error Data`, value 0 indicates that no error occurred.

```txt
| WORD | WORD     | WORD        | WORD      |++++++++++++|
>  7   | sdsFlags | sdsIdleRate | Error Len | Error Data |
|******|**********|*************|***********|++++++++++++|
```

`Error Data` contains the information from `sdsError` global structure and has the following format.

```txt
| WORD   | WORD |+++++++++++++++++++|
| Status | Line | Filename (string) |
|********|******|+++++++++++++++++++|
```
