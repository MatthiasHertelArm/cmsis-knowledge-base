---
id: "drv-vio-vioinit"
type: "concept"
domain: "drivers"
title: "VIO: vioInit"
summary: "The function vioInit initializes the VIO interface. Use it to initialize any connected hardware that is used to map VIO signals."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void vioInit (void)
```


The function **vioInit** initializes the VIO interface. Use it to initialize any connected hardware that is used to
map VIO signals. 

**Code** **Example:**
```
#include "cmsis_vio.h"                  // ::CMSIS Driver:VIO
 
int main (void) {
 
  // System Initialization
  SystemCoreClockUpdate();
  vioInit();
  // ...
 
}
```
**************************************************************************************************************************
