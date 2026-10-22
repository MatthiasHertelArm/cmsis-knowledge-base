---
id: "drv-mci-interface-arm-mci-event-retuning-request"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_EVENT_RETUNING_REQUEST"
summary: "This event does not invalidate transferred data and active transfer may finish normally unless the transfer ends with ARM_MCI_EVENT_TRANSFER_ERROR."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MCI_EVENT_RETUNING_REQUEST
```

\sa ARM_MCI_SignalEvent

This event does not invalidate transferred data and active transfer may finish normally unless the transfer ends
with ARM_MCI_EVENT_TRANSFER_ERROR.

After receiving this event, re-tuning should be performed using ARM_MCI_UHS_RETUNING_START before starting
the next normal command.
