---
id: "drv-can-interface-arm-can-messagesend"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_MessageSend"
summary: "The function ARMCANMessageSend sends a CAN message on the CAN bus, or sets data message that will be automatically returned upon RTR reception with matching CAN ID."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_MessageSend (uint32_t obj_idx, ARM_CAN_MSG_INFO *msg_info, const uint8_t *data, uint8_t size)
```


The function **ARM_CAN_MessageSend** sends a CAN message on the CAN bus, or sets data message that will be automatically returned upon RTR reception with matching CAN ID.

Only one message can be sent with a call to this function (for CAN up to `8` bytes; for CAN FD up to `64` bytes of data).
A message transmission can be terminated with a call to the function ARM_CAN_Control with **control** = ARM_CAN_ABORT_MESSAGE_SEND.

The parameter **obj_idx** specifies the message object index. 

The parameter **msg_info** is a pointer to the structure ARM_CAN_MSG_INFO, which contains the following relevant data fields for sending message:
    - **id:**  Identifier of the message; bit `31` specifies if this is an `11-bit` or `29-bit` identifier.
    - **rtr:** Specifies if Remote Transmission Request should be sent (**dlc** is used for number of requested bytes), otherwise the data message will be sent. Refer to Remote_Frame for details.
    - **edl:** Specifies if Extended Data Length is used; for CAN FD, message can contain up to `64` data bytes.
    - **brs:** Specifies if Bit Rate Switching is to be used; for CAN FD, the bit rate can be increased during data phase.
    - **dlc:** Data Length Code of requested data bytes when sending Remote Transmission Request.

The parameter **data** is a pointer to the data buffer.\n
The parameter **size** is the number of data bytes to send.\n

The function returns the number of bytes accepted to be sent or ARM_DRIVER_ERROR_BUSY if the hardware is not
ready to accept a new message for transmission.

When the message is sent, the callback function ARM_CAN_SignalObjectEvent is called signalling ARM_CAN_EVENT_SEND_COMPLETE
on specified object.

\sa can_filtering

**Example:**

```
  status = ptrCAN->ObjectConfigure(0, ARM_CAN_OBJ_TX);
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  memset(&tx_msg_info, 0, sizeof(ARM_CAN_MSG_INFO));            // Clear transmit message structure
  tx_msg_info.id  = ARM_CAN_EXTENDED_ID(0x12345678U);           // Set ID of message
  data_buf[0] = '1';  data_buf[1] = '2';                        // Prepare data to transmit
  data_buf[2] = '3';  data_buf[3] = '4';
  data_buf[4] = '5';  data_buf[5] = '6';
  data_buf[6] = '7';  data_buf[7] = '8';
  status = ptrCAN->MesageSend(0, &tx_msg_info, data_buf, 8);    // Send message
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
```
*************************************************************************************************************************
