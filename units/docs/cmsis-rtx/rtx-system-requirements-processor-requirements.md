---
id: "rtx-system-requirements-processor-requirements"
type: "concept"
domain: "rtos"
title: "System Requirements: Processor Requirements"
summary: "RTX assumes a fully functional processor and uses the following hardware features. It does not implement any confidence test for processor validation which should be provided by an user-supplied software test library."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/system_reqs.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/system_reqs.md#processor-requirements"
license: "Apache-2.0"
mode: "V"
---

RTX assumes a fully functional processor and uses the following hardware features. It does not implement any confidence test for processor validation which should be provided by an user-supplied software test library.

\if ARMv8M
### Cortex-M0/M0+/M23 device
\endif

\ifnot ARMv8M
### Cortex-M0/M0+ device
\endif

Hardware Requirement       | Description
:--------------------------|:------------------------------------------------------
SysTick timer              | The SysTick timer generates the kernel tick interrupts and the interface is implemented in %os_systick.c using the CMSIS_RTOS_TickAPI
Exception Handler          | RTX implements exception handlers for SVC, PendSV, and SysTick interrupt
Core Registers             | The processor status is read using the following core registers: CONTROL, IPSR, PRIMASK
System Control Block (SBC) | To control and setup the processor exceptions including PendSV and SVC
Interrupt Control          | The CMSIS-Core functions `__disable_irq` and `__enable_irq` to control the interrupt system via the CPSR core register.

The RTX implements interfaces to the processor hardware in following files:

- **irq_armv6m.S** defines exception handlers for Cortex-M0/M0+
\if ARMv8M
- **irq_armv8mbl.S** defines exception handlers for Cortex-M23
\endif
- **rtx_core_cm.h** defines processor specific helper functions and the interfaces to Core Registers and Core Peripherals.
- **os_tick.h** is the CMSIS_RTOS_TickAPI that defines the interface functions to the SysTick timer.

> **Note**
>
> - The CMSIS-Core variable SystemCoreClock is used by RTX to configure the SysTick timer.

\if ARMv8M
### Cortex-M3/M4/M7/M33/M35P/M55/M85 device
\endif

\ifnot ARMv8M
### Cortex-M3/M4/M7 device
\endif

RTX assumes a fully functional processor and uses the following hardware features:

Hardware Item              | Requirement Description
:--------------------------|:------------------------------------------------------
SysTick timer              | The SysTick timer shall be available in the processor.
System Exceptions          | The RTX requires SVC, PendSV, and SysTick exceptions and implements corresponding exception handlers.
Core Registers             | The RTX uses CONTROL, IPSR , PRIMASK and BASEPRI core registers for reading processor status.
System Control Block (SCB) | The RTX uses SCB registers to control and setup the processor system exceptions including PendSV and SVC.
NVIC Interface             | CMSIS-Core function `NVIC_GetPriorityGrouping` is used by the RTX to setup interrupt priorities.
LDREX, STREX instructions  | Exclusive access instructions LDREX and STREX are used to implement atomic execution without disabling interrupts.

The interface files to the processor hardware are:

- **irq_armv7m.S** defines exception handlers for Cortex-M3 and Cortex-M4/M7.
\if ARMv8M
- **irq_armv8mml.S** defines exception handlers for Cortex-M33/M35P/M55 and Cortex-M85
\endif
- **rtx_core_cm.h** defines processor specific helper functions and the interfaces to Core Registers and Core Peripherals.
- **os_tick.h** is the CMSIS_RTOS_TickAPI that defines the interface functions to the SysTick timer.

> **Note**
>
> - The CMSIS-Core variable SystemCoreClock is used by RTX to configure the SysTick timer.

\if ARMCA
### Cortex-A5/A7/A9 target processor

Hardware Requirement       | Description
:--------------------------|:------------------------------------------------------
Timer Peripheral           | An arbitrary timer peripheral generates the kernel tick interrupts. The interfaces for Cortex-A Generic Timer and Private Timer are implemented in %os_tick_gtim.c and %os_tick_ptim.c using the CMSIS_RTOS_TickAPI
Exception Handler          | RTX implements exception handlers for SVC, IRQ, Data Abort, Prefetch Abort and Undefined Instruction interrupt.
Core Registers             | The processor status is read using the following core registers: CPSR, CPACR and FPSCR.
LDREX, STREX instruction   | Atomic execution avoids the requirement to disable interrupts and is implemented via exclusive access instructions.
Interrupt Controller       | An interrupt controller interface is required to setup and control Timer Peripheral interrupt. The interface for Arm GIC (Generic Interrupt Controller) is implemented in %irq_ctrl_gic.c using the [IRQ Controller API](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__irq__ctrl__gr.html).

The interface files to the processor hardware are:

- **irq_armv7a.S** defines SVC, IRQ, Data Abort, Prefetch Abort and Undefined Instruction exception handlers.
- **rtx_core_ca.h** defines processor specific helper functions and the interfaces to Core Registers and Core Peripherals.
- **os_tick.h** is the CMSIS_RTOS_TickAPI that defines the interface functions to the timer peripheral.
- **irq_ctrl.h** is the [IRQ Controller API](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__irq__ctrl__gr.html) that defines the interface functions to the interrupt controller.

> **Note**
>
> - The CMSIS-Core variable `SystemCoreClock` is used by RTX to configure the timer peripheral.

\endif

### Device Memory Requirements

RTX requires RAM memory that is accessible with contiguous linear addressing.  When memory is split across multiple memory banks, some systems do not accept multiple load or store operations on this memory blocks.

RTX does not implement any confidence test for memory validation. This should be implemented by an user-supplied software test library.
