---
id: "rtos2-thread-management-tz-module"
type: "concept"
domain: "rtos"
title: "Thread Management: tz_module"
summary: "\\if (ARMv8M) TrustZone Thread Context Management Identifier to allocate context memory for threads. The RTOS kernel that runs in non-secure state calls the interface functions defined by the header file TZ_context.h."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::tz_module
```


\if (ARMv8M)
TrustZone Thread Context Management Identifier to allocate context memory for threads. The RTOS kernel that runs in
non-secure state calls the interface functions defined by the header file TZ_context.h. Can safely be set to zero
for threads not using secure calls at all. 
See TrustZone RTOS Context Management.

Default: `0` not thread context specified.
\else
Applicable only for devices on Armv8-M architecture. Ignored on others.
\endif
