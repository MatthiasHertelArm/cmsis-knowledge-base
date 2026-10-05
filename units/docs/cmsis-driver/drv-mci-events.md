---
id: "drv-mci-events"
type: "concept"
domain: "drivers"
title: "MCI Events"
summary: "The MCI driver generates call back events that are notified via the function ARM_MCI_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

The MCI driver generates call back events that are notified via the function ARM_MCI_SignalEvent.

This section provides the event values for the ARM_MCI_SignalEvent callback function.

The following call back notification events are generated:

### ARM_MCI_EVENT_CARD_INSERTED

```c
ARM_MCI_EVENT_CARD_INSERTED
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_CARD_REMOVED

```c
ARM_MCI_EVENT_CARD_REMOVED
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_COMMAND_COMPLETE

```c
ARM_MCI_EVENT_COMMAND_COMPLETE
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_COMMAND_TIMEOUT

```c
ARM_MCI_EVENT_COMMAND_TIMEOUT
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_COMMAND_ERROR

```c
ARM_MCI_EVENT_COMMAND_ERROR
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_TRANSFER_COMPLETE

```c
ARM_MCI_EVENT_TRANSFER_COMPLETE
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_TRANSFER_TIMEOUT

```c
ARM_MCI_EVENT_TRANSFER_TIMEOUT
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_TRANSFER_ERROR

```c
ARM_MCI_EVENT_TRANSFER_ERROR
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_SDIO_INTERRUPT

```c
ARM_MCI_EVENT_SDIO_INTERRUPT
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_CCS

```c
ARM_MCI_EVENT_CCS
```

\sa ARM_MCI_SignalEvent

### ARM_MCI_EVENT_CCS_TIMEOUT

```c
ARM_MCI_EVENT_CCS_TIMEOUT
```

\sa ARM_MCI_SignalEvent
******************************************************************************************************************
