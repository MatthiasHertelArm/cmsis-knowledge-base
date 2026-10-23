---
id: "rtos2-mutex-management-attr-bits"
type: "concept"
domain: "rtos"
title: "Mutex Management: attr_bits"
summary: "The following bit masks can be used to set options: - osMutexRecursive : a thread can consume the mutex multiple times without locking itself. - osMutexPrioInherit : the owner thread inherits the priority of a (higher priority) waiting thread."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexAttr_t::attr_bits
```


The following bit masks can be used to set options:
 - osMutexRecursive : a thread can consume the mutex multiple times without locking itself.
 - osMutexPrioInherit : the owner thread inherits the priority of a (higher priority) waiting thread.
 - osMutexRobust : the mutex is automatically released when owner thread is terminated.

Use logical **'OR'** operation to select multiple options, for example:
```
osMutexRecursive | osMutexPrioInherit;
```

Default: `0` which specifies:
 - _non recursive mutex_: a thread cannot consume the mutex multiple times.
 - _non priority raising_: the priority of an owning thread is not changed.
 - _mutex is not automatically release_: the mutex object must be always is automatically released when owner thread is terminated.
