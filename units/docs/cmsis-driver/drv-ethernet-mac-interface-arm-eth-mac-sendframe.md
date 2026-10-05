---
id: "drv-ethernet-mac-interface-arm-eth-mac-sendframe"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_SendFrame"
summary: "The function ARM_ETH_MAC_SendFrame writes an Ethernet frame to the Ethernet MAC transmit buffer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_SendFrame (const uint8_t *frame, uint32_t len, uint32_t flags)
```


The function **ARM_ETH_MAC_SendFrame** writes an **Ethernet frame** to the Ethernet MAC transmit buffer.

The Ethernet MAC transmit engine must be enabled by using the function ARM_ETH_MAC_Control (ARM_ETH_MAC_CONTROL_TX, 1) before a call to this function.

The frame data addressed by **buf** starts with MAC destination and ends with the last Payload data byte. The frame data is copied into 
the transmit buffer of the Ethernet MAC interface. The function does not wait until the transmission over the Ethernet is complete, 
however the memory addressed by **buf** is available for the next Ethernet frame after return.

The maximum value for **len** is implied by the size restrictions of the Ethernet frame but is not verified.
Using an invalid value for **len** may generate unpredicted results.

The parameter **flags** specifies additional attributes for the function as shown in the following table. Multiple flags can be combined, for example:
ARM_ETH_MAC_TX_FRAME_EVENT | ARM_ETH_MAC_TX_FRAME_TIMESTAMP.

Flag bit                               | Description
:--------------------------------------|:-----------------------------------------
ARM_ETH_MAC_TX_FRAME_FRAGMENT     | Indicates that it is a fragment of the frame. allows you to collect multiple fragments before the frame is sent.
ARM_ETH_MAC_TX_FRAME_EVENT        | ARM_ETH_MAC_SignalEvent with **event** bit ARM_ETH_MAC_EVENT_TX_FRAME set will be called when frame send is complete.
ARM_ETH_MAC_TX_FRAME_TIMESTAMP    | Capture the time stamp of the frame. The time stamp can be obtained using the function ARM_ETH_MAC_GetTxFrameTime.


**Example:**
```
  status = mac->SendFrame (&frame->data[0], frame->length, 0);
  if (status != ARM_DRIVER_OK)  {
    // error handling
  }
```

******************************************************************************************************************
