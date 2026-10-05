---
id: "drv-ethernet-mac-interface-arm-eth-mac-readframe"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_ReadFrame"
summary: "The function ARM_ETH_MAC_ReadFrame reads an Ethernet frame from the Ethernet MAC receive buffer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_ReadFrame (uint8_t *frame, uint32_t len)
```


The function **ARM_ETH_MAC_ReadFrame** reads an **Ethernet frame** from the Ethernet MAC receive buffer.

The Ethernet MAC receive engine must be enabled using the function ARM_ETH_MAC_Control (ARM_ETH_MAC_CONTROL_RX , 1) before a call to this function.
The **len** of the Ethernet frame can be checked using the function ARM_ETH_MAC_GetRxFrameSize.

The frame data addressed by **buf** starts with MAC destination and ends with the last Payload data byte. The frame data is read from 
the receive buffer of the Ethernet MAC interface and the number of bytes written into the memory addressed by **buf** is returned.
A negative return value indicates an error whereby the status code is defined with driver common return codes.

The function ARM_ETH_MAC_ReadFrame may be called with **buf** = NULL and **len** = 0 to discard or release an frame. This is useful when an incorrect frame has been received or
no memory is available to hold the Ethernet frame.

**Example:**
```
  size = mac->GetRxFrameSize ();
  if ((size < 14) || (size > 1514)) {    // frame excludes CRC
    mac->ReadFrame (NULL, 0);            // Frame error, release it
  }
  len = mac->ReadFrame (&frame->data[0], size);
  if (len < 0)  {
    // error handling
  }
```
******************************************************************************************************************
