---
id: "core-pmu-functions-for-armv8-1-m"
type: "concept"
domain: "core"
title: "PMU Functions for Armv8.1-M"
summary: "Functions that relate to the Performance Monitoring Unit."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_pmu8.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_pmu8.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that relate to the Performance Monitoring Unit.

The following functions support the Performance Monitoring Unit (PMU) that is available on the Cortex-M55/M85 processors.

The PMU is used to monitor events that occur during run-time of an application.

**Example:**
```
// Initialize counter variables
 
unsigned int cycle_count = 0;
unsigned int l1_dcache_miss_count = 0;
unsigned int instructions_retired_count = 0;
 
// Enable the PMU
// Note: Before using the PMU, software needs to ensure 
// that trace is enabled via the Debug Exception Monitor Control Register, DEMCR:
// CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;
 
ARM_PMU_Enable();
 
// Configure Event Counter Register 0 to count instructions retired
// Configure Event Counter Register 1 to count L1 D-Cache misses
 
ARM_PMU_Set_EVTYPER(0, ARM_PMU_INST_RETIRED);
ARM_PMU_Set_EVTYPER(1, ARM_PMU_L1D_CACHE_MISS_RD);
 
// Reset Event Counters and Cycle Counter
 
ARM_PMU_EVCNTR_ALL_Reset();
ARM_PMU_CYCCNT_Reset();
 
// Start incrementing Cycle Count Register and Event Counter Registers 0 & 1
 
ARM_PMU_CNTR_Enable(PMU_CNTENSET_CCNTR_ENABLE_Msk|PMU_CNTENSET_CNT0_ENABLE_Msk|PMU_CNTENSET_CNT1_ENABLE_Msk);
 
// Code you want to measure here
 
// Stop incrementing Cycle Count Register and Event Counter Registers 0 & 1
 
ARM_PMU_CNTR_Disable(PMU_CNTENCLR_CCNTR_ENABLE_Msk|PMU_CNTENCLR_CNT0_ENABLE_Msk|PMU_CNTENCLR_CNT1_ENABLE_Msk);
 
// Get cycle count, number of instructions retired and number of L1 D-Cache misses (on read)
 
cycle_count = cycle_count + ARM_PMU_Get_CCNTR();
instructions_retired_count = instructions_retired_count + ARM_PMU_Get_EVCNTR(0);
l1_dcache_miss_count = l1_dcache_miss_count + ARM_PMU_Get_EVCNTR(1);      // Note: D-Cache must be enabled using
                                                                          // SCB_EnableDCache() for meaningful result.
```
