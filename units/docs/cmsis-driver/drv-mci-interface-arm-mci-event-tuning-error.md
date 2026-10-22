---
id: "drv-mci-interface-arm-mci-event-tuning-error"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_EVENT_TUNING_ERROR"
summary: "Indicates an unrecoverable tuning-circuit error outside the tuning procedure. The affected transfer is invalid. Reset the tuning circuit and perform initial tuning before retrying. \\sa ARM_MCI_SignalEvent"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MCI_EVENT_TUNING_ERROR
```


Indicates an unrecoverable tuning-circuit error outside the tuning procedure.
The affected transfer is invalid. Reset the tuning circuit and perform initial tuning before retrying.
\sa ARM_MCI_SignalEvent
