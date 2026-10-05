---
id: "zep-interrupts-concepts"
type: "concept"
domain: "rtos"
title: "Interrupts: Concepts"
summary: "Any number of ISRs can be defined (limited only by available RAM), subject to the constraints imposed by underlying hardware."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of ISRs can be defined (limited only by available RAM), subject to
the constraints imposed by underlying hardware.

An ISR has the following key properties:

* An **interrupt request (IRQ) signal** that triggers the ISR.
* A **priority level** associated with the IRQ.
* An **interrupt service routine** that is invoked to handle the interrupt.
* An **argument value** that is passed to that function.

An `IDT (Interrupt Descriptor Table)` or a vector table is used
to associate a given interrupt source with a given ISR.
Only a single ISR can be associated with a specific IRQ at any given time.

Multiple ISRs can utilize the same function to process interrupts,
allowing a single function to service a device that generates
multiple types of interrupts or to service multiple devices
(usually of the same type). The argument value passed to an ISR's function
allows the function to determine which interrupt has been signaled.

The kernel provides a default ISR for all unused IDT entries. This ISR
generates a fatal system error if an unexpected interrupt is signaled.

The kernel supports **interrupt nesting**. This allows an ISR to be preempted
in mid-execution if a higher priority interrupt is signaled. The lower
priority ISR resumes execution once the higher priority ISR has completed
its processing.

An ISR executes in the kernel's **interrupt context**. This context has its
own dedicated stack area (or, on some architectures, stack areas). The size
of the interrupt context stack must be capable of handling the execution of
multiple concurrent ISRs if interrupt
nesting support is enabled.


**Important:** Many kernel APIs can be used only by threads, and not by ISRs. In cases where a routine may be invoked by both threads and ISRs the kernel provides the `k_is_in_isr` API to allow the routine to alter its behavior depending on whether it is executing as part of a thread or as part of an ISR.


### Multi-level Interrupt Handling


A hardware platform can support more interrupt lines than natively-provided
through the use of one or more nested interrupt controllers.  Sources of
hardware interrupts are combined into one line that is then routed to
the parent controller.

If nested interrupt controllers are supported, `CONFIG_MULTI_LEVEL_INTERRUPTS`
should be enabled, and `CONFIG_2ND_LEVEL_INTERRUPTS` and
`CONFIG_3RD_LEVEL_INTERRUPTS` configured as well, based on the
hardware architecture.

A unique 32-bit interrupt number is assigned with information
embedded in it to select and invoke the correct Interrupt
Service Routine (ISR). Each interrupt level is given a byte within this 32-bit
number, providing support for up to four interrupt levels using this arch, as
illustrated and explained below:

```none

          9                           2       0
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│   │   │ ╷ │   │   │   │   │ A │   │ ╷ │   │   │               (LEVEL 1)
└───┴───┴─│─┴───┴───┴───┴───┴───┴───┴─│─┴───┴───┘
          └─────────────────┐         └─────────────────────┐
      5                     v                               v
┌───┬───┬───┬───┬───┬───┬───┐   ┌───┬───┬───┬───┬───┬───┬───┐
│   │ ╷ │   │ C │   │   │   │   │   │   │   │   │ B │   │   │   (LEVEL 2)
└───┴─│─┴───┴───┴───┴───┴───┘   └───┴───┴───┴───┴───┴───┴───┘
      └─────────────────────┐
                            v
┌───┬───┬───┬───┬───┬───┬───┐
│   │   │   │   │ D │   │   │                                   (LEVEL 3)
└───┴───┴───┴───┴───┴───┴───┘
```
There are three interrupt levels shown here.

* A cell represents an interrupt line and is numbered from 0 (right most).
* LEVEL 1 has 12 interrupt lines, with two lines (2 and 9) connected
  to nested controllers and one device 'A' on line 4.
* One of the LEVEL 2 controllers has interrupt line 5 connected to
  a LEVEL 3 nested controller and one device 'C' on line 3.
* The other LEVEL 2 controller has no nested controllers but has one
  device 'B' on line 2.
* The LEVEL 3 controller has one device 'D' on line 2.

Here's how unique interrupt numbers are generated for each
hardware interrupt.  Let's consider four interrupts shown above
as A, B, C, and D:

```none

A -> 0x00000004
B -> 0x00000302
C -> 0x00000409
D -> 0x00030609
```

**Note:** The bit positions for LEVEL 2 and onward are offset by 1, as 0 means that interrupt number is not present for that level. For our example, the LEVEL 3 controller has device D on line 2, connected to the LEVEL 2 controller's line 5, that is connected to the LEVEL 1 controller's line 9 (2 -> 5 -> 9). Because of the encoding offset for LEVEL 2 and onward, device D is given the number 0x00030609.


### Preventing Interruptions


In certain situations it may be necessary for the current thread to
prevent ISRs from executing while it is performing time-sensitive
or critical section operations.

A thread may temporarily prevent all IRQ handling in the system using
an **IRQ lock**. This lock can be applied even when it is already in effect,
so routines can use it without having to know if it is already in effect.
The thread must unlock its IRQ lock the same number of times it was locked
before interrupts can be once again processed by the kernel while the thread
is running.


**Important:** A thread is not allowed to sleep while holding an IRQ lock; only isr-ok functions may be called.

Alternatively, a thread may temporarily **disable** a specified IRQ
so its associated ISR does not execute when the IRQ is signaled.
The IRQ must be subsequently **enabled** to permit the ISR to execute.


**Important:** Disabling an IRQ prevents *all* threads in the system from being preempted by the associated ISR, not just the thread that disabled the IRQ.


#### Zero Latency Interrupts


Preventing interruptions by applying an IRQ lock may increase the observed
interrupt latency. A high interrupt latency, however, may not be acceptable
for certain low-latency use-cases.

The kernel addresses such use-cases by allowing interrupts with critical
latency constraints to execute at a priority level that cannot be blocked
by interrupt locking. These interrupts are defined as
*zero-latency interrupts*. The support for zero-latency interrupts requires
`CONFIG_ZERO_LATENCY_IRQS` to be enabled. Any interrupts
configured as zero-latency must also be declared as :ref:`direct ISRs
<direct_isrs>` (and must not use the `ISR_DIRECT_PM` in them), since
regular ISRs interact with the kernel. In addition to that, the flag
`IRQ_ZERO_LATENCY` must be passed to the `IRQ_DIRECT_CONNECT`
macro to configure the particular interrupt with
zero latency. Declaring a zero-latency interrupt ISR to be both direct and
dynamic is possible on some architectures, see direct_isrs.

Zero-latency interrupts are expected to be used to manage hardware events
directly, and not to interoperate with the kernel code at all. They should
treat all kernel APIs as undefined behavior (i.e. an application that uses the
APIs inside a zero-latency interrupt context is responsible for directly
verifying correct behavior). Zero-latency interrupts may not modify any data
inspected by kernel APIs invoked from normal Zephyr contexts and shall not
generate exceptions that need to be handled synchronously (e.g. kernel panic).

When system power management keeps interrupts locked across PM resume, a
zero-latency interrupt is outside the locked-resume ordering and may be
dispatched during PM suspend/resume logic, before PM resume bookkeeping and
SoC/device hardware restore have completed. Such an ISR must be PM-wake-safe, or
the interrupt source must be masked or disabled while the system state does not
allow the ISR to execute. See :ref:`device power policy constraints
<pm-device-constraint>` for one way to keep unsafe states out of policy
selection while a device path that can produce a zero-latency interrupt is
active.


**Important:** Zero-latency interrupts are supported on an architecture-specific basis. The feature is currently implemented in the ARM Cortex-M architecture variant.


**Tip:** To mitigate flash access latency, consider relocating ISRs and all related symbols to RAM.


### Offloading ISR Work


An ISR should execute quickly to ensure predictable system operation.
If time consuming processing is required the ISR should offload some or all
processing to a thread, thereby restoring the kernel's ability to respond
to other interrupts.

The kernel supports several mechanisms for offloading interrupt-related
processing to a thread.

* An ISR can signal a helper thread to do interrupt-related processing
  using a kernel object, such as a FIFO, LIFO, or semaphore.

* An ISR can instruct the system workqueue thread to execute a work item.
  (See workqueues_v2.)

When an ISR offloads work to a thread, there is typically a single context
switch to that thread when the ISR completes, allowing interrupt-related
processing to continue almost immediately. However, depending on the
priority of the thread handling the offload, it is possible that
the currently executing cooperative thread or other higher-priority threads
may execute before the thread handling the offload is scheduled.


### Sharing interrupt lines


In the case of some hardware platforms, the same interrupt lines may be used
by different IPs. For example, interrupt 17 may be used by a DMA controller to
signal that a data transfer has been completed or by a DAI controller to signal
that the transfer FIFO has reached its watermark. To make this work, one would
have to either employ some special logic or find a workaround (for example, using
the shared_irq interrupt controller), which doesn't scale very well.

To solve this problem, one may use shared interrupts, which can be enabled using
`CONFIG_SHARED_INTERRUPTS`. Whenever an attempt to register
a second ISR/argument pair on the same interrupt line is made (using
`IRQ_CONNECT` or `irq_connect_dynamic`), the interrupt line will
become shared, meaning the two ISR/argument pairs (previous one and the one that
has just been registered) will be invoked each time the interrupt is triggered.
The entities that make use of an interrupt line in the shared interrupt context
are known as clients. The maximum number of allowed clients for an interrupt is
controlled by `CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS`.

Interrupt sharing is transparent to the user. As such, the user may register
interrupts using `IRQ_CONNECT` and `irq_connect_dynamic` as
they normally would. The interrupt sharing is taken care of behind the scenes.

Enabling the shared interrupt support and dynamic interrupt support will
allow users to dynamically disconnect ISRs using `irq_disconnect_dynamic`.
After an ISR is disconnected, whenever the interrupt line for which it was
register gets triggered, the ISR will no longer get invoked.

Please note that enabling `CONFIG_SHARED_INTERRUPTS` will
result in a non-negligible increase in the binary size. Use with caution.
