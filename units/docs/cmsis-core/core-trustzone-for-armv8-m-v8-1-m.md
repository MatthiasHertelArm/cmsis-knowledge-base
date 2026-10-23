---
id: "core-trustzone-for-armv8-m-v8-1-m"
type: "concept"
domain: "core"
title: "TrustZone for Armv8-M/v8.1-M"
summary: "Functions that related to optional Armv8-M and Armv8.1-M security extension"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_trustzone.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_trustzone.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that related to optional Armv8-M and Armv8.1-M security extension

The Armv8-M architecture has optional Armv8-M security extension based on Arm TrustZone technology.
To access Arm TrustZone extensions for Armv8-M additional CMSIS functions are provided:
 - coreregister_trustzone_functions
 - nvic_trustzone_functions
 - systick_trustzone_functions
 - sau_trustzone_functions
 - stacksealing_support_trustzone_functions
 - context_trustzone_functions


### __STACK_SEAL

```c
__STACK_SEAL
```

 Compiler/linker symbol specifying the location of the stack seal.

The address of the specified symbol is used to set the stack seal during low level init.
This is compiler/linker specific. CMSIS specifies common default for supported compilers. 

**Note:** This define is only intended to be used by the startup_c_pg.
