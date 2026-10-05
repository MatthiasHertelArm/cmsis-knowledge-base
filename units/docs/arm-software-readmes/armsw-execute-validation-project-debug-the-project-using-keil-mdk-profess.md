---
id: "armsw-execute-validation-project-debug-the-project-using-keil-mdk-profess"
type: "concept"
domain: "rtos"
title: "Execute Validation Project: Debug the Project using Keil MDK-Professional"
summary: "All projects can be opened and debugged using Keil MDK-Professional no matter whether the project was build using Python script or manually with cbuild. After the project was successfully built, follow the steps below:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md#debug-the-project-using-keil-mdk-professional"
license: "Apache-2.0"
mode: "V"
---

All projects can be opened and debugged using Keil MDK-Professional no matter whether the project was build using Python script or manually with cbuild.
After the project was successfully built, follow the steps below:

1. Go into folder Validation.{RTOS}+{DEVICE}_{COMPILER} and double click the generated cprj file
2. In uVision, open dialog Options for Target->Debug and configure the debugger
    - Configuration File 'fvp_config.txt' for each target can be found in folder [**.\Layer\Board**](https://github.com/ARM-software/CMSIS-RTOS2_Validation/tree/main/Layer/Board)

Documentation on how to [use Keil MDK with Arm Virtual Hardware](https://arm-software.github.io/AVH/main/infrastructure/html/run_mdk_pro.html) describes how to configure the debugger.
