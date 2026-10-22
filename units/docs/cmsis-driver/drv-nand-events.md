---
id: "drv-nand-events"
type: "concept"
domain: "drivers"
title: "NAND Events"
summary: "The NAND driver generates call back events that are notified via the function ARM_NAND_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

The NAND driver generates call back events that are notified via the function ARM_NAND_SignalEvent.
 
This section provides the event values for the ARM_NAND_SignalEvent callback function.

The following call back notification events are generated:

### ARM_NAND_EVENT_DEVICE_READY

```c
ARM_NAND_EVENT_DEVICE_READY
```


### ARM_NAND_EVENT_DRIVER_READY

```c
ARM_NAND_EVENT_DRIVER_READY
```


### ARM_NAND_EVENT_DRIVER_DONE

```c
ARM_NAND_EVENT_DRIVER_DONE
```


### ARM_NAND_EVENT_ECC_ERROR

```c
ARM_NAND_EVENT_ECC_ERROR
```
