---
id: "intr-arm-cortex-m-rtos-context-switchin-context-switching"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Demystifying the FreeRTOS Context Switcher / Context Switching"
summary: "Part of: Demystifying the FreeRTOS Context Switcher"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#context-switching"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Demystifying the FreeRTOS Context Switcher_

Let's start by looking at the code that deals with context switching itself. Once we understand
that, we will cycle back to how the scheduler itself is started and tasks are created.

The **FreeRTOS** scheduler works by utilizing the built in **SysTick** and **PendSV** interrupts. The
**SysTick** is configured to fire periodically. Each time it fires, a check is performed to see if a
context switch is required by calling `xTaskIncrementTick`:

```c
void xPortSysTickHandler( void )
{
    /* The SysTick runs at the lowest interrupt priority, so when this interrupt
    executes all interrupts must be unmasked.  There is therefore no need to
    save and then restore the interrupt mask value as its value is already
    known. */
    portDISABLE_INTERRUPTS();
    {
        /* Increment the RTOS tick. */
        if( xTaskIncrementTick() != pdFALSE )
        {
            /* A context switch is required.  Context switching is performed in
            the PendSV interrupt.  Pend the PendSV interrupt. */
            portNVIC_INT_CTRL_REG = portNVIC_PENDSVSET_BIT;
        }
    }
    portENABLE_INTERRUPTS();
}
```

A context switch may also occur outside of this if a task decides to yield (`portYIELD`).

Both of these paths trigger the **PendSV** exception, where the real magic happens:

```c
// FreeRTOSConfig.h

#define vPortSVCHandler    SVC_Handler
#define xPortPendSVHandler PendSV_Handler
#define xPortSysTickHandler SysTick_Handler

// port.c
void xPortPendSVHandler( void )
{
    /* This is a naked function. */

    __asm volatile
        (
        "       mrs r0, psp                     \n"
        "       isb                             \n"
        "                                       \n"
        "       ldr     r3, pxCurrentTCBConst   \n" /* Get the location of the current TCB. */
        "       ldr     r2, [r3]                \n"
        "                                       \n"
        "       tst r14, #0x10                  \n" /* Is the task using the FPU context?  If so, push high vfp registers. */
        "       it eq                           \n"
        "       vstmdbeq r0!, {s16-s31}         \n"
        "                                       \n"
        "       stmdb r0!, {r4-r11, r14}        \n" /* Save the core registers. */
        "       str r0, [r2]                    \n" /* Save the new top of stack into the first member of the TCB. */
        "                                       \n"
        "       stmdb sp!, {r0, r3}             \n"
        "       mov r0, %0                      \n"
        "       msr basepri, r0                 \n"
        "       dsb                             \n"
        "       isb                             \n"
        "       bl vTaskSwitchContext           \n"
        "       mov r0, #0                      \n"
        "       msr basepri, r0                 \n"
        "       ldmia sp!, {r0, r3}             \n"
        "                                       \n"
        "       ldr r1, [r3]                    \n" /* The first item in pxCurrentTCB is the task top of stack. */
        "       ldr r0, [r1]                    \n"
        "                                       \n"
        "       ldmia r0!, {r4-r11, r14}        \n" /* Pop the core registers. */
        "                                       \n"
        "       tst r14, #0x10                  \n" /* Is the task using the FPU context?  If so, pop the high vfp registers too. */
        "       it eq                           \n"
        "       vldmiaeq r0!, {s16-s31}         \n"
        "                                       \n"
        "       msr psp, r0                     \n"
        "       isb                             \n"
        "                                       \n"
        "                                       \n"
        "       bx r14                          \n"
        "                                       \n"
        "       .align 4                        \n"
        "pxCurrentTCBConst: .word pxCurrentTCB  \n"
        ::"i"(configMAX_SYSCALL_INTERRUPT_PRIORITY)
    );
}
```

Let's halt the debugger in this function and step through instruction by instruction discussing
what is actually happening.

```
(gdb) mon reset
Resetting target
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
prvQueuePingTask (pvParameters=<optimized out>) at main.c:33
33      __asm("bkpt 1");
(gdb) break PendSV_Handler
Breakpoint 2 at 0x1430: file freertos_kernel/portable/GCC/ARM_CM4F/port.c, line 435.
(gdb) n
34      xQueueSend(xQueue, &ulValueToSend, 0U);
(gdb) c
Continuing.

Breakpoint 2, PendSV_Handler () at freertos_kernel/portable/GCC/ARM_CM4F/port.c:435
435		__asm volatile
```

Great, we are halted on the first line of the context switcher. As we discussed
[above](#context-state-stacking), the hardware will automatically save registers on exception
entry for us. We can figure out how things are stacked by looking at the current `lr` value which
encodes [this information](#exception-entry-pseudocode).

```
(gdb) p/x $lr
$7 = 0xfffffffd
```

Using this info we know that the code was executing in thread mode and using the
`psp` for it's stack. We also know that the FPU context was **not** active.

This tells us a [**basic frame**](#basic-context-state-frame) was saved by the hardware on the
`psp`. We can walk up the stack using `x/a` with `gdb` to dump the register values.
I've annotated the registers being read inline below:

```
(gdb) x/a $psp // top of stack will be $r0
0x200005a0 <ucHeap+1096>:	0x1 <g_pfnVectors+1>
(gdb) <enter to get $r1>
0x200005a4 <ucHeap+1100>:	0x200003b4 <ucHeap+604>
(gdb) <enter to get $r2>
0x200005a8 <ucHeap+1104>:	0x10000000
(gdb) <enter to get $r3>
0x200005ac <ucHeap+1108>:	0x0 <g_pfnVectors>
(gdb) <enter to get $r12 >
0x200005b0 <ucHeap+1112>:	0x200001a8 <ucHeap+80>
(gdb) <enter to get $lr>
0x200005b4 <ucHeap+1116>:	0xbd1 <xQueueGenericSend+152>
(gdb) <enter to get ReturnAddress>
0x200005b8 <ucHeap+1120>:	0x1422 <vPortExitCritical+30>
(gdb) <enter to get xPSR>
// notice bit 9 is not set so there is no padding byte
0x200005bc <ucHeap+1124>:	0x6100f000
```

Now we are ready to walk through the assembly code that makes up the context switcher. First we have:

```c
        "       mrs r0, psp                     \n"
        "       isb                             \n"
```

We see that the current location of the `psp` (the stack that was in use prior to exception entry) is
loaded into `r0` using the `mrs` instruction detailed [above](#mrs-register-info). This is followed by
an `isb` (**Instruction Synchronization Barrier**) which flushes the instruction pipeline
guaranteeing any instruction which follows will be re-fetched. Technically it doesn't really serve
any purpose here and shouldn't be required at all[^14].

```
// step over the first two instructions (can also type "si 2" for short)
(gdb) step instruction 2
```

Moving on we have:

```c
        "       ldr     r3, pxCurrentTCBConst   \n" /* Get the location of the current TCB. */
        "       ldr     r2, [r3]                \n"
[...]
        "pxCurrentTCBConst: .word pxCurrentTCB  \n"
```

What's happening here is a label with the location of the C variable, `pxCurrentTCB`, is loaded into
`$r3`. Then the value of pxCurrentTCB gets loaded into `$r2`. We can confirm this by stepping through
the two instructions and comparing the registers with the C types.

```
(gdb) step instruction
(gdb) p/x $r3
$23 = 0x20000008
(gdb) p &pxCurrentTCB
$24 = (TCB_t * volatile *) 0x20000008 <pxCurrentTCB>
(gdb) step instruction
(gdb) p/x $r2
$25 = 0x20000610
(gdb) p pxCurrentTCB
$26 = (TCB_t * volatile) 0x20000610 <ucHeap+1208>
```

Next we have:

```c
        "       tst r14, #0x10                  \n" /* Is the task using the FPU context?  If so, push high vfp registers. */
        "       it eq                           \n"
        "       vstmdbeq r0!, {s16-s31}         \n"
```

This set of instructions checks to see if the FPU Context was active prior to exception
entry. This can be resolved by reading the information passed via the `$lr` register on exception
entry (more details [above](#exception-entry-pseudocode)). If bit 5 is 0, the FPU is active,
otherwise it is not. The `tst` (**Test**) instruction performs a logical AND operation between the
register and the immediate value provided (so in this case `r14 & 0x10`). It then populates
condition flags in the PSR register based on the result. Condition flags available include a "Zero
condition flag" which means the result of the AND was zero.

The `it` (**If-Then**) instruction is then used to conditionally execute further
instructions based on the current state in the condition flags. `it eq` is shorthand for "if the
result of the last comparison was zero then execute the instruction that follows". The following
instruction pushes the callee-saved floating point registers onto the `psp` (currently stored in `r0`). In our
case the result is **not** zero so this instruction should be skipped. We should see the psp
remains unchanged from the value we originally dumped:

```
(gdb) p/x $r0
$1 = 0x200005a0
(gdb) si 4
(gdb) x/i $pc
=> 0x1446 <PendSV_Handler+22>:	stmdb	r0!, {r4, r5, r6, r7, r8, r9, r10, r11, lr}
(gdb) p/x $r0
$1 = 0x200005a0
```

> WARNING: Over the years I've seen a lot of nasty stack overflows arise here which can be tricky
> to track down. As _soon_ as an FPU instruction is used an additional 132 bytes will be pushed on
> the stack, which can lead to unexpected overflows of small embedded stacks

This brings us to the next part which is pretty self explanatory:

```c
        "       stmdb r0!, {r4-r11, r14}        \n" /* Save the core registers. */
        "       str r0, [r2]                    \n" /* Save the new top of stack into the first member of the TCB. */
```

We push all the callee-saved core
registers onto `psp` using the `stmdb` (**Store Multiple Decrement Before stores multiple
registers**) instruction and then update the first word in our `pxCurrentTCB` pointer with the
updated stack location (stored in `r0`).

`pxCurrentTCB` is a **FreeRTOS** symbol that is _always_
populated with the running task. A TCB (**Task Control Block**) contains various state associated
with the task. Looking at the source code we see the first word is:

```c
typedef struct tskTaskControlBlock /_ The old naming convention is used to prevent breaking kernel aware debuggers. _/
{
volatile StackType_t _pxTopOfStack; /_< Points to the location of the last item placed on
the tasks stack. THIS MUST BE THE FIRST MEMBER OF THE TCB STRUCT. \*/
[...]
```

We can also look confirm this is what is happening by comparing the C types with register values
within `gdb`:

```
(gdb) si
0x0000144a	435		__asm volatile
(gdb) p/x $r0
$2 = 0x2000057c
(gdb) x/i $pc
=> 0x144a <PendSV_Handler+26>:	str	r0, [r2, #0]
(gdb) p/x pxCurrentTCB->pxTopOfStack
$3 = 0x200005a4
(gdb) si
0x0000144c	435		__asm volatile
(gdb) p/x pxCurrentTCB->pxTopOfStack
$4 = 0x2000057c
```

Awesome! At this point we have saved all the register state of the original task and recorded that
location within the task specific TCB context. Now it's time to actually **context switch** over to
a new task:

```c
        "       stmdb sp!, {r0, r3}             \n"
        "       mov r0, %0                      \n"
        "       msr basepri, r0                 \n"
        "       dsb                             \n"
        "       isb                             \n"
        "       bl vTaskSwitchContext           \n"
[...]
        ::"i"(configMAX_SYSCALL_INTERRUPT_PRIORITY)
```

We see the port uses a GCC feature known as **Extended Asm**[^15] to mix C macros with ARM
assembly. This block prepares to call the context switch logic, `vTaskSwitchContext`, a C function which
determines the next task to run. First the "argument" registers are saved on the active stack
(always `msp` for exceptions). Next interrupts below `configMAX_SYSCALL_INTERRUPT_PRIORITY`
are disabled since it is only safe to access the data structures accessed by `vTaskSwitchContext`
without interruption. If interrupts were not disabled, the context switching code could be
preempted and a call to a **FreeRTOS** `*_FromISR()` API could corrupt the data structure.

When lowering the effective execution level, an `isb` instruction **is** required for the new priority to be visible for future
instructions. The `dsb` instruction shouldn't be explicitly necessary here[^16]. Finally we call
the C function. From **FreeRTOS** documentation we can conclude what will happen:

```c
/*
 * THIS FUNCTION MUST NOT BE USED FROM APPLICATION CODE.  IT IS ONLY
 * INTENDED FOR USE WHEN IMPLEMENTING A PORT OF THE SCHEDULER AND IS
 * AN INTERFACE WHICH IS FOR THE EXCLUSIVE USE OF THE SCHEDULER.
 *
 * Sets the pointer to the current TCB to the TCB of the highest priority task
 * that is ready to run.
 */
 portDONT_DISCARD void vTaskSwitchContext( void ) PRIVILEGED_FUNCTION;
```

So when the function returns `pxCurrentTCB` should be populated with the new task to switch to.
Let's try it out!

```
// display the name
(gdb) p pxCurrentTCB->pcTaskName
$6 = "Ping", '\000' <repeats 11 times>
(gdb) si 5
0x00001460	435		__asm volatile
(gdb) x/i $pc
=> 0x1460 <PendSV_Handler+48>:	bl	0x760 <vTaskSwitchContext>
// step over the function call using "next instruction" ("ni")
(gdb) ni
0x00001464	435		__asm volatile
(gdb) x/i $pc
=> 0x1464 <PendSV_Handler+52>:	mov.w	r0, #0
(gdb) p pxCurrentTCB->pcTaskName
$7 = "Pong", '\000' <repeats 11 times>
```

We see that the pxCurrentTCB has changed from the "Ping" task to the "Pong" task.

Upon return from the function call, all interrupts are re-enabled by resetting `basepri` to 0 and the initial values of
the argument registers (`$r0`-`$r3`) prior to the function invocation are restored by popping them
off the stack. No synchronization instructions are required for the `msr` call because the
ARM core will actually take care of this for you when the execution priority increases [^17]. Let's
step over this block:

```c
        "       mov r0, #0                      \n"
        "       msr basepri, r0                 \n"
        "       ldmia sp!, {r0, r3}             \n"
```

```
(gdb) si 3
0x0000146e in PendSV_Handler () at freertos_kernel/portable/GCC/ARM_CM4F/port.c:435
435		__asm volatile
(gdb) x/i $pc
=> 0x146e <PendSV_Handler+62>:	ldr	r1, [r3, #0]
```

Now it's time to actually start up the new task. Recall when we saved the "Ping" task state above, we placed the
location of the task stack in `pxTopOfStack`. So to recover the task state of the "Pong" task we
just need to do the opposite. First this requires loading up the new TCB_t that `pxCurrentTCB` points to:

```c
        "       ldr r1, [r3]                    \n" /* The first item in pxCurrentTCB is the task top of stack. */
        "       ldr r0, [r1]                    \n"
```

```
(gdb) p/x pxCurrentTCB
$8 = 0x200003b0
(gdb) si
0x00001470	435		__asm volatile
(gdb) p/x $r1
$11 = 0x200003b0
(gdb) p/x pxCurrentTCB->pxTopOfStack
$12 = 0x20000324
(gdb) si
0x00001472	435		__asm volatile
(gdb) p/x $r0
$13 = 0x20000324
```

`r0` now holds a pointer to the top of the stack for the task we want to switch to. First we pop
the callee-saved core registers using the `ldmia` (**Load Multiple Increment After**) instruction,
then we check the restored value in the `$lr / $r14` register to determine if there is any FPU
state which needs to be restored as well (in our case, it does **not**):

```c
        "       ldmia r0!, {r4-r11, r14}        \n" /* Pop the core registers. */
        "                                       \n"
        "       tst r14, #0x10                  \n" /* Is the task using the FPU context?  If so, pop the high vfp registers too. */
        "       it eq                           \n"
        "       vldmiaeq r0!, {s16-s31}         \n"
        "                                       \n"
```

```
(gdb) si 4
0x00001480	435		__asm volatile
(gdb) x/i $pc
=> 0x1480 <PendSV_Handler+80>:	msr	PSP, r0
```

Now `r0` points to the location of the program stack _exactly_ as it was when the "Pong" task originally got context
switched out via the PendSV exception handler! Let's take a look at the stack just like we did on
exception entry:

```
(gdb) x/a $r0 // contains $r0 value for "Pong" task
0x20000348 <ucHeap+496>:	0x0 <g_pfnVectors>
(gdb) < enter for $r1 >
0x2000034c <ucHeap+500>:	0x200003b4 <ucHeap+604>
(gdb) < enter for $r2 >
0x20000350 <ucHeap+504>:	0x20000000 <uxCriticalNesting>
(gdb) < enter for $r3 >
0x20000354 <ucHeap+508>:	0x10000000
(gdb) < enter for $r12 >
0x20000358 <ucHeap+512>:	0x0 <g_pfnVectors>
(gdb) < enter for $r14 / $lr >
0x2000035c <ucHeap+516>:	0x5d9 <xTaskResumeAll+40>
(gdb) < enter for ReturnAddress - the pc that should be fetched upon return >
0x20000360 <ucHeap+520>:	0xe2a <xQueueReceive+246>
(gdb) < psr value>
0x20000364 <ucHeap+524>:	0x61000000
```

The last thing we need to do is change the location of the `psp` to match the value in `r0`
and populate the link register (`r14`) with the special [EXC_RETURN](#exc-return-info) value we
just recovered from the "Pong" task stack with the `ldmia` instruction. This will tell the hardware
how return to Thread Mode and restore the context state that was automatically saved correctly:

```c
        "       msr psp, r0                     \n"
        "       isb                             \n"
        "                                       \n"
        "                                       \n"
        "       bx r14                          \n"
        "                                       \n"
```

Based on the dump of the top of the "Pong" stack we did above, we expect to see `$sp=0x20000368`,
`$pc=0xe2a`, `$lr=0x5d9` after the branch to `r14`. Let's give it a try:

```
// state prior to branching
(gdb) info reg
[...]
sp             0x20002a88          0x20002a88
lr             0xfffffffd          4294967293
pc             0x1480              0x1480 <PendSV_Handler+80>
xpsr           0x2100000e          553648142
msp            0x20002a88          536881800
psp            0x200005a0          536872352
[...]
(gdb) si 3
// state after branching
xQueueReceive (xQueue=0x20000160 <ucHeap+8>, pvBuffer=pvBuffer@entry=0x2000039c <ucHeap+580>, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at freertos_kernel/queue.c:1378
1378						portYIELD_WITHIN_API();
(gdb) info reg
sp             0x20000368          0x20000368 <ucHeap+528>
lr             0x5d9               1497
pc             0xe2a               0xe2a <xQueueReceive+246>
xpsr           0x61000000          1627389952
msp            0x20002a88          536881800
psp            0x20000368          536871784
(gdb) bt
#0  xQueueReceive (xQueue=0x20000160 <ucHeap+8>, pvBuffer=pvBuffer@entry=0x2000039c <ucHeap+580>, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at freertos_kernel/queue.c:1378
#1  0x00000084 in prvQueuePongTask (pvParameters=<optimized out>) at main.c:41
#2  0x00001334 in ?? () at freertos_kernel/portable/GCC/ARM_CM4F/port.c:703
```

They values match! We've successfully completed a context switch and are running the pong task!
