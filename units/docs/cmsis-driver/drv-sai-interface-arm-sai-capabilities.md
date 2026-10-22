---
id: "drv-sai-interface-arm-sai-capabilities"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_CAPABILITIES"
summary: "An SAI driver can be implemented with different capabilities (for example protocol support). The data fields of this structure encode the capabilities implemented by this driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
ARM_SAI_CAPABILITIES
```


An SAI driver can be implemented with different capabilities (for example protocol support). The data fields of this
structure encode the capabilities implemented by this driver. If a certain hardware peripheral is not able to handle one
of the protocols directly (not advertised using ARM_SAI_CAPABILITIES), then it might be possible to implement it using
the Driver_SAI_User (if supported).

**Returned by:**
  - ARM_SAI_GetCapabilities
****************************************************************************************************************
