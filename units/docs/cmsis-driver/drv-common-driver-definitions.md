---
id: "drv-common-driver-definitions"
type: "concept"
domain: "drivers"
title: "Common Driver Definitions"
summary: "Definitions common in all driver interfaces (%Driver_Common.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Common.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Common.c"
license: "Apache-2.0"
mode: "V"
---

Definitions common in all driver interfaces (%Driver_Common.h)

The following definitions are common in all CMSIS-Driver interfaces. Refer to DriverFunctions
for a general overview.


### ARM_POWER_STATE

```c
ARM_POWER_STATE
```

 
The access structure of each CMSIS-Driver provides the function **PowerControl,** which handles the power
profile for a peripheral using the parameter ARM_POWER_STATE. Depending on this parameter, 
the peripheral will operate at full speed, detect just events, or is completely un-powered.

Refer to CallSequence for more information.
