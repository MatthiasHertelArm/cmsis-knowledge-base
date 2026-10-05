---
id: "drv-vstream-vstreaminitialize"
type: "concept"
domain: "drivers"
title: "vStream: vStreamInitialize"
summary: "This function prepares the Virtual Streaming interface for operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamInitialize (vStreamEvent_t event_cb)
```


This function prepares the Virtual Streaming interface for operation.  

It performs the following tasks:
  - Initializes internal driver resources and streaming device interface.
  - Registers the vStreamEvent event signaling callback function.

The event callback function must conform to the vStreamEvent_t type.  
If event signaling is not required, pass a NULL pointer for **event_cb.**

This function must be called before any other vStream operations.

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
}
```

*******************************************************************************
