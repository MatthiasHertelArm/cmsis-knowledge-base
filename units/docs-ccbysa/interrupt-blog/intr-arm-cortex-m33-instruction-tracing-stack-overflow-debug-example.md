---
id: "intr-arm-cortex-m33-instruction-tracing-stack-overflow-debug-example"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Example Project / Stack Overflow Debug Example"
summary: "Let's now go over an example of how to debug a stack overflow using the MTB."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#stack-overflow-debug-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Example Project_

Let's now go over an example of how to debug a stack overflow using the MTB.

#### Background Context

Most RTOS' implement a simple stack overflow detection scheme.

First, when a new task is created the stack is scrubbed with a known pattern. For example, for FreeRTOS[^3] it looks like:

```c
    /* Avoid dependency on memset() if it is not required. */
    #if ( tskSET_NEW_STACKS_TO_KNOWN_VALUE == 1 )
        {
            /* Fill the stack with a known value to assist debugging. */
            ( void ) memset( pxNewTCB->pxStack, ( int ) tskSTACK_FILL_BYTE, ( size_t ) ulStackDepth * sizeof( StackType_t ) );
        }
    #endif /* tskSET_NEW_STACKS_TO_KNOWN_VALUE */
```

Then, every time a task context switch takes place, the bottom of the stack is checked to see if it matches the known pattern. The FreeRTOS logic looks like this:

```c
#define taskCHECK_FOR_STACK_OVERFLOW()                                                            \
{                                                                                                 \
   const uint32_t * const pulStack = ( uint32_t * ) pxCurrentTCB->pxStack;                       \
   const uint32_t ulCheckValue = ( uint32_t ) 0xa5a5a5a5;                                        \
                                                                                                 \
   if( ( pulStack[ 0 ] != ulCheckValue ) ||                                                      \
       ( pulStack[ 1 ] != ulCheckValue ) ||                                                      \
       ( pulStack[ 2 ] != ulCheckValue ) ||                                                      \
       ( pulStack[ 3 ] != ulCheckValue ) )                                                       \
   {                                                                                             \
       vApplicationStackOverflowHook( ( TaskHandle_t ) pxCurrentTCB, pxCurrentTCB->pcTaskName ); \
   }                                                                                             \
}


void vTaskSwitchContext( void )
{
// ...
        taskCHECK_FOR_STACK_OVERFLOW();
// ...
```

If the check fails, we know a stack overflow occurred at some point while the task was running. We may not have any information about what call chain led to the stack overflow however. When we context switch, the stack may no longer be at it's deepest mark so the state may be lost! What's super neat with the MTB is we can see the history of the functions executing leading up to the context switch for additional clues.

Let's try out an example:

```
$ make flash
# Enable stack overflow example
(gdb) set g_trace_example_config=1
(gdb) continue
vApplicationStackOverflowHook (xTask=0x20008a88 <ucHeap+1832>, pcTaskName=0x20008abc <ucHeap+1884> "Algo") at ./main.c:101
101   __asm("bkpt 4");
```

We can load the `mtb` decoder script and take a look at the last 100 branches:

```
(gdb) mtb --limit 100

>S: 0x20000284 - recurse_func0 @ ./main.c:115
 D: 0x20000268 - recurse_func0 @ ./main.c:115
>S: 0x20000290 - recurse_func0 @ ./main.c:118
 D: 0x200002a4 - recurse_func1 @ ./main.c:123
>S: 0x200002ac - recurse_func1 @ ./main.c:123
 D: 0x200002c0 - recurse_func2 @ ./main.c:128
>S: 0x200002c8 - recurse_func2 @ ./main.c:128
 D: 0x200002dc - recurse_func3 @ ./main.c:133
>S: 0x200002e4 - recurse_func3 @ ./main.c:133
 D: 0x200002f8 - recurse_func4 @ ./main.c:138
>S: 0x20000300 - recurse_func4 @ ./main.c:138
 D: 0x20000318 - prvAlgoTask @ ./main.c:146
>S: 0x2000031a - prvAlgoTask @ ./main.c:146
 D: 0x20000e88 - vTaskDelay @ ./freertos_kernel/tasks.c:1341
>S: 0x20000e8c - vTaskDelay @ ./freertos_kernel/tasks.c:1341
 D: 0x20000ea0 - vTaskDelay @ ./freertos_kernel/tasks.c:1343
>S: 0x20000ea4 - vTaskDelay @ ./freertos_kernel/tasks.c:1343
 D: 0x20000eb0 - vTaskDelay @ ./freertos_kernel/tasks.c:1344
>S: 0x20000eb0 - vTaskDelay @ ./freertos_kernel/tasks.c:1344
 D: 0x20000bbc - vTaskSuspendAll @ ./freertos_kernel/tasks.c:2139
>S: 0x20000bc4 - vTaskSuspendAll @ ./freertos_kernel/tasks.c:2143
 D: 0x20000eb4 - vTaskDelay @ ./freertos_kernel/tasks.c:1355
>S: 0x20000eb8 - vTaskDelay @ ./freertos_kernel/tasks.c:1355
 D: 0x20000590 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5265
>S: 0x200005a0 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5280
 D: 0x20002540 - uxListRemove @ ./freertos_kernel/list.c:187
>S: 0x2000255e - uxListRemove @ ./freertos_kernel/list.c:208
 D: 0x200005a4 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5293
>S: 0x200005a8 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5293
 D: 0x200005ba - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5305
>S: 0x200005c0 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5310
 D: 0x200005d2 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5320
>S: 0x200005da - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5320
 D: 0x20002512 - vListInsert @ ./freertos_kernel/list.c:119
...
>S: 0x2000252e - vListInsert @ ./freertos_kernel/list.c:179
 D: 0x200005de - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5325
>S: 0x200005e8 - prvAddCurrentTaskToDelayedList @ ./freertos_kernel/tasks.c:5331
 D: 0x20000ebc - vTaskDelay @ ./freertos_kernel/tasks.c:1357
>S: 0x20000ebc - vTaskDelay @ ./freertos_kernel/tasks.c:1357
 D: 0x20000d18 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2217
>S: 0x20000d20 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2217
 D: 0x20000d2c - xTaskResumeAll @ ./freertos_kernel/tasks.c:2224
>S: 0x20000d2c - xTaskResumeAll @ ./freertos_kernel/tasks.c:2224
 D: 0x20002b94 - vPortRaiseBASEPRI @ ./freertos_kernel/portable/GCC/ARM_CM4F/portmacro.h:197
>S: 0x20002b9c - vPortRaiseBASEPRI @ ./freertos_kernel/portable/GCC/ARM_CM4F/portmacro.h:197
 D: 0x20002ba0 - vPortRaiseBASEPRI @ ./freertos_kernel/portable/GCC/ARM_CM4F/portmacro.h:197
>S: 0x20002bb8 - vPortEnterCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:420
 D: 0x20002bc4 - vPortEnterCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:420
>S: 0x20002bc4 - vPortEnterCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:420
 D: 0x20000d30 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2226
>S: 0x20000d38 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2228
 D: 0x20000d46 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2230
...
>S: 0x20000d3c - xTaskResumeAll @ ./freertos_kernel/tasks.c:2315
 D: 0x20002bd4 - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:427
...
>S: 0x20002bf2 - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/portmacro.h:231
 D: 0x20000d40 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2317
>S: 0x20000d42 - xTaskResumeAll @ ./freertos_kernel/tasks.c:2317
 D: 0x20000ec0 - vTaskDelay @ ./freertos_kernel/tasks.c:1366
>S: 0x20000ec2 - vTaskDelay @ ./freertos_kernel/tasks.c:1366
 D: 0x20000e8e - vTaskDelay @ ./freertos_kernel/tasks.c:1368
>S: 0x20000e9a - Exception (or debug) Entry from vTaskDelay @ ./freertos_kernel/tasks.c:1368
 D: 0x20002c00 - PendSV_Handler @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:441
...
>S: 0x20002c30 - PendSV_Handler @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:441
 D: 0x20000f08 - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3012
>S: 0x20000f12 - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3012
 D: 0x20000f1c - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3020
>S: 0x20000f2a - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3052
 D: 0x20000f44 - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3052
>S: 0x20000f4a - vTaskSwitchContext @ ./freertos_kernel/tasks.c:3052
 D: 0x20000482 - vApplicationStackOverflowHook @ ./main.c:101
```

Scanning up through the execution history, we see a `vTaskDelay()` call. This is what triggered a context switch. Prior to that call we see that there is a sequence of calls from `prvAlgoTask` (`recurse_func4` - `recurse_func0`). Since these were the functions executing prior to the context switch, it's a pretty strong indicator it was one of these functions which triggered the stack overflow. We can then go and inspect the functions for large stack allocations. Examining the code we can see that `recurse_func0` has an unbounded variable length array (VLA), `computation_buf` which likely tripped the overflow!

```c
int recurse_func0(int val) {
  uint8_t computation_buf[val];
  memset(computation_buf, val & 0xff, sizeof(computation_buf));
  uint32_t total;
  for (size_t i = 0; i < val; i++) {
    total += computation_buf[i];
  }

  return total;
}
```

Cool, looking at the trace history, we were able to hone in on the problematic code path.
