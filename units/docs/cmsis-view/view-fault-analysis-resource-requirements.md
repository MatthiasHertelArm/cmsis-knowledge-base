---
id: "view-fault-analysis-resource-requirements"
type: "concept"
domain: "trace"
title: "Fault Analysis: Resource requirements"
summary: "This section contains the the technical data of the Fault component firmware."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/fault.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/fault.md#resource-requirements"
license: "Apache-2.0"
mode: "V"
---

This section contains the the technical data of the Fault component firmware.

**RAM:**

The Fault component uses the ARM_FaultInfo structure to save information when the fault occurs. The size depends on the Arm Cortex-M core for which the code was compiled:

 - If the Arm Cortex-M core contains Fault Registers (e.g. Cortex-M33), the ARM_FaultInfo structure requires **140 bytes** of uninitialized RAM memory.
 - If the Arm Cortex-M core does not contain Fault Registers (e.g. Cortex-M0), the ARM_FaultInfo structure requires **104 bytes** of uninitialized RAM memory.

**ROM:**

The functions of the Fault component require the following amounts of ROM memory:

 - TheARM_FaultSave function requires up to **0.5 KB** of ROM memory.
 - The ARM_FaultRecord function requires approximately up to **1.5 KB** of ROM memory.
 - The ARM_FaultPrint function requires approximately up to **2.5 KB** of ROM memory.
# Using Fault component

The following steps explain how to enable Fault component using the µVision. Other tools might use different ways to accomplish this.

**For User Code:**

 1. flt_add_component.
 2. Locate fault information in uninitialized memory to be preserved over system reset.
