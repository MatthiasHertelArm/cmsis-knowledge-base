---
id: "drv-mci-cmd-line-mode"
type: "concept"
domain: "drivers"
title: "MCI CMD Line Mode"
summary: "Specify the CMD line mode (Push-Pull or Open Drain)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify the CMD line mode (Push-Pull or Open Drain).

Set the CMD line type with the function ARM_MCI_Control. 
The CMD line mode is push-pull (default) or open drain (needed for older MMC).


### ARM_MCI_BUS_CMD_PUSH_PULL

```c
ARM_MCI_BUS_CMD_PUSH_PULL
```


### ARM_MCI_BUS_CMD_OPEN_DRAIN

```c
ARM_MCI_BUS_CMD_OPEN_DRAIN
```

******************************************************************************************************************
