---
id: "drv-vio-viogetvalue"
type: "concept"
domain: "drivers"
title: "VIO: vioGetValue"
summary: "The function vioGetValue retrieves a value from the input identified by id. Use this function to read data from inputs."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vioGetValue (uint32_t id)
```


The function **vioGetValue** retrieves a value from the input identified by _id._ Use this function to read data from inputs.

Refer to vioValueIDs_gr for information about _id._

**Code** **Example:**
```
#include "cmsis_vio.h"                  // ::CMSIS Driver:VIO
 
int main (void) {
  uint32_t button;
 
  vioInit();
  button = vioGetValue(vioBUTTON0);
}
```
**************************************************************************************************************************
