---
id: "armsw-execute-validation-project-manually-build-and-execute-project-for-s"
type: "concept"
domain: "rtos"
title: "Execute Validation Project: Manually Build and Execute Project for Specific Target"
summary: "Behind the scenes, build.py script calls cbuild and VHT model executable to build and execute the test suite."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md#manually-build-and-execute-project-for-specific-target"
license: "Apache-2.0"
mode: "V"
---

Behind the scenes, build.py script calls cbuild and VHT model executable to build and execute the test suite.

The following command will build the project for specified RTOS/Device/Compiler and its output is an executable (either Validation.axf or Validation.elf):

```Shell
 ./Project $ cbuild Validation.csolution.yml --update-rte --context .{RTOS}+{DEVICE} --toolchain {COMPILER}
 ```

Executable file is then used as input parameter when calling Virtual Hardware Target model to run the validation:

```Shell
 ./Project $ {AVH_MODEL} -f ../Layer/Board/{DEVICE}/fvp_config.txt -a out/Validation/{DEVICE}/{RTOS}/Validation.axf
```

Please see a table below for a possible {AVH_MODEL} variable value when a project for specified {DEVICE} was built:

| AVH_MODEL                 | DEVICE  |
|---------------------------|---------|
| FVP_MPS2_Cortex-M0plus    | CM0plus |
| FVP_MPS2_Cortex-M3        | CM3     |
| FVP_MPS2_Cortex-M4        | CM4     |
| FVP_MPS2_Cortex-M7        | CM7     |
| FVP_MPS2_Cortex-M23       | CM23    |
| FVP_MPS2_Cortex-M33       | CM33    |
| FVP_MPS2_Cortex-M55       | CM55    |
| FVP_MPS2_Cortex-M85       | CM85    |
