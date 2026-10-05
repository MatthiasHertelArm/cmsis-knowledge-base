---
id: "rtx-cmsis-rtos2-api-osrtxidlethread"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxIdleThread"
summary: "The function osRtxIdleThread is executed by the RTX kernel when no other threads are ready to run."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void osRtxIdleThread (void *argument);
```

- `argument` (in): Unused parameter, always set to `NULL`.

The function **osRtxIdleThread** is executed by the RTX kernel when no other threads are ready to run.

By default, this thread is an empty end-less loop that does nothing. It only waits until another task
becomes ready to run. You may change the code of the **osRtxIdleThread** function to put the CPU into
a power-saving or idle mode, see TickLess.

The default stack size for this thread is defined in the file RTX_Config.h. Refer to threadConfig.

**Warning:**
The idle thread should never be blocked nor terminated!
**Do not** call


  
- blocking functions,
  
- osThreadTerminate, or 
  
- osThreadExit

and **do not** return from this function when providing a user defined implementation.

**Code Example**
```
#include "rtx_os.h"
 
__NO_RETURN void osRtxIdleThread (void *argument) {
  (void)argument;

  for (;;) {}
}
```
