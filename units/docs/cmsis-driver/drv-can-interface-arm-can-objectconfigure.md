---
id: "drv-can-interface-arm-can-objectconfigure"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_ObjectConfigure"
summary: "The function ARM_CAN_ObjectConfigure configures the message object, which can be a mailbox or FIFO. Refer to can_filtering for details."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_ObjectConfigure (uint32_t obj_idx, ARM_CAN_OBJ_CONFIG obj_cfg)
```


The function **ARM_CAN_ObjectConfigure** configures the message object, which can be a mailbox or FIFO.
Refer to can_filtering for details.

The parameter **obj_idx** specifies the message object index. \n
The parameter **obj_cfg** configures the **object** with values as shown in the following table.



| Parameter **obj_cfg | Object Configuration | supported when ARM_CAN_OBJ_CAPABILITIES data field |
|---|---|---|
| ARM_CAN_OBJ_INACTIVE | Deactivate object (default after ARM_CAN_Initialize) | always supported |
| ARM_CAN_OBJ_RX | Receive object; read received message with ARM_CAN_MessageRead. | **rx** = `1` |
| ARM_CAN_OBJ_TX | Transmit object; send message with ARM_CAN_MessageSend. | **tx** = `1` |
| ARM_CAN_OBJ_RX_RTR_TX_DATA | Remote_Frame Receive; when **RTR** is received data message is transmitted; set data message with ARM_CAN_MessageSend. | **rx_rtr_tx_data** = `1` |
| ARM_CAN_OBJ_TX_RTR_RX_DATA | Remote_Frame Transmit; a **RTR** is sent with ARM_CAN_MessageSend to trigger object reception; read received data message with ARM_CAN_MessageRead. | **tx_rtr_rx_data** = `1` |



When the **object** is deactivated, it is not used for data communication.

\sa ARM_CAN_ObjectSetFilter
*************************************************************************************************************************
