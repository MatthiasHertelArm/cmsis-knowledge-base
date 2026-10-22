---
id: "rtos2-thread-management-osthreadgetid"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetId"
summary: "The function osThreadGetId returns the thread object ID of the currently running thread or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadId_t osThreadGetId (void)
```


The function **osThreadGetId** returns the thread object ID of the currently running thread or NULL in case of an error.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
void ThreadGetId_example (void) {
  osThreadId_t id;                              // id for the currently running thread
   
  id = osThreadGetId();
  if (id == NULL) {
    // Failed to get the id
  }
}
```
