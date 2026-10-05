---
id: "drv-sai-events"
type: "concept"
domain: "drivers"
title: "SAI Events"
summary: "The SAI driver generates call back events that are notified via the function ARMSAISignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

The SAI driver generates call back events that are notified via the function ARM_SAI_SignalEvent.
 
This section provides the event values for the ARM_SAI_SignalEvent callback function.

The following call back notification events are generated:

### ARM_SAI_EVENT_SEND_COMPLETE

```c
ARM_SAI_EVENT_SEND_COMPLETE
```


### ARM_SAI_EVENT_RECEIVE_COMPLETE

```c
ARM_SAI_EVENT_RECEIVE_COMPLETE
```


### ARM_SAI_EVENT_TX_UNDERFLOW

```c
ARM_SAI_EVENT_TX_UNDERFLOW
```


### ARM_SAI_EVENT_RX_OVERFLOW

```c
ARM_SAI_EVENT_RX_OVERFLOW
```


### ARM_SAI_EVENT_FRAME_ERROR

```c
ARM_SAI_EVENT_FRAME_ERROR
```
