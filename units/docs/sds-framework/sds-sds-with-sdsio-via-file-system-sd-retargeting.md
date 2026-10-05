---
id: "sds-sds-with-sdsio-via-file-system-sd-retargeting"
type: "concept"
domain: "test"
title: "SDS with SDSIO via File System (SD Card): Retargeting"
summary: "For retargeting of standard C run-time library file operations the CMSIS-Compiler component is required:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:layer/sdsio/filesystem/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/layer/sdsio/filesystem/README.md#retargeting"
license: "Apache-2.0"
mode: "V"
---

For retargeting of standard C run-time library file operations the CMSIS-Compiler component is required:

```yml
  - component: CMSIS-Compiler:File Interface:MDK-MW File System
```

For more information refer to [Using File System Interface](https://arm-software.github.io/SDS-Framework/main/sdsio.html#using-file-system-interface).
