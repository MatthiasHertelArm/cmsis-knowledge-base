---
id: "core-cache-functions-level-1"
type: "concept"
domain: "core"
title: "Cache Functions (Level-1)"
summary: "Functions for level-1 instruction and data cache."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_cm7_cache.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_cm7_cache.txt"
license: "Apache-2.0"
mode: "V"
---

Functions for level-1 instruction and data cache.
 
Enhanced Cortex processors (like M7 and M55) include a memory system, which includes an optional
Harvard level-1 data and instruction cache with ECC. The optional CPU cache has an instruction
and data cache with sizes of `[0;4;8;16;32;64]KB`.
Both instruction and data cache RAM can be configured at implementation time to have Error
Correcting Code (ECC) to protect the data stored in the memory from errors.

All cache maintenance operations are executed by writing to registers in the memory mapped
System Control Space (SCS) region of the internal PPB memory space. 

**Note:** 
After reset, you must invalidate each cache before enabling it. 
 
The functions are grouped for:
 - Icache_functions_m7
 - Dcache_functions_m7
