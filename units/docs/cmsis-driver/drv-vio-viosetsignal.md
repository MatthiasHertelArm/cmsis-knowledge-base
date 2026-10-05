---
id: "drv-vio-viosetsignal"
type: "concept"
domain: "drivers"
title: "VIO: vioSetSignal"
summary: "The function vioSetSignal set a signal to an output specified by mask. Use this function to map VIOs to actual hardware for displaying signals on a target board."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void vioSetSignal (uint32_t mask, uint32_t signal)
```


The function **vioSetSignal** set a _signal_ to an output specified by _mask._ Use this function to map VIOs to actual
hardware for displaying signals on a target board.

Refer to vioSignals_gr for information about the possible _mask_ and _signal_ values.

**Code** **Example:**
```
#include "cmsis_vio.h"                  // ::CMSIS Driver:VIO
 
int main (void) {
 
  vioInit();
  vioSetSignal(vioLED0, vioLEDon);
  // ...
  vioSetSignal(vioLED0, vioLEDoff);
}
```
**************************************************************************************************************************
