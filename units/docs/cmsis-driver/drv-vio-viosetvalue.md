---
id: "drv-vio-viosetvalue"
type: "concept"
domain: "drivers"
title: "VIO: vioSetValue"
summary: "The function vioSetValue set the value to the output identified by id. Use this function to set states of I/Os for example."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void vioSetValue (uint32_t id, int32_t value)
```


The function **vioSetValue** set the _value_ to the output identified by _id._ Use this function to set states of I/Os for
example.

Refer to vioValueIDs_gr for information about _id._

**Code** **Example:**
```
#include "cmsis_vio.h"                  // ::CMSIS Driver:VIO
 
int main (void) {
 
  vioInit();
  vioSetValue(vioAOUT0, 1024);
}
```
**************************************************************************************************************************
