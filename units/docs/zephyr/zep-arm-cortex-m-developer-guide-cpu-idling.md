---
id: "zep-arm-cortex-m-developer-guide-cpu-idling"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / CPU Idling"
summary: "The Cortex-M architecture port implements both k_cpu_idle() and k_cpu_atomic_idle(). The implementation is present in arch/arm/core/cortex_m/cpu_idle.c."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

The Cortex-M architecture port implements both k_cpu_idle()
and k_cpu_atomic_idle(). The implementation is present in
`arch/arm/core/cortex_m/cpu_idle.c`.

In both implementations, the processor
will attempt to put the core to low power mode.
In k_cpu_idle() the processor ends up executing WFI (Wait For Interrupt)
instruction, while in k_cpu_atomic_idle() the processor will
execute a WFE (Wait For Event) instruction.

When using the CPU idling API in Cortex-M it is important to note the
following:

* Both k_cpu_idle() and k_cpu_atomic_idle() are *assumed* to be invoked
  with interrupts locked. This is taken care of by the kernel if the APIs
  are called by the idle thread.
* After waking up from low power mode, both functions will *restore*
  interrupts unconditionally, that is, regardless of the interrupt lock
  status before the CPU idle API was called.

The Zephyr CPU Idling mechanism is detailed in cpu_idle.
