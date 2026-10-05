---
id: "rtx-operation-using-interrupts-on-cortex-m"
type: "concept"
domain: "rtos"
title: "operation: Using Interrupts on Cortex-M"
summary: "On Cortex-M processors, the RTX5 kernel uses the following interrupt exceptions. The table below also lists the priorities that must be assigned to these interrupts."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#using-interrupts-on-cortex-m"
license: "Apache-2.0"
mode: "V"
---

On Cortex-M processors, the RTX5 kernel uses the following interrupt exceptions.  The table below also lists the priorities that must be assigned to these interrupts.

Handler | Priority | Interrupt/Exception
:-------|:---------|:----------------------------
SysTick | lowest   | Kernel system timer interrupt to generate periodic timer ticks
PendSV  | lowest   | PendSV (request for system-level service) when calling certain RTX functions from **Handler mode**
SVC     | lowest+1 | Supervisor Call used to enter the RTOS kernel from **Thread mode**

Other device interrupts can be used without limitation. For Arm Cortex-M3/M4/M7 \if ARMv8M /M23/M33/M35P/M55/M85 \endif  processors, interrupts are never disabled by RTX Kernel.

**Usage of interrupt priority grouping**

- The interrupt priority grouping should be configured using the CMSIS-Core function NVIC_SetPriorityGrouping before calling the function osKernelStart. The RTX kernel uses the priority group value to setup the priority for SysTick and PendSV interrupts.
- The RTX kernel sets the priority for the interrupts/exceptions listed in above table and uses the lowest two priority levels.
- Do not change the priority used by the RTX kernel. If this cannot be avoided, ensure that the preempt priority of SysTick/PendSV is lower than SVC.
- Permitted priority group values are 0 to 6. The priority group value 7 will cause RTX to fail as there is only one priority level available.
- The **main stack** is used to run the RTX functionality. It is therefore required to configure sufficient stack for the RTX kernel execution.

**Code Example**

```c
osKernelInitialize();                            // initialize RTX
NVIC_SetPriorityGrouping (3);                    // setup priority grouping
tread_id = osThreadNew(tread_func, NULL, NULL);  // create some threads
osKernelStart ();                                // start RTX kernel
```
