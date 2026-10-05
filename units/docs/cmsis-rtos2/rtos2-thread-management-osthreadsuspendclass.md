---
id: "rtos2-thread-management-osthreadsuspendclass"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadSuspendClass"
summary: "The function osThreadSuspendClass suspends execution of threads based on safety class assignment. safetyclass provides the reference safety class value, while mode is considered as a bitmap that additionally specifies the safety classes to be suspended."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadSuspendClass (uint32_t safety_class, uint32_t mode);
```


The function **osThreadSuspendClass** suspends execution of threads based on safety class assignment. _safety_class_ provides the reference safety class value, while _mode_ is considered as a bitmap that additionally specifies the safety classes to be suspended.

If osSafetyWithSameClass is set in _mode_ than the threads with safety class value equal to _safety_class_ will be suspended.


If osSafetyWithLowerClass is set in _mode_ than the threads with safety class value lower than _safety_class_ will be suspended.

Possible osStatus_t return values:
    - **osOK:** the threads with specified safety class have been suspended successfully.
    - **osErrorParameter:** _safety_class_ is invalid.
    - **osErrorResource:** no other READY thread exists.
    - **osErrorISR:** the function **osThreadSuspendClass** is called from interrupt other than osWatchdogAlarm_Handler.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class specified by _safety_class_ and _mode._

**Code Example:**
```
#include "cmsis_os2.h"
 
void SuspendNonCriticalClasses (void) {
  osStatus_t status;
 
  status = osThreadSuspendClass(4U, osSafetyWithSameClass | osSafetyWithLowerClass); // Suspends threads with safety class 4 or lower
  // verify status value here.
}
```
