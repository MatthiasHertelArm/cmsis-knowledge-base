---
id: "drv-can-interface-remote-frame"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame"
summary: "In general, data transmission is performed on an autonomous basis with the data source node sending out Data Frames."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

In general, data transmission is performed on an autonomous basis with the data source node sending out Data Frames.

However, sending a **Remote Frame** allows a destination node to request the data from the source node.
The examples below shows the data exchange using a **Remote Transmission Request (RTR)**.

**Example for automatic Data Message response on RTR**

For automatic data message response on an RTR, the object is configured with the function ARM_CAN_ObjectConfigure **obj_cfg** = ARM_CAN_OBJ_RX_RTR_TX_DATA.

In this case, the function ARM_CAN_MessageSend sets a data message that is transmitted when an RTR with a matching CAN ID is received.
If  ARM_CAN_MessageSend was not called before the RTR is received, the response is hardware dependent (either last data message is repeated 
or no data message is sent until ARM_CAN_MessageSend is called).

After data transmission is completed, the driver calls a callback function ARM_CAN_SignalObjectEvent with **event** = ARM_CAN_EVENT_SEND_COMPLETE 
and the related **obj_idx.**

**Example:**
```
  status = ptrCAN->ObjectSetFilter(0, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x12345678U), 0U);
  if (status != ARM_DRIVER_OK) ... // error handling
  status = trCAN->ObjectConfigure(0, ARM_CAN_OBJ_RX_RTR_TX_DATA);
  if (status != ARM_DRIVER_OK) ... // error handling

  memset(&tx_msg_info, 0, sizeof(ARM_CAN_MSG_INFO));            // Clear transmit message structure
  tx_msg_info.id  = ARM_CAN_EXTENDED_ID(0x12345678U);           // Set ID of message
  data_buf[0] = '1';  data_buf[1] = '2';                        // Prepare data to transmit
  data_buf[2] = '3';  data_buf[3] = '4';
  data_buf[4] = '5';  data_buf[5] = '6';
  data_buf[6] = '7';  data_buf[7] = '8';
  ptrCAN->MessageSend(0, &tx_msg_info, data_buf, 8);            // Start send message that will be triggered on RTR reception
```

 
**Example for automatic Data Message reception using RTR**

For automatic data message reception on an RTR, the object is configured with the function ARM_CAN_ObjectConfigure **obj_cfg** = ARM_CAN_OBJ_TX_RTR_RX_DATA. 

The receiver or consumer requests data with transmission of an RTR with the ARM_CAN_MessageSend. This RTR requests from the transmitter or producer to send the data message.
Once the data message is received, the driver calls a callback function ARM_CAN_SignalObjectEvent with **event** = ARM_CAN_EVENT_RECEIVE
and the related **obj_idx.** The received data message can then be read with the function ARM_CAN_MessageRead. 

**Example:**
```
  status = ptrCAN->ObjectSetFilter(0, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x12345678U), 0U);
  if (status != ARM_DRIVER_OK) ... // error handling
  status = ptrCAN->ObjectConfigure(0, ARM_CAN_OBJ_TX_RTR_RX_DATA);
  if (status != ARM_DRIVER_OK) ... // error handling
  memset(&tx_msg_info, 0, sizeof(ARM_CAN_MSG_INFO));            // Clear transmit message structure
  tx_msg_info.id  = ARM_CAN_EXTENDED_ID(0x12345678U);           // Set ID of message
  tx_msg_info.rtr = 1;                                          // Set RTR flag of message to send RTR
  tx_msg_info.dlc = 1;                                          // Set data length code of message to 1 to request 1 data byte
  ptrCAN->MesageSend(0, &tx_msg_info, 0, 0);                    // Send RTR

  // Wait for ARM_CAN_EVENT_RECEIVE
  ptrCAN->MessageRead(0, &rx_msg_info, data_buf, 8);            // Read received message
```


****************************************************************************************************************
