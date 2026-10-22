---
id: "view-fault-analysis-locate-fault-information-in-uninitialize"
type: "concept"
domain: "trace"
title: "Fault Analysis: Locate fault information in uninitialized memory"
summary: "For preservation of the saved fault information after system reset, RAM for the ARM_FaultInfo structure should be placed to a memory region that is not cleared (or initialized) by a system restart (reset)."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/fault.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/fault.md#locate-fault-information-in-uninitialized-memory"
license: "Apache-2.0"
mode: "V"
---

For preservation of the saved fault information after system reset, RAM for the ARM_FaultInfo structure should be placed to a memory
region that is not cleared (or initialized) by a system restart (reset).

> **Note**
> - Make sure that you use normal, non-cacheable, and non-shareable memory for fault information data.

For size of this memory section take a look at flt_req. 

To setup this uninitialized RAM, use either flt_create_mem_ls or flt_create_mem_uv procedure.


### Create memory region using linker script

If the linker script does not contain provisions for uninitialized memory section then, for respective toolchain, add the necessary section like described below:

**Arm Compiler:**

For the Arm Compiler toolchain add the following code snippet to the linker script (.sct file), in the part specifying RAM sections (usually before Heap section):

```
  RW_NOINIT <start_address> UNINIT 0x800 {
    *(.bss.noinit)
    *(.bss.noinit.*)
  }
```

> **Note**
> - `<start_address>` is the physical address in RAM where the section will start.
> - 0x800 is the size of the section covering also default Event Recorder data, adjust that as necessary


**GCC:**

For the GCC toolchain add the following code snippet to the linker script (.ld file), in the part specifying RAM sections (usually before Heap section):

```
  .noinit (NOLOAD) :
  {
    . = ALIGN(4);
    __noinit_start = .;
    *(.noinit)
    *(.noinit.*)
    . = ALIGN(4);
    __noinit_end = .;
  } > RAM
```

> **Note**
> - The code snippet above expects defined RAM memory region, if RAM region is not defined then adapt the script accordingly.

### Create memory region using µVision

To setup this uninitialized RAM in the µVision, follow the steps below:

 1. In the **Options for Target** dialog, define a Read/Write Memory Area that is not initialized, by splitting available internal RAM into 2 areas.

   For example, split IRAM1 into two regions. Reduce size of IRAM1 to 0x800 and create an IRAM2 area with remaining of the available RAM. Enable **NoInit** for the IRAM1 region.

   (figure: Create RAM area)


 2. In the **Options for Component Class 'CMSIS-View'** dialog (opens with right-click on **ARM_FaultStorage.c** in the **Project** window), on the **Memory** tab, assign **Zero Initialized Data** to the IRAM1 region.

    (figure: Create RAM area)

 3. Build the application to place the ARM_FaultInfo structure to uninitialized RAM.
