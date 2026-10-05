---
id: "dap-dap-queuecommands"
type: "concept"
domain: "debug"
title: "DAP_QueueCommands"
summary: "Queue multiple DAP commands provided in a multiple packets."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_QueueCommands_gr.html"
license: "Apache-2.0"
mode: "V"
---

Queue multiple DAP commands provided in a multiple packets.

Queues multiple DAP commands provided in multiple packets.
Queuing starts with the first packet that includes **DAP_QueueCommands** command and continues with all subsequent packets that also include this command.
Queued commands execute when a packet without **DAP_QueueCommands** command is received.
Packet size and count limitation for requests and responses needs to respected.

The command is similar to DAP_ExecuteCommands_gr on a packet level but queues multiple packets before processing them.

**DAP_QueueCommands Request:**
```
 | BYTE | BYTE **|+++++++++++++++++++|
 > 0x7E | NumCmd | Command Requests  |   First queued packet
 |******|********|+++++++++++++++++++|
  .
  .
  .
 | BYTE | BYTE **|+++++++++++++++++++|
 > 0x7E | NumCmd | Command Requests  |   Last queued packet
 |******|********|+++++++++++++++++++|
```

 - **>** Command Request (any command except **DAP_QueueCommands)**  \n
        Queued commands are executed before this command
 - **NumCmd:** Number of commands to queue (single packet)
 - **Commands Requests**: Concatenated command requests (single packet)

**DAP_QueueCommands Response:**
```
 | BYTE | BYTE **|+++++++++++++++++++|
 < 0x7F | NumCmd | Command Responses |
 |******|********|+++++++++++++++++++|
  .
  .
  .
 | BYTE | BYTE **|+++++++++++++++++++|
 < 0x7F | NumCmd | Command Responses |
 |******|********|+++++++++++++++++++|
```

 - **<** Command Response (first non **DAP_QueueCommands** command)
 - **NumCmd:** Number of commands executed (single packet)
 - **Commands Responses**: Concatenated command responses (single packet)

**Example:**

Queue DAP_SWJ_Pins and DAP_Delay in first packet. \n
Queue DAP_SWJ_Pins in second packet. \n
Queue DAP_Delay in third packet. \n
Send DAP_SWJ_Pins in fourth packet which executes queued commands and command in the last packet.

**Request:**

```
 | BYTE | BYTE | BYTE | BYTE ******| BYTE ******| WORD ****| BYTE | SHORT |
 > 0x7E | 0x02 | 0x10 | Pin Output | Pin Select | Pin Wait | 0x09 | Delay |
 |******|******|******|************|************|**********|******|*******|
   Queue|NumCmd| DAP_SWJ_Pins                              | DAP_Delay    |

 | BYTE | BYTE | BYTE | BYTE ******| BYTE ******| WORD ****|
 > 0x7E | 0x01 | 0x10 | Pin Output | Pin Select | Pin Wait |
 |******|******|******|************|************|**********|
   Queue|NumCmd| DAP_SWJ_Pins                              |

 | BYTE | BYTE | BYTE | SHORT |
 > 0x7E | 0x01 | 0x09 | Delay |
 |******|******|******|*******|
   Queue|NumCmd| DAP_Delay    |

 | BYTE | BYTE ******| BYTE ******| WORD ****|
 > 0x10 | Pin Output | Pin Select | Pin Wait |
 |******|************|************|**********|
   DAP_SWJ_Pins                              |
```

**Response:**

```
 | BYTE | BYTE | BYTE | BYTE *****| BYTE | BYTE **|
 < 0x7F | 0x02 | 0x10 | Pin Input | 0x09 | Status |
 |******|******|******|***********|******|********|
        |NumCmd| DAP_SWJ_Pins     | DAP_Delay     |

 | BYTE | BYTE | BYTE | BYTE *****|
 < 0x7F | 0x01 | 0x10 | Pin Input |
 |******|******|******|***********|
        |NumCmd| DAP_SWJ_Pins     |

 | BYTE | BYTE | BYTE | BYTE **|
 < 0x7F | 0x01 | 0x09 | Status |
 |******|******|******|********|
        |NumCmd| DAP_Delay     |

 | BYTE | BYTE *****|
 < 0x10 | Pin Input |
 |******|***********|
   DAP_SWJ_Pins     |
```
