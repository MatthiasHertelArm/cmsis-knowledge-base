---
id: "armsw-execute-validation-project-build-and-execute-projects-with-arm-virt"
type: "concept"
domain: "rtos"
title: "Execute Validation Project: Build and Execute Projects with Arm Virtual Hardware"
summary: "The simplest way to execute this validation suite is to build and run configured targets using Python script:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md#build-and-execute-projects-with-arm-virtual-hardware"
license: "Apache-2.0"
mode: "V"
---

The simplest way to execute this validation suite is to build and run configured targets using Python script:

```Shell
 ./Project $ python build.py build run
```

Use `--verbose` command to output more information:

```Shell
 ./Project $ python build.py --verbose build run
```

Above commands will build all defined projects and run each target. One might be interested in only one RTOS/Device/Compiler combination and can also build and run a project for specific combination, see below.
