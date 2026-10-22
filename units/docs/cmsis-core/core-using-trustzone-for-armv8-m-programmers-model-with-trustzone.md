---
id: "core-using-trustzone-for-armv8-m-programmers-model-with-trustzone"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M: Programmers Model with TrustZone"
summary: "The figure Secure Memory Map shows the memory view for the Secure state. In the Secure state all memory and peripherals can be accessed."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/using_tz.md#programmers-model-with-trustzone"
license: "Apache-2.0"
mode: "V"
---

The figure **Secure Memory Map** shows the memory view for the **Secure state**. In the Secure state all memory and peripherals can be accessed. The **System Control and Debug** area provides access to secure peripherals and non-secure peripherals that are mirrored at a memory alias.

The secure peripherals are only accessible during program execution in **Secure state**. The Secure Attribute Unit (SAU) configures the non-secure memory, peripheral, and interrupt access. Also available are a secure MPU (memory protection unit), secure SCB (system control block), and secure SysTick timer.

The system supports two separate interrupt vector tables for secure and non-secure code execution.

This interrupt assignment is controlled during **Secure state** code execution via the NVIC (nested vector interrupt controller).



(figure: Secure Memory Map)

The figure **Non-Secure Memory Map** shows the memory view for the Non-secure state. This memory view is identical to the traditional Cortex-M memory map. Access to any secure memory or peripheral space triggers the secure exception that executes a handler in **Secure state**.

The partition_h_pg defines the initial setup of the **Non-Secure Memory Map** during system start in the Secure state (refer to functions SystemInit and TZ_SAU_Setup).



(figure: Non-Secure Memory Map)

The figure **Registers** shows the register view of the Armv8-M system with TrustZone. As the general purpose registers are can be accessed from any state (secure or non-secure), function calls between the states use these registers for parameter and return values.

The register R13 is the stack pointer alias, and the actual stack pointer (PSP_NS, MSP_NS, PSP_S, MSP_S) accessed depends on state (Secure or Non-secure) and mode (handler=exception/interrupt execution or thread=normal code execution).

In Armv8-M Mainline, each stack pointer has a limit register (PSPLIM_NS, MSPLIM_NS, PSPLIM_S, MSPLIM_S) that traps stack overflows with the **UsageFault** exception (register UFSR bit STKOF=1).

An Armv8-M system with TrustZone has an independent **CONTROL** register for each state (Secure or Non-secure).

The interrupt/exception control registers (PRIMASK, FAULTMASK, BASEPRI) are banked between the states (Secure or Non-secure), however the interrupt priority for the Non-Secure state can be lowered (SCB_AIRCR register bit PRIS) so that secure interrupts have always higher priority.

The core registers of the current state (Secure or Non-secure) are accessed using the standard Core_Register_gr functions. In Secure state all non-secure registers are accessible using the coreregister_trustzone_functions related to TrustZone for Armv8-M.

(figure: Registers)
