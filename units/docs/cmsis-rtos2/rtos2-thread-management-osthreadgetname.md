---
id: "rtos2-thread-management-osthreadgetname"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetName"
summary: "The function osThreadGetName returns the pointer to the name string of the thread identified by parameter thread_id or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osThreadGetName (osThreadId_t thread_id)
```


The function **osThreadGetName** returns the pointer to the name string of the thread identified by parameter _thread_id_ or
`NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
void ThreadGetName_example (void) {
  osThreadId_t thread_id = osThreadGetId();
  const char* name = osThreadGetName(thread_id);
  if (name == NULL) {
    // Failed to get the thread name; not in a thread
  }
}
```
