---
id: "zep-arm-cortex-m-developer-guide-interrupt-handling-features"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Interrupt handling features"
summary: "This section describes certain aspects around exception and interrupt handling in Arm Cortex-M."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

This section describes certain aspects around exception and interrupt
handling in Arm Cortex-M.


#### Interrupt priority levels


The number of available (configurable) interrupt priority levels is
determined by the number of implemented interrupt priority bits in
NVIC; this needs to be described for each Cortex-M platform using
DeviceTree:

```devicetree

&nvic {
        arm,num-irq-priority-bits = <#priority-bits>;
};
```

#### Reserved priority levels


A number of interrupt priority levels are reserved for the OS.

By design, system fault exceptions have the highest priority level. In
*Baseline* Cortex-M, this is actually enforced by hardware, as HardFault
is the only available processor fault exception, and its priority is
higher than any configurable exception priority.

In *Mainline* Cortex-M, the available fault exceptions (e.g. MemManageFault,
UsageFault, etc.) are assigned the highest *configurable* priority level.
(`CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS` signifies explicitly
that the Cortex-M implementation supports configurable fault priorities.)

This priority level is never shared with HW interrupts (an exception to
this rule is described below). As a result, processor faults occurring in regular
ISRs will be handled by the corresponding fault handler and will not escalate to
a HardFault, *similar to processor faults occurring in thread mode*.

SVC exception is normally configured with the highest configurable priority level
(an exception to this rule will be described below).
SVCs are used by the Zephyr kernel to dispatch system calls, trigger runtime
system errors (e.g. Kernel oops or panic), or implement IRQ offloading.

In Baseline Cortex-M the priority level of SVC may be shared with other exceptions
or HW interrupts that are also given the highest configurable priority level (As a
result of this, kernel runtime errors during interrupt handling will escalate to
HardFault. Additional logic in the fault handling routines ensures that such
runtime errors are detected successfully).

In Mainline Cortex-M, however, the SVC priority level is *reserved*, thus normally it
is only shared with the fault exceptions of configurable priority. This simplifies the
fault handling routines in Mainline Cortex-M architecture, since runtime kernel errors
are serviced by the SVC handler (i.e no HardFault escalation, even if the kernel errors
occur in ISR context).

HW interrupts in Mainline Cortex-M builds are allocated a priority level lower than the SVC.

One exception to the above rules is when Zephyr applications support Zero Latency Interrupts
(ZLIs). Such interrupts are designed to have a priority level higher than any HW or system
interrupt. If the ZLI feature is enabled in Mainline Cortex-M builds (see
`CONFIG_ZERO_LATENCY_IRQS`), then

* ZLIs are assigned the highest configurable priority level
* SVCs are assigned the second highest configurable priority level
* Regular HW interrupts are assigned priority levels lower than SVC.

The priority level configuration in Cortex-M is implemented in
`include/zephyr/arch/arm/cortex_m/exception.h`.


#### Locking and unlocking IRQs


In Baseline Cortex-M locking interrupts is implemented using the PRIMASK register.

```c

arch_irq_lock()
```
will set the PRIMASK register to 1, eventually, masking all IRQs with configurable
priority. While this fulfils the OS requirement of locking interrupts, the consequence
is that kernel runtime errors (triggering SVCs) will escalate to HardFault.

In Mainline Cortex-M locking interrupts is implemented using the BASEPRI register (Mainline
Cortex-M builds select `CONFIG_CPU_CORTEX_M_HAS_BASEPRI` to signify that BASEPRI register is
implemented.). By modifying BASEPRI (or BASEPRI_MAX) arch_irq_lock() masks all system and HW
interrupts with the exception of

* SVCs
* processor faults
* ZLIs

This allows zero latency interrupts to be triggered inside OS critical sections.
Additionally, this allows system (processor and kernel) faults to be handled by Zephyr
in *exactly the same way*, regardless of whether IRQs have been locked or not when the
error occurs. It also allows for system calls to be dispatched while IRQs are locked.


**Note:** Mainline Cortex-M fault handling is designed and configured in a way that all processor and kernel faults are handled by the corresponding exception handlers and never result in HardFault escalation. In other words, a HardFault may only occur in Zephyr applications that have modified the default fault handling configurations. The main reason for this design was to reserve the HardFault exception for handling exceptional error conditions in safety critical applications.


#### Dynamic direct interrupts


Cortex-M builds support the installation of direct interrupt service routines during
runtime. Direct interrupts are designed for performance-critical interrupt
handling and do not go through all of the common Zephyr interrupt handling
code.

Direct dynamic interrupts are enabled via switching on
`CONFIG_DYNAMIC_DIRECT_INTERRUPTS`.

Note that enabling direct dynamic interrupts requires enabling support for
dynamic interrupts in the kernel, as well (see `CONFIG_DYNAMIC_INTERRUPTS`).


#### Zero Latency interrupts


As described above, in Mainline Cortex-M applications, the Zephyr kernel reserves
the highest configurable interrupt priority level for its own use (SVC). SVCs will
not be masked by interrupt locking. Zero-latency interrupt can be used to set up
an interrupt at the highest interrupt priority which will not be blocked by interrupt
locking. To use the ZLI feature `CONFIG_ZERO_LATENCY_IRQS` needs to be enabled.

Zero latency IRQs have minimal interrupt latency, as they will always preempt regular HW
or system interrupts.

Note, however, that since ZLI ISRs will run at a priority level higher than the kernel
exceptions they **cannot use** any kernel functionality. Additionally, since the ZLI
interrupt priority level is equal to processor fault priority level, faults occurring
in ZLI ISRs will escalate to HardFault and will not be handled in the same way as regular
processor faults. Developers need to be aware of this limitation.
