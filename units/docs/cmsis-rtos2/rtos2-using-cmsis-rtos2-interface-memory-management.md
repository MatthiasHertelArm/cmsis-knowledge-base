---
id: "rtos2-using-cmsis-rtos2-interface-memory-management"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Memory Management"
summary: "The CMSISRTOS offers two options for memory management the user can choose. For object storage one can either use"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#memory-management"
license: "Apache-2.0"
mode: "V"
---

The CMSIS_RTOS offers two options for memory management the user can choose. For object storage one can either use

 - CMSIS_RTOS_MemoryMgmt_Automatic (fully portable), or
 - CMSIS_RTOS_MemoryMgmt_Manual (implementation specific).

In order to affect the memory allocation scheme all RTOS objects that can be created on request, i.e. those having a `osXxxNew` function, accept an optional `osXxxAttr_t attr` argument on creation. As a rule of thumb the object attributes at least have members to assign custom control block memory, i.e. `cb_mem` and `cb_size` members. By default, i.e. `attr` is `NULL` or `cb_mem` is `NULL`, CMSIS_RTOS_MemoryMgmt_Automatic is used. Providing a pointer to user memory in `cb_mem` switches
to CMSIS_RTOS_MemoryMgmt_Manual.

### Automatic Dynamic Allocation

The automatic allocation is the default and viable for many use-cases. Moreover it is fully portable across different implementations of the CMSIS_RTOS. The common drawback of dynamic memory allocation is the possibility of memory fragmentation and exhaustion. Given that all needed objects are created once upon system initialization and never deleted at runtime this class of runtime failures can be prevented, though.

The actual allocation strategy used is implementation specific, i.e. whether global heap or preallocated memory pools are used.

**Code Example:**

```c
#include "cmsis_os2.h"                          // CMSIS-RTOS2 API header
  
osMutexId_t mutex_id;
osMutexId_t mutex2_id;
  
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",                              // human readable mutex name
  osMutexRecursive | osMutexPrioInherit,        // attr_bits
  NULL,                                         // memory for control block (default)
  0U                                            // size for control block (default)
};
  
void CreateMutex (void)  {
  mutex_id = osMutexNew(NULL);                  // use default values for all attributes
  mutex2_id = osMutexNew(&Thread_Mutex_attr);   // use attributes from defined structure
  :
}
```

The Mutexes in this example are created using automatic memory allocation.

### Manual User-defined Allocation

One can get fine grained control over memory allocation by providing user-defined memory. The actual requirements such user-defined memory are kernel-specific. Thus one needs to carefully refer to the size and alignment rules of the implementation used.

**Code Example:**

```c
#include "cmsis_os2.h"                          // CMSIS-RTOS2 API header
#include "rtx_os.h"                             // kernel include file
  
osMutexId_t mutex_id;
  
static osRtxMutex_t mutex_cb __attribute__((section(".bss.os.mutex.cb")));  // Placed on .bss.os.mutex.cb section for RTX5 aware debugging
  
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",                              // human readable mutex name
  osMutexRecursive | osMutexPrioInherit,        // attr_bits
  &mutex_cb,                                    // memory for control block (user-defined)
  sizeof(mutex_cb)                              // size for control block (user-defined)
};
  
void CreateMutex (void)  {
  mutex_id = osMutexNew(&Thread_Mutex_attr);    // use attributes from defined structure
  :
}
```

The above example uses user-defined memory for the mutex control block. For this `mutex_cb` is defined with the control block type provided by the kernel header file `rtx_os.h` from CMSIS-RTX RTOS kernel.
