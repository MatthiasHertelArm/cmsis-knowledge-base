---
id: "core-scatter-loading-description-file-d"
type: "concept"
domain: "core"
title: "Scatter-Loading description file `<device>`_ac6.sct"
summary: "A scatter file for linking is required when using a startup_c_pg."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_linker_sct.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_linker_sct.md"
license: "Apache-2.0"
mode: "V"
---

A scatter file for linking is required when using a startup_c_pg.

The linker_sct_pg contains regions for:

 - Code (read-only data, execute-only data)
 - RAM (read/write data, zero-initialized data)
 - Stack
 - Heap
 - Stack seal (for Armv8-M/v8.1-M)
 - CMSE veneer (for Armv8-M/v8.1-M)

Within the scatter file, the user needs to specify a set of macros. The scatter file is passed through the C preprocessor which uses these macros to calculate the start address and the size of the different regions.

```
/*--------------------- Flash Configuration ----------------------------------
; <h> Flash Configuration
;   <o0> Flash Base Address <0x0-0xFFFFFFFF:8>
;   <o1> Flash Size (in Bytes) <0x0-0xFFFFFFFF:8>
; </h>
 *----------------------------------------------------------------------------*/
#define __ROM_BASE      0x00000000
#define __ROM_SIZE      0x00080000

/*--------------------- Embedded RAM Configuration ---------------------------
; <h> RAM Configuration
;   <o0> RAM Base Address    <0x0-0xFFFFFFFF:8>
;   <o1> RAM Size (in Bytes) <0x0-0xFFFFFFFF:8>
; </h>
 *----------------------------------------------------------------------------*/
#define __RAM_BASE      0x20000000
#define __RAM_SIZE      0x00040000

/*--------------------- Stack / Heap Configuration ---------------------------
; <h> Stack / Heap Configuration
;   <o0> Stack Size (in Bytes) <0x0-0xFFFFFFFF:8>
;   <o1> Heap Size (in Bytes) <0x0-0xFFFFFFFF:8>
; </h>
 *----------------------------------------------------------------------------*/
#define __STACK_SIZE    0x00000200
#define __HEAP_SIZE     0x00000C00

/*--------------------- CMSE Veneer Configuration ---------------------------
; <h> CMSE Veneer Configuration
;   <o0>  CMSE Veneer Size (in Bytes) <0x0-0xFFFFFFFF:32>
; </h>
 *----------------------------------------------------------------------------*/
#define __CMSEVENEER_SIZE    0x200
```

> **Note**
> - The stack is placed at the end of the available RAM and is growing downwards whereas the Heap is placed after the application data and growing upwards.
