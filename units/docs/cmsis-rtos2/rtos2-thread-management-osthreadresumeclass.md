---
id: "rtos2-thread-management-osthreadresumeclass"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadResumeClass"
summary: "The function osThreadResumeClass resumes execution of threads based on safety class assignment. safety_class provides the reference safety class value, while mode is considered as a bitmap that additionally specifies the safety classes to be resumed."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadResumeClass (uint32_t safety_class, uint32_t mode);
```


The function **osThreadResumeClass** resumes execution of threads based on safety class assignment. _safety_class_ provides the reference safety class value, while _mode_ is considered as a bitmap that additionally specifies the safety classes to be resumed.

If osSafetyWithSameClass is set in _mode_ than the threads with safety class value equal to _safety_class_ will be resumed.


If osSafetyWithLowerClass is set in _mode_ than the threads with safety class value lower than _safety_class_ will be resumed.


Possible osStatus_t return values:
    - **osOK:** the threads with specified safety class have been resumed successfully.
    - **osErrorParameter:** _safety_class_ is invalid.
    - **osErrorISR:** the function **osThreadResumeClass** is called from interrupt other than osWatchdogAlarm_Handler.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class specified by _safety_class_ and _mode._

**Code Example:**
```
#include "cmsis_os2.h"
 
void ResumeNonCriticalClasses (void) {
  osStatus_t status;
 
  status = osThreadResumeClass(4U, osSafetyWithSameClass | osSafetyWithLowerClass); // Resumes threads with safety class 4 or lower
  // verify status value here.
}
```
