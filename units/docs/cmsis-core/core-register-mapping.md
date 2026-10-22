---
id: "core-register-mapping"
type: "concept"
domain: "core"
title: "Register Mapping"
summary: "The table below associates some common register names used in CMSIS to the register names used in Technical Reference Manuals."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/register_mapping.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/register_mapping.md"
license: "Apache-2.0"
mode: "V"
---

The table below associates some common register names used in CMSIS to the register names 
used in Technical Reference Manuals.



| CMSIS Register Name | Cortex-M3/M4/M7 | Cortex-M0/M0+ | Register Name |
|---|---|---|---|
| Nested Vectored Interrupt Controller (NVIC) Register Access |  |  |  |
| NVIC->ISER[] | NVIC_ISER0..7 | ISER | Interrupt Set-Enable Registers |
| NVIC->ICER[] | NVIC_ICER0..7 | ICER | Interrupt Clear-Enable Registers |
| NVIC->ISPR[] | NVIC_ISPR0..7 | ISPR | Interrupt Set-Pending Registers |
| NVIC->ICPR[] | NVIC_ICPR0..7 | ICPR | Interrupt Clear-Pending Registers |
| NVIC->IABR[] | NVIC_IABR0..7 | - | Interrupt Active Bit Register |
| NVIC->IP[] | NVIC_IPR0..59 | IPR0..7 | Interrupt Priority Register |
| NVIC->STIR | STIR | - | Software Triggered Interrupt Register |
| System Control Block (SCB) Register Access |  |  |  |
| SCB->CPUID | CPUID | CPUID | CPUID Base Register |
| SCB->ICSR | ICSR | ICSR | Interrupt Control and State Register |
| SCB->VTOR | VTOR | - | Vector Table Offset Register |
| SCB->AIRCR | AIRCR | AIRCR | Application Interrupt and Reset Control Register |
| SCB->SCR | SCR | SCR | System Control Register |
| SCB->CCR | CCR | CCR | Configuration and Control Register |
| SCB->SHP[] | SHPR1..3 | SHPR2..3 | System Handler Priority Registers |
| SCB->SHCSR | SHCSR | SHCSR | System Handler Control and State Register |
| SCB->CFSR | CFSR | - | Configurable Fault Status Registers |
| SCB->HFSR | HFSR | - | HardFault Status Register |
| SCB->DFSR | DFSR | - | Debug Fault Status Register |
| SCB->MMFAR | MMFAR | - | MemManage Fault Address Register |
| SCB->BFAR | BFAR | - | BusFault Address Register |
| SCB->AFSR | AFSR | - | Auxiliary Fault Status Register |
| SCB->PFR[] | ID_PFR0..1 | - | Processor Feature Registers |
| SCB->DFR | ID_DFR0 | - | Debug Feature Register |
| SCB->ADR | ID_AFR0 | - | Auxiliary Feature Register |
| SCB->MMFR[] | ID_MMFR0..3 | - | Memory Model Feature Registers |
| SCB->ISAR[] | ID_ISAR0..4 | - | Instruction Set Attributes Registers |
| SCB->CPACR | CPACR | - | Coprocessor Access Control Register |
| System Control and ID Registers not in the SCB (SCnSCB) Register Access |  |  |  |
| SCnSCB->ICTR | ICTR | - | Interrupt Controller Type Register |
| SCnSCB->ACTLR | ACTLR | - | Auxiliary Control Register |
| System Timer (SysTick) Control and Status Register Access |  |  |  |
| SysTick->CTRL | STCSR | SYST_CSR | SysTick Control and Status Register |
| SysTick->LOAD | STRVR | SYST_RVR | SysTick Reload Value Register |
| SysTick->VAL | STCVR | SYST_CVR | SysTick Current Value Register |
| SysTick->CALIB | STCR | SYST_CALIB | SysTick Calibaration Value Register |
| Data Watchpoint and Trace (DWT) Register Access |  |  |  |
| DWT->CTRL | DWT_CTRL | - | Control Register |
| DWT->CYCCNT | DWT_CYCCNT | - | Cycle Count Register |
| DWT->CPICNT | DWT_CPICNT | - | CPI Count Register |
| DWT->EXCCNT | DWT_EXCCNT | - | Exception Overhead Count Register |
| DWT->SLEEPCNT | DWT_SLEEPCNT | - | Sleep Count Register |
| DWT->LSUCNT | DWT_LSUCNT | - | LSU Count Register |
| DWT->FOLDCNT | DWT_FOLDCNT | - | Folded-instruction Count Register |
| DWT->PCSR | DWT_PCSR | - | Program Counter Sample Register |
| DWT->COMP0..3 | DWT_COMP0..3 | - | Comparator Register 0..3 |
| DWT->MASK0..3 | DWT_MASK0..3 | - | Mask Register 0..3 |
| DWT->FUNCTION0..3 | DWT_FUNCTION0..3 | - | Function Register 0..3 |
| Instrumentation Trace Macrocell (ITM) Register Access |  |  |  |
| ITM->PORT[] | ITM_STIM0..31 | - | Stimulus Port Registers |
| ITM->TER | ITM_TER | - | Trace Enable Register |
| ITM->TPR | ITM_TPR | - | ITM Trace Privilege Register |
| ITM->TCR | ITM_TCR | - | Trace Control Register |
| Trace Port Interface (TPIU) Register Access |  |  |  |
| TPI->SSPSR | TPIU_SSPR | - | Supported Parallel Port Size Register |
| TPI->CSPSR | TPIU_CSPSR | - | Current Parallel Port Size Register |
| TPI->ACPR | TPIU_ACPR | - | Asynchronous Clock Prescaler Register |
| TPI->SPPR | TPIU_SPPR | - | Selected Pin Protocol Register |
| TPI->FFSR | TPIU_FFSR | - | Formatter and Flush Status Register |
| TPI->FFCR | TPIU_FFCR | - | Formatter and Flush Control Register |
| TPI->FSCR | TPIU_FSCR | - | Formatter Synchronization Counter Register |
| TPI->TRIGGER | TRIGGER | - | TRIGGER |
| TPI->FIFO0 | FIFO data 0 | - | Integration ETM Data |
| TPI->ITATBCTR2 | ITATBCTR2 | - | ITATBCTR2 |
| TPI->ITATBCTR0 | ITATBCTR0 | - | ITATBCTR0 |
| TPI->FIFO1 | FIFO data 1 | - | Integration ITM Data |
| TPI->ITCTRL | TPIU_ITCTRL | - | Integration Mode Control |
| TPI->CLAIMSET | CLAIMSET | - | Claim tag set |
| TPI->CLAIMCLR | CLAIMCLR | - | Claim tag clear |
| TPI->DEVID | TPIU_DEVID | - | TPIU_DEVID |
| TPI->DEVTYPE | TPIU_DEVTYPE | - | TPIU_DEVTYPE |
| Memory Protection Unit (MPU) Register Access |  |  |  |
| MPU->TYPE | MPU_TYPE | - | MPU Type Register |
| MPU->CTRL | MPU_CTRL | - | MPU Control Register |
| MPU->RNR | MPU_RNR | - | MPU Region Number Register |
| MPU->RBAR | MPU_RBAR | - | MPU Region Base Address Register |
| MPU->RASR | MPU_RASR | - | MPU Region Attribute and Size Register |
| MPU->RBAR_A1..3 | MPU_RBAR_A1..3 | - | MPU alias Register |
| MPU->RASR_A1..3 | MPU_RASR_A1..3 | - | MPU alias Register |
| Floating Point Unit (FPU) Register Access [only Cortex-M4 and Cortex-M7 both with FPU] |  |  |  |
| FPU->FPCCR | FPCCR | - | FP Context Control Register |
| FPU->FPCAR | FPCAR | - | FP Context Address Register |
| FPU->FPDSCR | FPDSCR | - | FP Default Status Control Register |
| FPU->MVFR0..1 | MVFR0..1 | - | Media and VFP Feature Registers |
