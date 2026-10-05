---
id: "drv-vstream-vstreamuninitialize"
type: "concept"
domain: "drivers"
title: "vStream: vStreamUninitialize"
summary: "This function disables the Virtual Streaming interface and releases all associated resources that were allocated during vStreamInitialize."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamUninitialize (void)
```


This function disables the Virtual Streaming interface and releases all associated resources that
were allocated during vStreamInitialize.

Use this function to properly shut down the interface when streaming is no longer required.  
After calling **vStreamUninitialize,** the interface is considered inactive, and re-initialization is required to resume streaming operations.

**Code Example**:
```
#include "cmsis_vstream.h"

// vStream driver
extern vStreamDriver_t     Driver_vStreamAccelerometer;
static vStreamDriver_t *ptrDriver_vStreamAccelerometer = &Driver_vStreamAccelerometer;

int main (void) {

  SystemCoreClockUpdate();              // System Initialization

  ptrDriver_vStreamAccelerometer->Initialize(NULL);
  // ...
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
