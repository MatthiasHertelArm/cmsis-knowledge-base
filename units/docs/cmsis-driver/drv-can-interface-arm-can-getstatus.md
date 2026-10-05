---
id: "drv-can-interface-arm-can-getstatus"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_GetStatus"
summary: "The function ARMCANGetStatus retrieves runtime information on CAN bus and CAN unit state."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_STATUS ARM_CAN_GetStatus (void)
```


The function **ARM_CAN_GetStatus** retrieves runtime information on CAN bus and CAN unit state.

The following defines give information about the current unit involvement in bus communication:

Unit State                             | Description
:--------------------------------------|:------------
ARM_CAN_UNIT_STATE_INACTIVE       | Unit state: Not active on the bus. Unit is in initialization state.
ARM_CAN_UNIT_STATE_ACTIVE         | Unit state: Active on the bus. Unit can generate active error frames.
ARM_CAN_UNIT_STATE_PASSIVE        | Unit state: Error passive. Unit is interacting on the bus but does not send active error frames.
ARM_CAN_UNIT_STATE_BUS_OFF        | Unit state: Bus-off. Unit does not participate on the bus but monitors it and can recover to active state.

The following defines are error codes of the last error that happened on the bus:

Last Error Code                        | Description
:--------------------------------------|:------------
ARM_CAN_LEC_NO_ERROR              | No error. There was no error since last read of status or last successful transmit or receive.
ARM_CAN_LEC_BIT_ERROR             | Bit error. The bit monitored is different than the bit sent (except during arbitration phase).
ARM_CAN_LEC_STUFF_ERROR           | Bit stuffing error. There were 6 consecutive same bit levels on the bus.
ARM_CAN_LEC_CRC_ERROR             | CRC error. CRC of received data is not as expected.
ARM_CAN_LEC_FORM_ERROR            | Illegal fixed-form bit. Error in fixed form bits.
ARM_CAN_LEC_ACK_ERROR             | Acknowledgment error. Message was not acknowledged by any receiver on the bus.

******************************************************************************************************************
