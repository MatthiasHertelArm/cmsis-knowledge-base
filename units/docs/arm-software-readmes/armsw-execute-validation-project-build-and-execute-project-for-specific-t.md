---
id: "armsw-execute-validation-project-build-and-execute-project-for-specific-t"
type: "concept"
domain: "rtos"
title: "Execute Validation Project: Build and Execute Project for Specific Target"
summary: "To build and execute validation suite for specific target use the following command:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md#build-and-execute-project-for-specific-target"
license: "Apache-2.0"
mode: "V"
---

To build and execute validation suite for specific target use the following command:

```Shell
 ./Project $ python build.py build run -r {RTOS} -d {DEVICE} -c {COMPILER}
```

> Note: Mentioned commands can be executed either in Windows command prompt or bash shell.

Python script is used to simplify build commands and Virtual Hardware Target model execution. One can call cbuild and execute the model manually, see below.
