---
id: "drv-spi-events"
type: "concept"
domain: "drivers"
title: "SPI Events"
summary: "The SPI driver generates call back events that are notified via the function ARM_SPI_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

The SPI driver generates call back events that are notified via the function ARM_SPI_SignalEvent.
 
This section provides the event values for the ARM_SPI_SignalEvent callback function.

The following call back notification events are generated:

### ARM_SPI_EVENT_TRANSFER_COMPLETE

```c
ARM_SPI_EVENT_TRANSFER_COMPLETE
```


### ARM_SPI_EVENT_DATA_LOST

```c
ARM_SPI_EVENT_DATA_LOST
```


### ARM_SPI_EVENT_MODE_FAULT

```c
ARM_SPI_EVENT_MODE_FAULT
```
