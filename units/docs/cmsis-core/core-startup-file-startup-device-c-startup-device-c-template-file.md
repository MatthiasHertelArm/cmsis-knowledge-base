---
id: "core-startup-file-startup-device-c-startup-device-c-template-file"
type: "concept"
domain: "core"
title: "Startup File startup_`<Device>`.c: startup_Device.c Template File"
summary: "CMSIS-Core cmsis_template_files include a startup_Device.c file that can be used as a starting point for chip vendors to implement own device-specific startup file."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md#startup-device-c-template-file"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core cmsis_template_files include a `startup_Device.c` file that can be used as a starting point for chip vendors to implement own device-specific startup file.

The C startup file relys on certain compiler specific preprocessor defines specified in CMSIS compiler headers:

 - __INITIAL_SP
 - __STACK_LIMIT
 - __PROGRAM_START
 - __VECTOR_TABLE
 - __VECTOR_TABLE_ATTRIBUTE
 - __STACK_SEAL (for Armv8-M/v8.1-M)
 - __TZ_set_STACKSEAL_S (for Armv8-M/v8.1-M)

The stack sealing and the initialization for the Stack Limit register is done in function ` Reset_Handler(void)`:

```c
/*----------------------------------------------------------------------------
  Reset Handler called on controller reset
 *----------------------------------------------------------------------------*/
__NO_RETURN void Reset_Handler(void)
{
  __set_PSP((uint32_t)(&__INITIAL_SP));

  __set_MSPLIM((uint32_t)(&__STACK_LIMIT));
  __set_PSPLIM((uint32_t)(&__STACK_LIMIT));

#if defined (__ARM_FEATURE_CMSE) && (__ARM_FEATURE_CMSE == 3U)
  __TZ_set_STACKSEAL_S((uint32_t *)(&__STACK_SEAL));
#endif

  SystemInit();                             /* CMSIS System Initialization */
  __PROGRAM_START();                        /* Enter PreMain (C library entry point) */
}
```

> **Note**
> - Stack Sealing also requires the application project to use a scatter file (or a linker script) as explained in RTOS_TrustZone_stacksealing section.
