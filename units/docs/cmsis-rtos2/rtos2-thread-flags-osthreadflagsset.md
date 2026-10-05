---
id: "rtos2-thread-flags-osthreadflagsset"
type: "concept"
domain: "rtos"
title: "Thread Flags: osThreadFlagsSet"
summary: "The function osThreadFlagsSet sets the thread flags for a thread specified by parameter threadid. The thread returns the flags stored in the thread control block, or an error code if highest bit is set (refer to flagserrorcodes)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadFlagsSet (osThreadId_t thread_id, uint32_t flags )
```

The function **osThreadFlagsSet** sets the thread flags for a thread specified by parameter **thread_id.** The thread returns
the flags stored in the thread control block, or an error code if highest bit is set (refer to flags_error_codes).
Refer to **Usage** **Examples** below to understand how the return value is computed.

The target thread waiting for a flag to be set will resume from BLOCKED state.

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error.
    - **osFlagsErrorParameter:** parameter **thread_id** is not a valid thread or **flags** has highest bit set.
    - **osFlagsErrorResource:** the thread is in invalid state.
    - **osFlagsErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function may be called from Interrupt Service Routines.

**Code** **Example**
```
/*----------------------------------------------------------------------------
     Function 'signal_func' called from multiple threads
---------------------------------------------------------------------------*/
void signal_func (osThreadId_t tid)  {
  osThreadFlagsSet(tid_clock, 0x0100U);     /* set signal to clock thread    */
  osDelay(500U);                            /* delay 500ms                   */
  osThreadFlagsSet(tid_clock, 0x0100U);     /* set signal to clock thread    */
  osDelay(500U);                            /* delay 500ms                   */
  osThreadFlagsSet(tid, 0x0001U);           /* set signal to thread 'thread' */
  osDelay(500U);                            /* delay 500ms                   */
}
```

**Usage** **Examples**

The following diagram assumes that in the control block of Thread1 the flag 1 is already set. Thread2 now sets flag 2 and
Thread1 returns the updated value immediately:

\msc
 a [label="",    textcolor="indigo", linecolor="indigo", arclinecolor="red"],
 b [label="",    textcolor="blue",   linecolor="blue",   arclinecolor="blue"];
 
 a note a [label="Thread1",       textbgcolour="#FFCCCF"],
 b note b [label="Thread2",       textbgcolour="#E0E0FF"];
 
 a box a [label = "Flags == 1"];
 a<-b [label = "osThreadFlagsSet(2)"];
 a>>b [label = "return(3)"];
 a->a [label = "while(1)"];
\endmsc

Depending on thread scheduling, the flag status can be modified before returning: 

\msc
 a [label="",    textcolor="indigo", linecolor="indigo", arclinecolor="red"],
 b [label="",    textcolor="blue",   linecolor="blue",   arclinecolor="blue"];
 
 a note a [label="Thread1",       textbgcolour="#FFCCCF"],
 b note b [label="Thread2",       textbgcolour="#E0E0FF"];
 
 b box b [label = "Flags == 0"];
 b->b [label = "osThreadFlagsWait(1)"];
 b box b [label = "thread state = blocked"];
 a->b [label = "osThreadFlagsSet(1)"];
 b box b [label = "Flags == 1"];
 b box b [label = "thread state = ready"];
 b box b [label = "Flags == 0*"];
 --- [label = "If Thread2 priority > Thread1 priority, it gets scheduled immediately"];
 b->b [label = "return(1)"];
 b->b [label = "osThreadFlagsWait(1)"];
 b box b [label = "thread state = blocked"];
 --- [label = "endif"];
 b->a [label = "return(0)"];
\endmsc
**Note:** * In this case osThreadFlagsWait auto-clears the flag.
