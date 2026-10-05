---
id: "drv-can-interface-arm-can-control"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_Control"
summary: "The function ARM_CAN_Control controls the CAN interface settings and executes various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_Control (uint32_t control, uint32_t arg)
```


The function **ARM_CAN_Control** controls the CAN interface settings and executes various operations.

The parameter **control** specifies various operations that are listed in the table below.

The parameters **arg** provides, depending on the **control** value, additional information or set values.

Parameter **control**                        | Operation
:--------------------------------------------|:------------------------------
ARM_CAN_SET_FD_MODE                     | Select **CAN FD** mode; **arg** : `0` = CAN 2.0B; `1` = CAN FD.
ARM_CAN_ABORT_MESSAGE_SEND              | Abort sending of CAN message;      **arg** : object index
ARM_CAN_CONTROL_RETRANSMISSION          | Enable/disable automatic retransmission; **arg** : `0 = disable, 1 = enable (default state)`
ARM_CAN_SET_TRANSCEIVER_DELAY           | Set transceiver delay; **arg** : delay in time quanta 

Verify the CAN interface capabilities with ARM_CAN_GetCapabilities.
******************************************************************************************************************
