---
id: "rtos2-thread-management-osthreadexit"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadExit"
summary: "The function osThreadExit terminates the calling thread. This allows the thread to be synchronized with osThreadJoin."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__NO_RETURN void osThreadExit (void)
```



The function **osThreadExit** terminates the calling thread. This allows the thread to be synchronized with osThreadJoin.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code** **Example**
```
__NO_RETURN void worker (void *argument) {
  // do something
  osDelay(1000U);
  osThreadExit();
}
```
