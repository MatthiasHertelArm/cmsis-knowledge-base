---
id: "rtos2-thread-management-osthreadgetzone"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetZone"
summary: "The function osThreadGetZone returns the MPU Protected Zone value assigned to the thread identified by parameter threadid. In case of an error, it returns osErrorId."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadGetZone (osThreadId_t thread_id);
```


The function **osThreadGetZone** returns the MPU Protected Zone value assigned to the thread identified by parameter _thread_id._
In case of an error, it returns osErrorId.
