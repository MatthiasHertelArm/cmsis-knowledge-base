---
id: "dap-dap-executecommands"
type: "concept"
domain: "debug"
title: "DAP_ExecuteCommands"
summary: "Execute multiple DAP commands from a single packet."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_ExecuteCommands_gr.html"
license: "Apache-2.0"
mode: "V"
---

Execute multiple DAP commands from a single packet.

Executes multiple DAP commands that are provided in a single packet. Packet size limitation for requests and responses needs to respected.

**DAP_ExecuteCommands Request:**
```
 | BYTE | BYTE **|+++++++++++++++++++|
 > 0x7F | NumCmd | Command Requests  |
 |******|********|+++++++++++++++++++|
```

  - **NumCmd:** Number of commands to execute
  - **Commands Requests**: Concatenated command requests

**DAP_ExecuteCommands Response:**
```
 | BYTE | BYTE **|+++++++++++++++++++|
 < 0x7F | NumCmd | Command Responses |
 |******|********|+++++++++++++++++++|
```

  - **NumCmd:** Number of commands executed
  - **Commands Responses**: Concatenated command responses

**Example**:

Execute two DAP_SWJ_Pins commands with DAP_Delay in between.

**Request:**
```
 | BYTE | BYTE | BYTE | BYTE ******| BYTE ******| WORD ****| BYTE | SHORT | BYTE | BYTE ******| BYTE ******| WORD ****|
 > 0x7F | 0x03 | 0x10 | Pin Output | Pin Select | Pin Wait | 0x09 | Delay | 0x10 | Pin Output | Pin Select | Pin Wait |
 |******|******|******|************|************|**********|******|*******|******|************|************|**********|
        |NumCmd| DAP_SWJ_Pins                              | DAP_Delay    | DAP_SWJ_Pins                              |
```

**Response:**
```
 | BYTE | BYTE | BYTE | BYTE *****| BYTE | BYTE **| BYTE | BYTE *****|
 < 0x7F | 0x03 | 0x10 | Pin Input | 0x09 | Status | 0x10 | Pin Input |
 |******|******|******|***********|******|********|******|***********|
        |NumCmd| DAP_SWJ_Pins     | DAP_Delay     | DAP_SWJ_Pins     |
```
