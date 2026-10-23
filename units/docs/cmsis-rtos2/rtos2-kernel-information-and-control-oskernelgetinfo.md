---
id: "rtos2-kernel-information-and-control-oskernelgetinfo"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelGetInfo"
summary: "The function osKernelGetInfo retrieves the API and kernel version of the underlying RTOS kernel and a human readable identifier string for the kernel. It can be safely called before the RTOS is initialized or started (call to osKernelInitialize or osKernelStart)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osKernelGetInfo (osVersion_t *version, char *id_buf, uint32_t id_size)
```


The function **osKernelGetInfo** retrieves the API and kernel version of the underlying RTOS kernel and a human readable
identifier string for the kernel. It can be safely called before the RTOS is initialized or started (call to
osKernelInitialize or osKernelStart).

Possible osStatus_t return values:
- **osOK** in case of success.
- **osError** if an unspecific error occurred.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
void info (void) {
  char infobuf[100];
  osVersion_t osv;
  osStatus_t status;
 
  status = osKernelGetInfo(&osv, infobuf, sizeof(infobuf));
  if(status == osOK) {
    printf("Kernel Information: %s\r\n", infobuf);
    printf("Kernel Version    : %d\r\n", osv.kernel);
    printf("Kernel API Version: %d\r\n", osv.api);
  }
}
```
