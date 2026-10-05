---
id: "rtos2-thread-management"
type: "concept"
domain: "rtos"
title: "Thread Management"
summary: "Define, create, and control thread functions."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

Define, create, and control thread functions.
 
The Thread Management function group allows defining, creating, and controlling thread functions in the system.

**Note:** Thread management functions cannot be called from Interrupt Service Routines.


Thread states
-------------
Threads can be in the following states:

 - **RUNNING:** The thread that is currently running is in the RUNNING state. Only one thread at a time can be in this
   state.
 - **READY:** Threads which are ready to run are in the READY state. Once the RUNNING thread has terminated, or is
   BLOCKED, the next READY thread with the highest priority becomes the RUNNING thread.
 - **BLOCKED:** Threads that are blocked either delayed, waiting for an event to occur or suspended are in the BLOCKED
   state.
 - **TERMINATED:** When osThreadTerminate is called, threads are TERMINATED with resources not yet released (applies to joinable_threads "joinable threads).
 - **INACTIVE:** Threads that are not created or have been terminated with all resources released are in the INACTIVE state.
 
" "Thread State and State Transitions"


A CMSIS-RTOS assumes that threads are scheduled as shown in the figure **Thread State and State Transitions**. The thread
states change as follows:
 - A thread is created using the function osThreadNew. This puts the thread into the READY or RUNNING state
   (depending on the thread priority).
 - CMSIS-RTOS is preemptive. The active thread with the highest priority becomes the RUNNING thread provided it does not
   wait for any event. The initial priority of a thread is defined with the osThreadAttr_t but may be changed during
   execution using the function osThreadSetPriority.
 - The RUNNING thread transfers into the BLOCKED state when it is delayed, waiting for an event or suspended.
 - Active threads can be terminated any time using the function osThreadTerminate. Threads can terminate also by just
   returning from the thread function. Threads that are terminated are in the INACTIVE state and typically do not consume
   any dynamic memory resources. 


Processor Mode for Thread Execution
-------------

When creating user threads with osThreadNew it is possible to specify for each thread whether it shall be executed in privileged or unprivileged mode. For that the thread attributes argument shall have in its osThreadAttr_t::attr_bits flags either osThreadPrivileged or osThreadUnprivileged set respectively.
If not set then the default operation mode will be used according to kernel configuration.

For detailed differences between privileged and unprivileged mode, please refer to the User's Guide of the target processor. But typically following differences are specified:

In **unprivileged processor mode**, the thread :
 - has limited access to the MSR and MRS instructions, and cannot use the CPS instruction.
 - cannot access the system timer, NVIC, or system control block.
 - might have restricted access to memory or peripherals.

In **privileged processor mode**, the application software can use all the instructions and has access to all resources.


Thread Examples
===============
The following examples show various scenarios to create threads:
 
**Example 1 - Create a simple thread** 

Create a thread out of the function thread1 using all default values for thread attributes and memory allocated by the system.
 
```
__NO_RETURN void thread1 (void *argument) {
  // ...
  for (;;) {}
}
 
int main (void) {
  osKernelInitialize();
  ;
  osThreadNew(thread1, NULL, NULL);     // Create thread with default settings
  ;
  osKernelStart(); 
}
```

**Example 2 - Create thread with stack non-default stack size**

Similar to the simple thread all attributes are default. The stack size is requested of size 1024 Bytes with with corresponding value passed as osThreadAttr_t.stack_size to osThreadNew. The memory for the stack is then allocated by the system.

```
__NO_RETURN void thread1 (void *argument) {
  // ...
  for (;;) {}
}
 
const osThreadAttr_t thread1_attr = {
  .stack_size = 1024                            // Create the thread stack with a size of 1024 bytes
};
 
int main (void) {
  ;  
  osThreadNew(thread1, NULL, &thread1_attr);    // Create thread with custom sized stack memory
  ;
}
```

**Example 3 - Create thread with statically allocated stack**
 
Similar to the simple thread all attributes are default. The stack is statically allocated using the `uint64_t` array
`thread1_stk_1.` This allocates 64*8 Bytes (=512 Bytes) with an alignment of 8 Bytes (mandatory for Cortex-M stack memory). 
 
osThreadAttr_t.stack_mem holds a pointer to the stacks lowest address. 
 
osThreadAttr_t.stack_size is used to pass the stack size in Bytes to osThreadNew.

```
__NO_RETURN void thread1 (void *argument) {
  // ...
  for (;;) {}
}
 
static uint64_t thread1_stk_1[64];
 
const osThreadAttr_t thread1_attr = {
  .stack_mem  = &thread1_stk_1[0],
  .stack_size = sizeof(thread1_stk_1)
};
 
int main (void) {
  ;  
  osThreadNew(thread1, NULL, &thread1_attr);    // Create thread with statically allocated stack memory
  ;
}
```

**Example 4 - Thread with statically allocated task control block**
 
Typically this method is chosen together with a statically allocated stack as shown in Example 2. 
```
#include "cmsis_os2.h"
 
//include rtx_os.h for control blocks of CMSIS-RTX objects
#include "rtx_os.h"

__NO_RETURN void thread1 (void *argument) {
  // ...
  for (;;) {}
}
 
static osRtxThread_t thread1_tcb;
 
const osThreadAttr_t thread1_attr = {
  .cb_mem  = &thread1_tcb,
  .cb_size = sizeof(thread1_tcb),
};
 
int main (void) {
  ;
  osThreadNew(thread1, NULL, &thread1_attr);    // Create thread with custom tcb memory
  ;
}
```

**Example 5 - Create thread with a different priority** 
 
The default priority of RTX kernel is `osPriorityNormal`. Often you want to run a task with a higher or lower priority. Using the osThreadAttr_t::priority field you can assign any initial priority required.

```
__NO_RETURN void thread1 (void *argument) {
  // ...
  for (;;) {}
}
 
const osThreadAttr_t thread1_attr = {
  .priority = osPriorityHigh                    //Set initial thread priority to high   
};
 
int main (void) {
  ;
  osThreadNew(thread1, NULL, &thread1_attr);
  ;
}
```


**Example 6 - Joinable threads**
 
In this example a master thread creates four threads with the osThreadJoinable attribute. These will do some work and
return using the osThreadExit call after finished. osThreadJoin is used to synchronize the thread termination. 


```
__NO_RETURN void worker (void *argument) {
  ; // work a lot on data[] 
  osDelay(1000U);
  osThreadExit();
}
 
__NO_RETURN void thread1 (void *argument) {
  osThreadAttr_t worker_attr;
  osThreadId_t worker_ids[4];
  uint8_t data[4][10];

  memset(&worker_attr, 0, sizeof(worker_attr));
  worker_attr.attr_bits = osThreadJoinable;
 
  worker_ids[0] = osThreadNew(worker, &data[0][0], &worker_attr);
  worker_ids[1] = osThreadNew(worker, &data[1][0], &worker_attr);
  worker_ids[2] = osThreadNew(worker, &data[2][0], &worker_attr);
  worker_ids[3] = osThreadNew(worker, &data[3][0], &worker_attr);
 
  osThreadJoin(worker_ids[0]);
  osThreadJoin(worker_ids[1]);
  osThreadJoin(worker_ids[2]);
  osThreadJoin(worker_ids[3]);
 
  osThreadExit(); 
}
```
