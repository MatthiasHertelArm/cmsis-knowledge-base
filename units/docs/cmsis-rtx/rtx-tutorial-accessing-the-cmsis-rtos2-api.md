---
id: "rtx-tutorial-accessing-the-cmsis-rtos2-api"
type: "concept"
domain: "rtos"
title: "tutorial: Accessing the CMSIS-RTOS2 API"
summary: "To access any of the CMSIS-RTOS2 features in our application code, it is necessary to include the following header file."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#accessing-the-cmsis-rtos2-api"
license: "Apache-2.0"
mode: "V"
---

To access any of the CMSIS-RTOS2 features in our application code, it is necessary to include the following header file.

```c
#include <cmsis_os2.h>
```

This header file is maintained by Arm as part of the CMSIS-RTOS2 standard. For Keil RTX5, this is the default API. Other RTOS will have their own proprietary API but may provide a wrapper layer to implement the CMSIS-RTOS2 API so they can be used where compatibility with the CMSIS standard is required.
