---
id: "drv-vio-viogetsignal"
type: "concept"
domain: "drivers"
title: "VIO: vioGetSignal"
summary: "The function vioGetSignal retrieves a signal from an input identified by mask. Use this function to read data from any input that is provided."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t vioGetSignal (uint32_t mask)
```


The function **vioGetSignal** retrieves a signal from an input identified by _mask._ Use this function to read data from any
input that is provided.

Refer to vioSignals_gr for information about the possible _mask_ values.

**Code** **Example:**
```
#include "cmsis_vio.h"                  // ::CMSIS Driver:VIO
 
int main (void) {
  uint32_t state;
  uint32_t last = 0U;
 
  vioInit();
  for (;;) {
    state = (vioGetSignal (vioBUTTON0)); // Get pressed button state
    if (state != last){
      if (state == vioBUTTON0){
        // do something
      }
    }
    last = state;
  }
}
```
**************************************************************************************************************************
