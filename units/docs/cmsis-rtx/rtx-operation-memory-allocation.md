---
id: "rtx-operation-memory-allocation"
type: "concept"
domain: "rtos"
title: "operation: Memory Allocation"
summary: "RTX5 objects (thread, mutex, semaphore, timer, message queue, thread and event flags, as well as memory pool) require dedicated RAM memory. Objects can be created using osObjectNew() calls and deleted using osObjectDelete() calls."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#memory-allocation"
license: "Apache-2.0"
mode: "V"
---

RTX5 objects (thread, mutex, semaphore, timer, message queue, thread and event flags, as well as memory pool) require dedicated RAM memory. Objects can be created using os_Object_New() calls and deleted using os_Object_Delete() calls. The related object memory needs to be available during the lifetime of the object.

RTX5 offers three different memory allocation methods for objects:

- GlobalMemoryPool uses a single global memory pool for all objects. It is easy to configure, but may have the disadvantage for memory fragmentation when objects with different sizes are created and destroyed.
- ObjectMemoryPool uses a fixed-size memory pool for each object type. The method is time deterministic and avoids memory fragmentation.
- StaticObjectMemory reserves memory during compile time and completely avoids that a system can be out of memory. This is typically a required for some safety critical systems.

It's possible to intermix all the memory allocation methods in the same application.

### Global Memory Pool

The global memory pool allocates all objects from a memory area. This method of memory allocation is the default configuration setting of RTX5.

(figure: Global Memory Pool for all objects)

When the memory pool does not provide sufficient memory, the creation of the object fails and the related os_Object_New() function returns `NULL`.

Enabled in systemConfig.

### Object-specific Memory Pools

Object-specific memory pools avoids memory fragmentation with a dedicated fixed-size memory management for each object type.

This type of memory pools are fully time deterministic, which means that object creation and destruction takes always the same fixed amount of time. As a fixed-size memory pool is specific to an object type, the handling of out-of-memory situations is simplified.

(figure: One memory pool per object type)

Object-specific memory pools are selectively enabled for each object type, e.g: mutex or thread using the RTX configuration
file:

- Enabled in threadConfig for thread objects.
- Enabled in timerConfig for timer objects.
- Enabled in eventFlagsConfig for event objects.
- Enabled in mutexConfig for mutex objects.
- Enabled in semaphoreConfig for semaphore.
- Enabled in memPoolConfig for memory pools.
- Enabled in msgQueueConfig for message objects.

When the memory pool does not provide sufficient memory, the creation of the object fails and the related os_Object_New() function returns `NULL`.

### Static Object Memory

In contrast to the dynamic memory allocations, the static memory allocation requires compile-time allocation of object memory.

(figure: Statically allocated memory for all objects)

Static memory allocation can be achieved by providing user-defined memory using attributes at object creation, see CMSIS_RTOS_MemoryMgmt_Manual. Please take special note of the following restrictions:

Memory type                                  | Requirements
---------------------------------------------|-------------------------------------------------------------------------------
Control Block (osXxxAttr_t::cb_mem)          | 4-Byte alignment. Size defined by osRtxThreadCbSize, osRtxTimerCbSize, osRtxEventFlagsCbSize, osRtxMutexCbSize, osRtxSemaphoreCbSize, osRtxMemoryPoolCbSize, osRtxMessageQueueCbSize.
Thread Stack (osThreadAttr_t::stack_mem)     | 8-Byte alignment. Size is application specific, i.e. amount of stack variables and frames.
Memory Pool (osMemoryPoolAttr_t::mp_mem)     | 4-Byte alignment. Size calculated with osRtxMemoryPoolMemSize.
Message Queue (osMessageQueueAttr_t::mq_mem) | 4-Byte alignment. Size calculated with osRtxMessageQueueMemSize.

In order to allow RTX5 aware debugging, i.e. Component Viewer, to recognize control blocks, they need to be placed in individual memory sections by using `__attribute__((section(...)))`.

RTX Object    | Linker Section
--------------|------------------------
Thread        | `.bss.os.thread.cb`
Timer         | `.bss.os.timer.cb`
Event Flags   | `.bss.os.evflags.cb`
Mutex         | `.bss.os.mutex.cb`
Semaphore     | `.bss.os.semaphore.cb`
Memory Pool   | `.bss.os.mempool.cb`
Message Queue | `.bss.os.msgqueue.cb`

It must be assured that these sections are placed into contiguous memory. This can fail, i.e. sections end up being split over multiple memory segments, when assigning compilation units to memory segments, manually.

The following code example shows how to create an OS object using static memory.

**Code Example:**

```c
/*----------------------------------------------------------------------------
 * CMSIS-RTOS 'main' function template
 *---------------------------------------------------------------------------*/

#include "RTE_Components.h"
#include  CMSIS_device_header
#include "cmsis_os2.h"
 
//include rtx_os.h for types of RTX objects
#include "rtx_os.h"
 
//The thread function instanced in this example
void worker(void *arg)
{
  while(1) 
  {
    //work
    osDelay(10000);
  }  
}
 
// Define objects that are statically allocated for worker thread 1
__attribute__((section(".bss.os.thread.cb")))
osRtxThread_t worker_thread_tcb_1;
 
// Reserve two areas for the stacks of worker thread 1
// uint64_t makes sure the memory alignment is 8
uint64_t worker_thread_stk_1[64];
 
// Define the attributes which are used for thread creation
// Optional const saves RAM memory and includes the values in periodic ROM tests 
const osThreadAttr_t worker_attr_1 = {
  "wrk1",
  osThreadJoinable,
  &worker_thread_tcb_1,
  sizeof(worker_thread_tcb_1),
  &worker_thread_stk_1[0],
  sizeof(worker_thread_stk_1),
  osPriorityAboveNormal,
  0
};
 
// Define ID object for thread
osThreadId_t th1;
 
/*----------------------------------------------------------------------------
 * Application main thread
 *---------------------------------------------------------------------------*/
void app_main (void *argument) {
  uint32_t param = NULL;
 
  // Create an instance of the worker thread with static resources (TCB and stack)
  th1 = osThreadNew(worker, &param, &worker_attr_1);
 
  for (;;) {}
}
 
int main (void) {
  // System Initialization
  SystemCoreClockUpdate();
  // ...

  osKernelInitialize();                 // Initialize CMSIS-RTOS
  osThreadNew(app_main, NULL, NULL);    // Create application main thread
  osKernelStart();                      // Start thread execution
  for (;;) {}
}
```
