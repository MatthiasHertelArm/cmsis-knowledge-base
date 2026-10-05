---
id: "core-debug-access"
type: "concept"
domain: "core"
title: "Debug Access"
summary: "Debug Access to the Instrumented Trace Macrocell (ITM)"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_debug.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_debug.txt"
license: "Apache-2.0"
mode: "V"
---

Debug Access to the Instrumented Trace Macrocell (ITM)

CMSIS provides additional debug functions to enlarge the Debug Access. 
Data can be transmitted via a certain global buffer variable towards the target system.    

The Cortex-M3 / Cortex-M4 / Cortex-M7 incorporates the **Instrumented Trace Macrocell (ITM)** that 
provides together with the **Serial Wire Output (SWO)** trace capabilities for the 
microcontroller system. The ITM has 32 communication channels; two ITM 
communication channels are used by CMSIS to output the following information:

- **ITM Channel 0**: implements the ITM_SendChar function 
which can be used for printf-style output via the debug interface.

- **ITM Channel 31**: is reserved for the RTOS kernel and can be used for kernel awareness debugging.

**Note:**
- ITM channels have 4 groups with 8 channels each, whereby each group can be configured for 
access rights in the Unprivileged level. 
- The ITM channel 0 can be enabled for the user task. 
- ITM channel 31 can be accessed only in Privileged mode 
from the RTOS kernel itself. The ITM channel 31 has been selected for the RTOS kernel because some 
kernels may use the Privileged level for program execution.
