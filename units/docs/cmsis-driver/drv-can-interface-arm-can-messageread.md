---
id: "drv-can-interface-arm-can-messageread"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_MessageRead"
summary: "The function ARM_CAN_MessageRead reads the message received on the CAN bus, if obj_idx was configured for reception or for automatic Data Message reception using RTR and the callback function ARM_CAN_SignalObjectEvent was called signalling ARM_CAN_EVENT_RECEIVE."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_MessageRead (uint32_t obj_idx, ARM_CAN_MSG_INFO *msg_info, uint8_t *data, uint8_t size)
```


The function **ARM_CAN_MessageRead** reads the message received on the CAN bus, if **obj_idx** was configured for reception or 
for automatic Data Message reception using RTR and the callback function ARM_CAN_SignalObjectEvent was called 
signalling ARM_CAN_EVENT_RECEIVE.
If the message was overrun by another received message, then the callback function ARM_CAN_SignalObjectEvent
will be called signalling ARM_CAN_EVENT_RECEIVE_OVERRUN.

The function can read a maximum of `8` data bytes for CAN and `64` bytes for CAN FD.

The parameter **obj_idx** specifies the message object index. \n
The parameter **msg_info** is a pointer to the CAN information structure. \n
The parameter **data** is a pointer to the data buffer for reading data. \n
The parameter **size** is data buffer size in bytes and indicates the maximum number of bytes that can be read.

The function returns the number of read data in bytes or the execution_status.

All data fields of the structure ARM_CAN_MSG_INFO are updated as described below:
    - id:  Identifier of the message that was received, bit `31` specifies if it is a `11-bit` identifier or `29-bit` identifier.
    - rtr: `1` = Remote Frame Request was received (**dlc** is number of requested bytes).  `0` = data message
    - edl: `1` = CAN FD Extended Data Length message was received.  `0` = not Extended Data Length message.
    - brs: `1` = CAN FD Bit Rate Switching was used for message transfer. `0` = no Bit Rate Switching was used.
    - esi: `1` = CAN FD Error State Indicator is active for received message.  `0` = Error State Indicator is not active.
    - dlc: Data Length Code is the number of data bytes in the received message or number of data bytes requested by RTR.

Message reception can be disabled by de-configuring the receive object with the function ARM_CAN_ObjectConfigure.
*************************************************************************************************************************
