---
id: "drv-flash-events"
type: "concept"
domain: "drivers"
title: "Flash Events"
summary: "The Flash driver generates call back events that are notified via the function ARMFlashSignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

The Flash driver generates call back events that are notified via the function ARM_Flash_SignalEvent.
 
This section provides the event values for the ARM_Flash_SignalEvent callback function.

The following call back notification events are generated:

### ARM_FLASH_EVENT_READY

```c
ARM_FLASH_EVENT_READY
```


### ARM_FLASH_EVENT_ERROR

```c
ARM_FLASH_EVENT_ERROR
```
