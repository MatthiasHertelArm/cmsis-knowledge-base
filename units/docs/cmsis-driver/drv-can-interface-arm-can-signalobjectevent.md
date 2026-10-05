---
id: "drv-can-interface-arm-can-signalobjectevent"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_SignalObjectEvent"
summary: "The function ARMCANSignalObjectEvent is a callback function registered by the function ARMCANInitialize and signals a CAN message object event."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
void ARM_CAN_SignalObjectEvent (uint32_t obj_idx, uint32_t event)
```


The function **ARM_CAN_SignalObjectEvent** is a callback function registered by the function ARM_CAN_Initialize and 
signals a CAN message object event. 

The parameter **obj_idx**  is the index of the message object. \n
The parameter **event** indicates object event that occurred during driver operation. 

The following events can be generated:

 Parameter **event**                 | Bit | Description
:------------------------------------|:---:|:-------------------------------------------------------------------------
 ARM_CAN_EVENT_SEND_COMPLETE    |  0  | Message was sent successfully by the **obj_idx** object.
 ARM_CAN_EVENT_RECEIVE          |  1  | Message was received successfully by the **obj_idx** object.
 ARM_CAN_EVENT_RECEIVE_OVERRUN  |  2  | Message was overwritten before it was read on the **obj_idx** object.

\sa ARM_CAN_MessageSend
\sa ARM_CAN_MessageRead
\sa ARM_CAN_ObjectConfigure
******************************************************************************************************************
