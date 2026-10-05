---
id: "rtx-create-an-rtx5-project-rtx5-header-file"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project: RTX5 Header File"
summary: "Every implementation of the CMSIS-RTOS2 API can bring its own additional features. RTX5 adds a couple of functions for the idle more, for error notifications, and special system timer functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md#rtx5-header-file"
license: "Apache-2.0"
mode: "V"
---

Every implementation of the CMSIS-RTOS2 API can bring its own additional features. RTX5 adds a couple of functions for the idle more, for error notifications, and special system timer functions. It is also using macros for control block and memory sizes.

If you require some of the RTX specific functions in your application code, include the header file rtx_os.h:

```c
#include "rtx_os.h"
```
