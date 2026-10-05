---
id: "drv-sai-interface-arm-sai-signalevent"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_SignalEvent"
summary: "The function ARMSAISignalEvent is a callback function registered by the function ARMSAIInitialize."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
void ARM_SAI_SignalEvent (uint32_t event)
```


The function **ARM_SAI_SignalEvent** is a callback function registered by the function ARM_SAI_Initialize. 

The parameter **event** indicates one or more events that occurred during driver operation.
Each event is encoded in a separate bit and therefore it is possible to signal multiple events within the same call. 

The following events can be generated:

Parameter **event**                        | Bit | Description 
------------------------------------------ |:---:|:-----------
ARM_SAI_EVENT_SEND_COMPLETE           |  0  | Occurs after call to ARM_SAI_Send to indicate that all the data has been sent (or queued in transmit buffers). The driver is ready for the next call to ARM_SAI_Send.
ARM_SAI_EVENT_RECEIVE_COMPLETE        |  1  | Occurs after call to ARM_SAI_Receive to indicate that all the data has been received. The driver is ready for the next call to ARM_SAI_Receive.
ARM_SAI_EVENT_TX_UNDERFLOW            |  2  | Occurs when data is to be sent but send operation has not been started. Data field **tx_underflow** = `1` of ARM_SAI_STATUS.
ARM_SAI_EVENT_RX_OVERFLOW             |  3  | Occurs when data is received but receive operation has not been started. Data field **rx_underflow** = `1` of ARM_SAI_STATUS.
ARM_SAI_EVENT_FRAME_ERROR             |  4  | Occurs in slave mode when invalid synchronization frame is detected. Data field **event_frame_error** = `1` of ARM_SAI_STATUS.
  
****************************************************************************************************************
