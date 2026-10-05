---
id: "dap-cmsis-dap-commands"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Commands"
summary: "Commands between a CMSIS-DAP debug probe and a host computer."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Commands_gr.html"
license: "Apache-2.0"
mode: "V"
---

Commands between a CMSIS-DAP debug probe and a host computer.


This section explains each command that is exchanged between the CMSIS-DAP compliant Debug probe and the host computer.

Every Command starts with a Command-ID and optional data. Depending on the Command, the CMSIS-DAP firmware replies with a Response that repeats the Command-ID and delivers additional data.

Command and Response data have a package size limitation that is defined with DAP_PACKET_SIZE.
This configuration setting can be obtained with the command DAP_Info and is used to
optimize the performance for Full-Speed or High-Speed USB. The debugger must ensure that each
data package fits within the limitations of the configured DAP_PACKET_SIZE.

**Note:**
Commands that are not implemented reply with 0xFF instead of repeating the command byte.

Conventions and Command Structure
---------------------------------

The following conventions describe the command semantic used in the following documentation:

 Symbol   | Description
--------- | ------------------------------------------------------------------------------------
 \>       | Prefix indicating the direction: Command from host to Debug Unit.
 \<       | Prefix indicating the direction: Response from Debug Unit to host.
 BYTE     | 8-bit value.
 SHORT    | 16-bit value (low byte first).
 WORD     | 32-bit value (low byte first).
 LWORD    | 64-bit value (low byte first).
 FLOAT    | 32-bit single precision floating point value (LSB first).
 0x01     | Fixed HEX value in C notation. Used for example to identify a command.
 Reserved | The field above is reserved for future extension.
 \*\*\*\* | The field above has exactly one occurrence.
 \+\+\+\+ | The field above has a variable length.
 //////// | The field above is repeated and may appear 0..n times.


The commands are described in a structure consisting of three lines.
  - The first line indicates the field type.
  - The second line indicates the communication direction and the command structure.
  - The third line indicates the occurrence of the field.

**Examples:**
```
 | BYTE | SHORT *| WORD ***|
 > 0x99 | RecLen | Data    |
 |******|********|+++++++++|
```

The Command with the Command-ID _0x99_ is sent from the host computer to the Debug Unit.
The value of _RecLen_ indicates the number of WORDS that follow with _Data_.
_Data_ is repeated several times depending on the value of _RecLen_.

Depending on the Command the Debug Unit may send a **Response**.
```
 | BYTE ***| WORD***********|
 < 0       | Register Value |
 |*Reserved|****************|
```
