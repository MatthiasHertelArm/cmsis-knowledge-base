---
id: "drv-can-interface-arm-can-msg-info"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_MSG_INFO"
summary: "Structure with information about the CAN message."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_MSG_INFO
```

      CAN Message Information

Structure with information about the CAN message.

In CAN mode, the following ARM_CAN_MSG_INFO data fields are ignored: **edl,** **brs,** **esi.** \n
In CAN FD mode, the following ARM_CAN_MSG_INFO data field is ignored: **rtr.**

**Parameter for:**
  - ARM_CAN_MessageSend
  - ARM_CAN_MessageRead

\sa can_filtering
\sa Remote_Frame
****************************************************************************************************************
