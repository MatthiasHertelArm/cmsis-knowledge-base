---
id: "drv-gpio-status-error-codes"
type: "concept"
domain: "drivers"
title: "GPIO Status Error Codes"
summary: "Negative values indicate errors (GPIO has specific codes in addition to common execution_status)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

Negative values indicate errors (GPIO has specific codes in addition to common execution_status). 
 
The GPIO driver has additional status error codes that are listed below.
Note that the GPIO driver also returns the common execution_status. 
  

### ARM_GPIO_ERROR_PIN

```c
ARM_GPIO_ERROR_PIN
```

The **pin** specified is not available.
