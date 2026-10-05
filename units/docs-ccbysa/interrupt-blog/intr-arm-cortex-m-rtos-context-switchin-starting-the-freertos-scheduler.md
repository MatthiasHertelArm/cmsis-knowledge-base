---
id: "intr-arm-cortex-m-rtos-context-switchin-starting-the-freertos-scheduler"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Demystifying the FreeRTOS Context Switcher / Starting the FreeRTOS Scheduler"
summary: "Part of: Demystifying the FreeRTOS Context Switcher"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#starting-the-freertos-scheduler"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Demystifying the FreeRTOS Context Switcher_

The astute observer reader may wonder how the scheduler starts in the first place. What happens if
a **PendSV** gets triggered but there isn't a currently running task because the system just booted?!

There are several different strategies but a common pattern an RTOS will follow when creating a new task is
to initialize the task stack to look like it had been context switched out by the scheduler. Then
to start the scheduler itself by triggering a SVC exception with the `svc` instruction. This way
starting a thread is nearly identical to context switching to a thread.

During initialization you will also usually find a couple extra configuration settings such as:

- Configuration as to whether or not tasks operate at privileged or unprivileged level
- **FP Extension** configuration (i.e whether or not the FPU is enabled and what context stacking
  schema to use). For example, the port used in the example does the following FPU configuration:

```c
static void vPortEnableVFP( void )
{
    __asm volatile
    (
        "	ldr.w r0, =0xE000ED88		\n" /* The FPU enable bits are in the CPACR. */
        "	ldr r1, [r0]				\n"
        "								\n"
        "	orr r1, r1, #( 0xf << 20 )	\n" /* Enable CP10 and CP11 coprocessors, then save back. */
        "	str r1, [r0]				\n"
        "	bx r14						"
    );
}
[...]
BaseType_t xPortStartScheduler( void )
{
[...]
    /* Ensure the VFP is enabled - it should be anyway. */
    vPortEnableVFP();

    /* Lazy save always. */
    *( portFPCCR ) |= portASPEN_AND_LSPEN_BITS;
[...]
```

To start **FreeRTOS** and get tasks to run`vTaskStartScheduler` needs to be called. If you are
interested in taking a closer look at this logic, I'd recommend looking at are `pxPortInitialiseStack`,
`xPortStartScheduler`, and `vPortSVCHandler` functions in `port.c`.
